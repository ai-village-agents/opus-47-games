import pexpect, sys, re, time

child = pexpect.spawn('/usr/games/dfrotz',
    ['-p','-m','-s','1','-w','80','-h','200',
     '/home/computeruse/games/witness.z3'],
    encoding='latin-1', timeout=20)

def drain(deadline=25, idle=0.6):
    out = ''
    start = time.time()
    last_data = time.time()
    yes_handled_at_len = -1
    while time.time() - start < deadline:
        try:
            chunk = child.read_nonblocking(size=8192, timeout=idle)
            out += chunk
            last_data = time.time()
            if 'YES or NO' in chunk and out.rstrip().endswith('>') and len(out) > yes_handled_at_len:
                child.sendline('yes')
                yes_handled_at_len = len(out) + 10
                out += '\n[AUTO-YES]\n'
                time.sleep(0.4)
                continue
        except pexpect.TIMEOUT:
            if time.time() - last_data > idle:
                if out.rstrip().endswith('>'):
                    return out
                continue
        except pexpect.EOF:
            return out
    return out

initial = drain(deadline=8)

with open('/tmp/witness_cmds.txt') as f:
    cmds = [c.strip() for c in f if c.strip()]

new_cmds = []
wait_count = 0
for idx, c in enumerate(cmds):
    if c == 'wait':
        wait_count += 1
        if wait_count == 2:
            new_cmds.append('wait until 9:04')
            continue
    if c == 'read it' and cmds[idx-1] == 'get receipt':
        new_cmds.append(c)
        new_cmds.append('drop receipt')
        new_cmds.append('get handgun')
        continue
    if c == 'analyze muddy gun':
        new_cmds.append('analyze handgun')
        continue
    if c == 'analyze piece':
        new_cmds.append('analyze green wire piece')
        continue
    if c == 'handcuff monica':
        # NEW: Hide behind lounge BEFORE midnight so Monica goes to clock
        new_cmds.append('hide behind lounge')
        new_cmds.append('wait until 12:30')
        new_cmds.append('wait for monica')
        new_cmds.append('stand up')
    new_cmds.append(c)

sys.stderr.write(f"Total cmds: {len(new_cmds)}\n")
log = open('/tmp/witness_log8.txt','w')
log.write(initial)
for i, c in enumerate(new_cmds):
    log.write(f"\n>>> [{i}] {c}\n")
    child.sendline(c)
    out = drain(deadline=25)
    log.write(out)
    if 'restart, restore' in out.lower() or 'you have died' in out.lower():
        sys.stderr.write(f"GAME OVER at {i}: {c}\n"); break
    if i % 10 == 0:
        sys.stderr.write(f"[{i}/{len(new_cmds)}] {c}\n")
log.close()
