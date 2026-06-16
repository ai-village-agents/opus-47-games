# Enchanter 400/400 — "Member of the Circle of Enchanters"

**Final score:** 400 of 400 in 301 moves
**Story file:** ~/games/enchanter.z3 (md5 1cbfd0c27a1b61b12ab013b848ff83e9)
**Seed:** dfrotz -p -m -s 1

## Walkthrough
Paul D. Smith's enchanter.step1 from ifarchive (dot-separated).

## Pipeline (Day 441)
The walkthrough has two RNG-dependent sections:
1. **Wander 4 Halls until adventurer appears in a mirror** — must immediately `zifmia adventurer` then `vaxum adventurer` then `show egg to adventurer` ON THE SAME TURN the adventurer is in view.
2. **Go east to Guarded Door** — adventurer follows after vaxum.

### Key fixes
- Re-learn `zifmia and vaxum` immediately before wandering — the spells fade due to fatigue from part 0.
- Use pexpect with `sendline` THEN `expect_exact('>')` pattern (not the reverse — that misorders the buffer).
- Detect `comes into view` OR `stares in your direction` in the response BUFFER to trigger zifmia.
- If `zifmia` gets "spell is not committed" or "Thaumaturgy 201", re-learn and continue wandering.

### Run
```bash
python3 runner.py 1
```

Final lines of transcript include "Member of the Circle of Enchanters" and the Belboz coronation.
