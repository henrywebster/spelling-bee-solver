# spelling-bee-solver
Solves the Spelling Bee Game

Word list provided in the repo courtsey [here](https://github.com/dwyl/english-words).

The English word data set is... promiscuous. Because of that, not every result is guaranteed to be recognized as a word even if the rules pass. I suggest spot-checking for recognizable ones before going for the more esoteric.

# Usage
```bash
python solver.py --center o --outer egyhmn
```

## Parameters
* *center* - the center letter of the puzzle
* *outer* - the six outer letters of the puzzle
* *file* (optional) - an alternative file of line-separated words to the one provided in the repo
