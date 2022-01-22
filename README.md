## Instructions

Run the following in the command line python environment
```python
>> python
from main import *
guess = WordPartition("raise")
```

Then in Wordle guess "raise" and record the resulting color tiles. In this example lets say the "A" is green and the "E" is yellow.

```python
solutionSet = guess.partitions["bgbby"]
guess = iterate(solutionSet)
print(solutionSet)
print(guess.word)
```

This will then give you the next word to guess and the list of possible solutions. Note that it is not always best to guess a word from the set of possible solutions. Then repeate the step above till you get the solution

```python
solutionSet = guess.partitions["bgbby"]
guess = iterate(solutionSet)
print(solutionSet)
print(guess.word)
```

## Premise
The idea is to take the set of possible solutions and through guessing reduce the set as much as possible. I've taken the approach of choosing guesses based off the worst possible outcome of the guess. For example if you guess the word "raise", the most likely outcome is no letters match the solution and you recieve all black tiles ("bbbbb"). In this scenario we've reduced the solution set down to 168 possible words.