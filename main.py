from solutions import solutions
from validGuesses import guesses
import statistics

# Class which stores information about a particular word
class WordPartition:

    # The word in question
    word = ""

    # A dictionary where the keys are the possible color tile combinations and the values
    # are all words in the solution set that would give you that color combination if it was 
    # the solution and word was the guess.

    # Eg if word is mince then at key "bgggg" you would find mince and since
    partitions = dict()

    def __init__(self, word, solutionSet=solutions):
        self.word = word
        self.partitions = dict()
        self.populateSolutionSet(solutionSet)

    def populateSolutionSet(self, solutionSet):
        for solution in solutionSet:
            coloring = computeGuessColoring(self.word, solution)
            if coloring not in self.partitions:
                self.partitions[coloring] = set()
            self.partitions[coloring].add(solution)
    
    def calculateOptimalityStat(self, debug=False):
        lengths = []
        for coloring in self.partitions:
            lengths.append(len(self.partitions[coloring]))
        val = max(lengths)
        if (debug):
            print(self.word + ": " + str(lengths) + " " + str(val))
        return val

    # Helper function to print out stats of a word
    def getStats(self):
        mostComonColoring = max(self.partitions, key= lambda x: len(self.partitions[x]))
        optimalityStat = self.calculateOptimalityStat()
        print(self.word + ": " + mostComonColoring + ": " + str(optimalityStat))

# Given a guess and a solution, computes the resulting coloring
# computeGuessColoring("mince", "wince") -> "bgggg"
def computeGuessColoring(guess, solution):
    coloring = ""
    for index in range(len(guess)):
        if guess[index] == solution[index]:
            coloring += "g"
        elif guess[index] in solution:
            coloring += "y"
        else:
            coloring += "b"
    return coloring

# Given a set of solutions calculate the optimal guess
def iterate(solutionSet):
    if len(solutionSet) == 1:
        return list(solutionSet)[0]
    wordPartition = WordPartition("aahed", solutionSet)
    bestGuess = wordPartition
    minStat = wordPartition.calculateOptimalityStat()
    for word in solutionSet:
        wordPartition = WordPartition(word, solutionSet)
        stat = wordPartition.calculateOptimalityStat()

        if stat < minStat:
            bestGuess = wordPartition
            minStat = stat
            print("new word "  + word + " " + str(minStat))

    for word in guesses:
        wordPartition = WordPartition(word, solutionSet)
        stat = wordPartition.calculateOptimalityStat()

        if stat < minStat:
            bestGuess = wordPartition
            minStat = stat
            print("new word "  + word + " " + str(minStat))
    return bestGuess

