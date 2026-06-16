import pexpect, sys, re, time

with open('/tmp/ench/part0.cmds') as f: part0 = [l.strip() for l in f if l.strip()]
with open('/tmp/ench/part3.cmds') as f: part3 = [l.strip() for l in f if l.strip()]

seed = sys.argv[1] if len(sys.argv) > 1 else '1'
child = pexpect.spawn('/usr/games/dfrotz', ['-p', '-m', '-s', seed, '-w', '80', '-h', '200', '/home/computeruse/games/enchanter.z3'], encoding='latin-1', timeout=10)

log = open(f'/tmp/ench/out3_s{seed}.txt', 'w')

# Consume initial banner up to first prompt
child.expect_exact('>')
log.write(child.before)

def send(cmd):
    child.sendline(cmd)
    child.expect_exact('>')
    out = child.before
    log.write(out)
    return out

# Send part 0
for c in part0:
    send(c)

# Re-learn zifmia and vaxum
send('learn zifmia and vaxum')

# Wander up to 30 moves, alternating e/w in Hall of Mirrors
moves = ['e','w'] * 20 + ['n','s','u','d'] * 5
pacified = False
relearn_attempts = 0
for m in moves:
    out = send(m)
    if 'comes into view' in out or 'stares in your direction' in out:
        # immediately zifmia
        out2 = send('zifmia adventurer')
        low = out2.lower()
        if "spell is not committed" in low or "isn't committed" in low or "don't have" in low or 'thaumaturgy' in low:
            # not in view or spell forgotten - try relearn
            if relearn_attempts < 3:
                send('learn zifmia and vaxum')
                relearn_attempts += 1
            continue
        # check vaxum
        out3 = send('vaxum adventurer')
        if "can't see" in out3.lower():
            continue
        out4 = send('show egg to adventurer')
        if "doubt" in out4 or "can't see" in out4.lower():
            continue
        pacified = True
        break

print(f"pacified: {pacified}")

if pacified:
    door_seen = False
    for _ in range(15):
        out = send('e')
        if 'guarded door' in out.lower() or "don't bother" in out.lower():
            door_seen = True
            break
    print(f"door_seen: {door_seen}")
    if door_seen:
        for c in part3:
            try:
                child.sendline(c)
                child.expect_exact('>', timeout=5)
                log.write(child.before)
            except: break

try:
    child.sendline('score')
    child.expect_exact('>', timeout=5)
    log.write(child.before)
except: pass
try:
    child.sendline('quit')
    child.expect('affirmative', timeout=5)
    log.write(child.before)
    child.sendline('y')
    time.sleep(0.5)
    log.write(child.read_nonblocking(20000, timeout=2))
except: pass
log.close()
