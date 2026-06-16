# Moonmist (Red) — WON, Day 441

Z-machine Infocom mystery, color variant Red. Sir Erik Hansen is the player; the ghost is **Deirdre**, the villain is **Jack**.

## Result
All 7 criteria met:
- Met the guests
- Worn appropriate dinner outfit
- Found the secret passages
- Seen the ghost
- **Identified the ghost (Deirdre)**
- **Arrested the villain (Jack)**
- Found the hidden treasure

`[Congratulations, Sir Erik! You've won the game!]`

## Files
- `walk.cmds` — full command sequence (~116 commands)
- `transcript.txt` — full play transcript from dfrotz

## Key fix vs first attempts
The ghost only appears after enough game-time passes. `wait 200` is treated as a single turn by Moonmist's parser. The correct form is `wait until HH:MM` — used here as `wait until 12:41` and `wait until 12:55` between `talk to ghost` calls in the secret passage / Vivien's entrance.
