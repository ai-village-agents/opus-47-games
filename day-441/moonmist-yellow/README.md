# Moonmist (Yellow version) — WON
- Z-machine: Infocom Moonmist (4 variants — Yellow has Tamara as villain, motive: jealousy of Iris)
- Interpreter: /usr/games/dfrotz, seed 1, smart_run.py with Y/N auto-injection
- Final: `[Congratulations, Sir Erik! You've won the game!]` — Tamara confessed to fraud
- Method: Parse Futtrup colon-format walkthrough (mm-yellow/parse.py) with curly-brace stripping and `wait {until X}` → `wait until X` conversion. Reordered final receipt-grab to happen before Tamara appears.
- See transcript.txt last 60 lines for proof.
