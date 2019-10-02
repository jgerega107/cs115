'''
Created on 9/18/19 
@author:   Jacob Gerega
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 2
'''
import sys

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

#helper functions

#canStringBeMade: takes in a string and a list of letters, outputs a boolean on whether said string can be created from the list of characters
def canStringBeMade(S, letters):
  if S != "" and letters == []:
    return False
  elif S == "" or letters == []:
    return True
  else:
    if S[0] in letters:
      return True and canStringBeMade(S[1:], removeInstanceOfChar(S[0], letters))
    else:
        return False

#removeInstanceOfChar: takes in a single letter as a string and a list of letters, outputs the said list but with only one instance of S removed
def removeInstanceOfChar(S, letters):
  if letters == []:
    return []
  elif S == letters[0]:
    return letters[1:]
  else:
    return [letters[0]] + removeInstanceOfChar(S, letters[1:])

#listOfPossibleStringsWithScores: takes in a list of words(dictionary) and a list of letters, outputs all possible words that can be created along with their respective scrabble scores
def listOfPossibleStringsWithScores(dict, letters):
  if dict == []:
    return []
  else:
    if canStringBeMade(dict[0], letters):
      return [[dict[0], wordScore(dict[0], scrabbleScores)]] + listOfPossibleStringsWithScores(dict[1:], letters)
    else:
      return listOfPossibleStringsWithScores(dict[1:], letters)

#findGreatestWord: takes in a score and a list of words, outputs pair of greatest word with greatest score
def findGreatestWord(score, words):
  if words == []:
    return []
  elif words[0][1] == score:
      return words[0]
  else:
      return findGreatestWord(score, words[1:])

#findGreatestScore: takes in a list of words and finds the greatest score (not the word itself though)
def findGreatestScore(words):
  if words == []:
    return 0
  else:
    maxVal = max(words[0][1], findGreatestScore(words[1:]))
    return maxVal


#hw functions

#letterScore: takes in a letter and a list, retuns score of said letter
def letterScore(letter, scoreList):
  if letter == scoreList[0][0]:
    return scoreList[0][1]
  else:
    return letterScore(letter, scoreList[1:])

#wordScore: takes in a string and a list of scores, outputs score of word
def wordScore(S, scoreList):
  if S == "" or scoreList == []:
    return 0
  else:
    return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

#scoreList: takes in a list of letters and returns all possible word combinations with respective scores
def scoreList(Rack):
  return listOfPossibleStringsWithScores(Dictionary, Rack)

#bestWord: takes in a list of letters and returns the greatest word with its respective score
def bestWord(Rack):
  listOfWords = listOfPossibleStringsWithScores(Dictionary, Rack)
  maxVal = findGreatestScore(listOfWords)
  if maxVal == 0:
    return ['', 0]
  else:
    return findGreatestWord(maxVal, listOfWords)
