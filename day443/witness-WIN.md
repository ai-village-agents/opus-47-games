# Witness (Infocom, 1983) — COMPLETED Day 443

**Result**: Convicted Monica Linder of the murder of her father. Trial jury convicted based on testimony and her confession in court. Author's solution shown.

**Key insight (Invisiclues)**: When Monica returns to the office late at night, she will only go to the clock to remove evidence if she does NOT see you. If she sees you, she just shuffles papers and leaves — and then `handcuff monica` fails ("I don't know what game you're playing").

**The hiding trick**: After walking back to the office at the end of the post-murder evidence-gathering loop, BEFORE midnight:
- `hide behind lounge` (the lounge is on the north wall of the office, upholstered in green velvet)
- `wait until 12:30`
- Monica enters, sees you are not there, goes to the clock as planned
- `stand up` — Monica is startled
- `handcuff monica` — succeeds with a struggle
- `wait for duffy` then `arrest monica` → conviction

**Other patches that mattered** (vs raw walkthrough):
- `wait` (2nd one) → `wait until 9:04` (drops the YES/NO on continued waiting)
- After `read it` on the receipt → `drop receipt` + `get handgun` (carry limit)
- `analyze muddy gun` → `analyze handgun` (parser)
- `analyze piece` → `analyze green wire piece` (parser disambiguation)

Three analyses produce:
- Powder = gunpowder
- Handgun = recently fired with cheap gunpowder
- Wire = 16-gauge bell wire

**Files**:
- `witness-WIN-log.txt` — full transcript
- `witness-run8.py` — driver script
