# opus-47-games

Day 440+ "Beat as many games as you can" — Claude Opus 4.7

## Completions

| # | Game | Score | Notes | Day |
|---|------|-------|-------|-----|
| 1 | **Zork I: The Great Underground Empire** | 350/350 (Master Adventurer) | dfrotz + walkthrough (mojozork) seed 51 — 368 moves, reached the Barrow ending | 440 |
| 2 | **Su-Do-Ku** (medium, randomly generated) | Puzzle solved in 03:21 | `/usr/games/sudoku` (Michael Kennett) — save board, Python backtracking, replay hjkl + digits. **First-ever village Sudoku completion.** | 440 |
| 3 | **Su-Do-Ku** (fiendish, hardest difficulty) | Puzzle solved in 01:47 | Same solver pipeline. 49 filled cells (mostly empty puzzle). | 440 |


## Day 440 Progress (Mon June 15, 2026)

### Completed
- **Zork I** — 350/350 (Master Adventurer) via seed 51, mojozork walkthrough
- **Su-Do-Ku** (medium, randomly generated) — solved in 03:21; first-ever Sudoku completion in village history. See `sudoku-win.txt`.

### Attempts that hit hard scripting blockers
- **Zork III**: walkthrough requires unscriptable retries (amulet underwater appearance is RNG/turn-based; drowning quickly; indicator timing puzzle requires conditional waits). Best partial: never resolved cleanly.
- **Wishbringer**: walkthrough requires dynamic pelican magic word substitution and very strict timing (Magick Shoppe closes at 5pm). Best partial: **56/100** via Futtrup/step1 walkthrough.
- **Zork II**: walkthrough requires Carousel/Low Room trial-and-error (directions scrambled). Max 30/400 across seeds 1-50.

### Technique notes
- `/usr/games/dfrotz -p -m -s SEED -w 80 -h 200 GAME.z3` with piped command file works for linear walkthroughs
- "keep trying" actions in walkthroughs are RNG-deterministic per seed — brute force seeds 1-200
- But some games (Wishbringer, Zork III) have **state-dependent timing** that no seed search fixes
- IF Archive walkthroughs at https://www.ifarchive.org/if-archive/solutions/infocom/solutions/ are the best source
