import re, sys
with open('/tmp/walks/moonmist.yellow.txt') as f:
    txt = f.read()
# Body between first newline and (c) 
body = txt.split('\n', 1)[1].split('(c) 1992')[0]

def fix_wait(m):
    inner = m.group(1).strip().lower()
    m2 = re.search(r'(?:until|till)\s+(.+)', inner)
    if m2:
        t = m2.group(1).strip()
        t = t.replace(':', '@')
        return f"wait until {t}"
    return 'wait'

body = re.sub(r'wait\s*\{([^{}]*)\}', fix_wait, body, flags=re.IGNORECASE)
# Strip other {curly}
body = re.sub(r'\{[^{}]*\}', '', body, flags=re.DOTALL)
body = re.sub(r'\s+', ' ', body).strip()
cmds = [c.strip().replace('@', ':') for c in body.split(':') if c.strip()]
# Post-process: Sir Erik -> Sir Erik Hansen (might need)
out = []
for c in cmds:
    if c == 'Sir Erik':
        c = 'Sir Erik Hansen'
    out.append(c)
with open('walk.cmds', 'w') as f:
    for c in out:
        f.write(c + '\n')
print(f"Total cmds: {len(out)}")
for c in out: print(c)
