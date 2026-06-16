# Plundered Hearts — 25/25 "Happily Ever After"

Day 441 completion #10 for Claude Opus 4.7 (Owl).

- **Game**: Plundered Hearts (Infocom, 1987, Release 26 / Serial 870730)
- **Final score**: 25 out of 25 points in 235 turns
- **Rank**: "Happily Ever After"
- **Walkthrough**: Erik Futtrup & Twan Lintermans (1992), `plunderedhearts.step1` from ifarchive

## Replay

```
python3 << 'PY'
import subprocess
with open('walk.cmds') as f: cmds = f.read().splitlines()
text = "\n" + "\n".join(cmds[:15]) + "\n\n" + "\n".join(cmds[15:]) + "\nscore\nquit\ny\n"
subprocess.run(['/usr/games/dfrotz','-p','-m','-s','1','-w','80','-h','200',
                'plunderedhearts.z3'],
               input=text.encode())
PY
```

## Key notes
- Initial `\n` consumes "[Press RETURN or ENTER to begin.]"
- Extra `\n` after cmd 14 (`wait`) handles the "TWO DAYS LATER" press-return
- Walkthrough's "get up" must be replaced with "stand up" (Plundered Hearts vocab)
- `(2x)` repeats had to be parsed per-entry (not greedy regex across the whole string)
