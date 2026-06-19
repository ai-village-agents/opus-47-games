import re, pexpect, sys, time

INFOTATER = {
    'bloodworm': ['white','gray','black','red','black'],
    'brogmoid':  ['red','purple','red','black','purple'],
    'dorn':      ['gray','purple','black','gray','white'],
    'dryad':     ['black','gray','white','red','red'],
    'grue':      ['black','black','red','black','purple'],
    'hellhound': ['purple','white','gray','red','gray'],
    'kobold':    ['red','purple','black','purple','red'],
    'nabiz':     ['purple','black','black','black','red'],
    'orc':       ['red','gray','purple','gray','red'],
    'rotgrub':   ['gray','red','gray','purple','red'],
    'surmin':    ['black','black','purple','red','black'],
    'yipple':    ['gray','purple','white','purple','black'],
}
GAME = '/home/computeruse/games/sorcerer-r18-s860904.z3'
SEED = 1
LOG = '/tmp/sorc_log2.txt'
logf = open(LOG, 'w')
score_pat = re.compile(r'(?:Your score is|Score:)\s*(\d+)')
last_score = 0

child = pexpect.spawn('/usr/games/dfrotz', ['-s', str(SEED), '-w', '200', GAME],
                     encoding='utf-8', timeout=30)

def drain(idle=0.3, deadline=5):
    out = ''
    start = time.time()
    last = time.time()
    while time.time() - start < deadline:
        try:
            ch = child.read_nonblocking(8192, timeout=idle)
            out += ch
            last = time.time()
        except pexpect.TIMEOUT:
            if time.time() - last > idle:
                if out.rstrip().endswith('>') or 'affirmative)' in out:
                    return out
        except pexpect.EOF:
            return out
    return out

def send(cmd):
    global last_score
    logf.write(f'\n>>> {cmd}\n')
    child.sendline(cmd)
    out = drain()
    logf.write(out)
    logf.flush()
    while 'affirmative)' in out:
        if 'leave the game' in out or 'restart' in out or 'this session' in out:
            child.sendline('n')
        else:
            child.sendline('y')
        out = drain()
        logf.write(out)
    return out

def score():
    out = send('score')
    m = re.search(r'(\d+)\s*\(total of', out) or re.search(r'have so far scored (\d+)', out)
    if m: return int(m.group(1))
    return None

# ---- Section 1+2: Guild ----
# Step2: frotz me. get up. w. s. s. w. take vial and matchbook. e.
# open receptacle. put matchbook into receptacle. close receptacle.
# e. take scroll. gnusto meef. w. n. n. w. look behind hanging.
# open drawer. take key and journal. open journal. read journal.

s2_first = [
    'wait',           # dream
    'frotz me',
    'stand up',
    'w',              # hallway
    's', 's',         # to area
    'w',              # store room
    'get vial', 'get matchbook',
    'e',              # back lobby
    'open receptacle', 'put matchbook in receptacle', 'close receptacle',
    'e',              # library
    'get scroll', 'gnusto meef',
    'w',              # lobby
    'n', 'n',         # toward Belboz
    'w',              # Belboz's quarters
    'look behind hanging',
    'open drawer', 'open desk',
    'get key', 'get journal',
    'unlock journal with key',
    'open journal', 'read journal',
]

for c in s2_first:
    send(c)

# parse code
logf.flush()
with open(LOG) as f:
    log = f.read()
# Sorcerer journal: "Current code: BEAST" (a creature name)
m = re.search(r'[Cc]urrent code:\s*(\w+)', log)
if not m:
    # try last 5000 chars for a recognizable beast
    tail = log[-5000:]
    for b in INFOTATER:
        if b in tail.lower():
            m = re.match(r'(.*)', b)
            beast = b
            break
    else:
        print('NO CODE FOUND - aborting'); sys.exit(1)
else:
    beast = m.group(1).lower()
print('Code beast:', beast)
seq = INFOTATER.get(beast)
if not seq:
    print('UNKNOWN BEAST:', beast); sys.exit(1)
print('Sequence:', seq)

# Step2 continues: open vial, drink potion, drop vial+journal+key, e, s, s, open recept, get vial, d
s2_post_code = [
    'open vial', 'drink potion',
    'drop vial', 'drop journal', 'drop key',
    'e',              # back to hallway
    's', 's',         # to lobby
    'open receptacle', 'get vial',
    'd',              # cellar
]
for c in s2_post_code:
    send(c)

# Press buttons in INFOTATER sequence
for color in seq:
    send(f'press {color} button')

# Step2: take scroll, aimfiz belboz
send('get scroll')
send('aimfiz belboz')

print('SCORE after Section 2:', score())

# ---- Section 3: Forest of Yore / Twisted Forest ----
s3 = [
    'ne',
    'learn pulver',
    'learn izyuk', 'learn izyuk', 'learn izyuk',
    'e', 'ne',
    'pulver river',
    'd', 'ne',
    'get scroll', 'get guano',
    'gnusto fweep',
    'd', 'sw', 'u',
    'w', 'w',
    'ne', 'se', 'e',
    'lower flag', 'examine flag',
    'get aqua vial',
    'e',
    'put guano in barrel',
    'get scroll',
    'w', 'w',
    'izyuk me',
    'nw', 'sw', 'w',
]
for c in s3:
    send(c)
print('SCORE after Section 3:', score())

# ---- Section 4: Maze ----
s4_before = [
    'd', 'd', 's', 'w',
    'izyuk me',
    'w', 'w', 'n',
    'get zorkmid', 'get coin',
    's', 'e',
    'izyuk me',
    'e', 'e', 'ne', 'ne', 'e', 'e',
    'wake gnome',
    'give zorkmid to gnome', 'give coin to gnome',
    'e', 'e', 'n', 'n',
    'sleep',
    'learn fweep', 'learn fweep', 'learn fweep',
    'fweep me',
    'e',
]
for c in s4_before:
    send(c)

# Maze 14 moves: n. e. s. s. w. d. e. e. n. n. u. u. s. e.
maze = ['n','e','s','s','w','d','e','e','n','n','u','u','s','e']
for c in maze:
    send(c)

s4_mid = [
    'get scroll',
    'drop scroll in hole',
    'fweep me',
    'w','w','s','e',  # dorn falls
    'd','d','w','w','u','u','n','n','d','e',
    'fweep me',
    's','e','n','d','w','s','w','u','w',  # NOTE final 'w'!
    'wait','wait',
    'get all',
    's','s','e',
    'get scroll',
    'gnusto swanzo',
    'w','w','w',
    'search gnome',
    'w','w','sw','sw','s',
]
for c in s4_mid:
    send(c)
print('SCORE after Section 4:', score())

# ---- Section 5: Amusement Park ----
s5 = [
    'sw', 'w',
    'give zorkmid to gnome', 'give coin to gnome',
    'w', 'w', 's',
    'get ball',
    'open aqua vial', 'drink aqua potion',
    'throw ball at rabbit',
    'gnusto malyon',
    'n', 'e', 'e', 'ne',
]
for c in s5:
    send(c)
print('SCORE after Section 5:', score())

# ---- Section 6: Coal Mine ----
s6_pre = [
    's',
    'yonk malyon',
    'learn malyon',
    'malyon dragon',
    'sleep',
    's', 'e',
    'open orange vial', 'drink orange potion',
    'give spell book to older self',
    'give book to older self',
    'give book to twin',
]
for c in s6_pre:
    send(c)

# Parse combination (look for 3-4 digits in last 4KB)
logf.flush()
with open(LOG) as f:
    log = f.read()
tail = log[-4000:]
# Try to find combination in older-self/younger-self dialogue
combo_match = re.search(r'(?:combination|number)\D{0,30}?(\d{2,4})', tail, re.I)
if not combo_match:
    # try just any 2-4 digit num not equal to 860904 or year
    nums = re.findall(r'\b(\d{2,4})\b', tail)
    nums = [n for n in nums if n != '860904' and n != '400' and n != '1986']
    if nums: combo = nums[0]
    else: combo = '0'
else:
    combo = combo_match.group(1)
print('Combination:', combo)

s6_post = [
    'e',
    f'turn dial to {combo}',
    'open door',
    'e',
    'get rope', 'u',
    'nw', 'get timber', 'get beam',
    'nw', 'w',
    'put timber over chute', 'put beam over chute',
    'tie rope to timber', 'tie rope to beam',
    'drop rope in chute',
    'drop all',
    'climb down rope',
    'get scroll',
    'golmac me',
    'open lamp', 'get smelly scroll',
    'e',
    f'younger self, the combination is {combo}',
    f'say to younger self "the combination is {combo}"',
    f'tell younger self about {combo}',
    'd',
]
for c in s6_post:
    send(c)
print('SCORE after Section 6:', score())

# ---- Section 7: Belboz's Lair ----
s7 = [
    'gnusto vardik',
    'ne', 'wait', 'sleep',
    'learn vardik','learn meef','learn meef','learn swanzo',
    'drop all',
    's','d',
    'meef weeds',
    'get crate',
    'n','open crate',
    'wear suit',
    'get book',
    'n','meef vines',
    'w','w',
    'vardik me',
    'open white door',
    'swanzo belboz',
]
for c in s7:
    send(c)

print('FINAL SCORE:', score())
send('quit')
send('y')
logf.close()
