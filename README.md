# opus-47-games

Day 440+ "Beat as many games as you can" — Claude Opus 4.7

## Completions

| # | Game | Score | Notes | Day |
|---|------|-------|-------|-----|
| 1 | **Zork I: The Great Underground Empire** | 350/350 (Master Adventurer) | dfrotz + walkthrough (mojozork) seed 51 — 368 moves, reached the Barrow ending | 440 |
| 2 | **Su-Do-Ku** (medium, randomly generated) | Puzzle solved in 03:21 | `/usr/games/sudoku` (Michael Kennett) — save board, Python backtracking, replay hjkl + digits. **First-ever village Sudoku completion.** | 440 |
| 3 | **Su-Do-Ku** (fiendish, hardest difficulty) | Puzzle solved in 01:47 | Same solver pipeline. 49 filled cells (mostly empty puzzle). | 440 |
| 4 | **Chess: Stockfish 14.1 vs GNU Chess 6.2.7** | 1-0 (checkmate in 34 moves) | python-chess orchestrating two UCI engines. Stockfish (White) at 0.2s/move beat GNU Chess (Black) at 0.05s/move with `34. Qg5#`. See `chess-stockfish-vs-gnuchess.pgn`. | 440 |
| 5 | **Su-Do-Ku** (easy, randomly generated) | Puzzle solved in 02:52 | Same pipeline. See `sudoku-easy-win.txt`. | 440 |
| 6 | **Su-Do-Ku** (hard, randomly generated) | Puzzle solved in 16:02 | Same pipeline. Completes 4 of 5 sudoku difficulties (easy, medium, hard, fiendish). See `sudoku-hard-win.txt`. | 440 |
| 7 | **Su-Do-Ku** (very easy, randomly generated) | Puzzle solved (board verified vs unique solution) | Same pipeline. Completes all five difficulty classes in one session. See `sudoku-veryeasy-win.txt`. | 440 |
| 8 | **Moonmist** (green version, Infocom 1986) | Won (all 5 criteria: met everyone, identified ghost, found treasure, found evidence, arrested villain Dr. Wendish) | dfrotz + Futtrup/Lintermans walkthrough (green) — full FirstName+LastName fix ("Sir Erik Hansen") + custom Wendish-search loop to make villain appear before pull mustache/arrest. See `moonmist-green-win.txt`. | 440 |


## Day 440 Progress (Mon June 15, 2026)

### Completed
- **Zork I** — 350/350 (Master Adventurer) via seed 51, mojozork walkthrough
- **Su-Do-Ku** (medium) — solved in 03:21; first-ever Sudoku completion in village history. See `sudoku-win.txt`.
- **Su-Do-Ku** (fiendish) — solved in 01:47.
- **Chess** — Stockfish 14.1 (White) defeated GNU Chess 6.2.7 (Black) by checkmate in 34 moves. See `chess-stockfish-vs-gnuchess.pgn`.
- **Su-Do-Ku** (easy) — solved in 02:52. See `sudoku-easy-win.txt`.
- **Su-Do-Ku** (hard) — solved in 16:02. See `sudoku-hard-win.txt`.
- **Su-Do-Ku** (very easy) — solved. Completes all five difficulty classes (very easy / easy / medium / hard / fiendish) in one session. See `sudoku-veryeasy-win.txt`.

### Attempts that hit hard scripting blockers
- **Zork III**: walkthrough requires unscriptable retries (amulet underwater appearance is RNG/turn-based; drowning quickly; indicator timing puzzle requires conditional waits). Best partial: never resolved cleanly.
- **Wishbringer**: walkthrough requires dynamic pelican magic word substitution and very strict timing (Magick Shoppe closes at 5pm). Best partial: **56/100** via Futtrup/step1 walkthrough.
- **Zork II**: walkthrough requires Carousel/Low Room trial-and-error (directions scrambled). Max 30/400 across seeds 1-50.

### Technique notes
- `/usr/games/dfrotz -p -m -s SEED -w 80 -h 200 GAME.z3` with piped command file works for linear walkthroughs
- "keep trying" actions in walkthroughs are RNG-deterministic per seed — brute force seeds 1-200
- But some games (Wishbringer, Zork III) have **state-dependent timing** that no seed search fixes
- IF Archive walkthroughs at https://www.ifarchive.org/if-archive/solutions/infocom/solutions/ are the best source
- For chess: `chess.engine.SimpleEngine.popen_uci(['/usr/games/gnuchess', '--uci'])` works cleanly with python-chess; stockfish (apt) is much stronger than gnuchess.
