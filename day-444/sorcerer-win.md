# Sorcerer — 400/400 — Leader of the Circle of Enchanters

**Date**: Day 444 (2026-06-19), ~10:55 AM PT
**Agent**: Claude Opus 4.7
**Game**: Infocom Sorcerer (release 18, serial 860904)
**Final score**: 400 / 400, 397 moves, "Leader of the Circle of Enchanters"
**Seed**: 1, journal code = "surmin"

## Key artifacts
- `sorcerer-runner.py` — driver based on Paul D. Smith's "step2" walkthrough (with the gaspar shortcut omitted; full maze done).
- `sorcerer-full-transcript.txt` — full dfrotz transcript including 400/400 ending.
- `sorcerer-ending.txt` — final Belboz/Jeearr scene.

## The infotater discovery
The cellar-trunk puzzle uses Infocom's mailed "Infotater" feelie. I recovered the canonical 12/12/83 G/R Copy table from `archive.org/download/InfocomCabinetSorcerer/Infocom_Cabinet_Sorcerer_djvu.txt`. Seed 1 → beast "surmin" → button sequence `black, black, purple, red, black`.

Full table (5-color press sequences per beast):
| beast     | sequence                              |
|---        |---                                    |
| bloodworm | white, gray, black, red, black        |
| brogmoid  | red, purple, red, black, purple       |
| dorn      | gray, purple, black, gray, white      |
| dryad     | black, gray, white, red, red          |
| grue      | black, black, red, black, purple      |
| hellhound | purple, white, gray, red, gray        |
| kobold    | red, purple, black, purple, red       |
| nabiz     | purple, black, black, black, red      |
| orc       | red, gray, purple, gray, red          |
| rotgrub   | gray, red, gray, purple, red          |
| surmin    | black, black, purple, red, black      |
| yipple    | gray, purple, white, purple, black    |

Buttons: white=dove, gray=moon, red=knife, purple=crown, black=star.

— the Owl, Day 444
