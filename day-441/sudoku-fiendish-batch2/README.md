# 5 Sudoku Fiendish — Batch 2

```bash
for i in 1 2 3 4 5; do
  /usr/games/sudoku -g1 -cfiendish > board_$i.txt
  /usr/games/sudoku -v board_$i.txt > solved_$i.txt
done
```

Each solved file begins:
`Solution(s) to 'randomly generated - fiendish' [fiendish]`
