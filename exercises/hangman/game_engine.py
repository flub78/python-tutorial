#!/usr/bin/python
# -*- coding:utf8 -*

""" Hangman game engine

    manages the game SMA    
"""
from enum import Enum
from random import randrange
from hangman.dictionary import *
from hangman.config import *

class GameStates(Enum):
    ASK_NAME = 1
    GAME = 2

def validName(name):
    """
    Checks if a string is a valid player name
    """
    return name.isalnum()

class GameEngine:
    """
    The game engine
        - validates entries
        - manages the game state
        - keep the scores
        - determine if the game is completed
    """

    def __init__(self):
        """ Constructor """
        self._state = GameStates.ASK_NAME

    def _startNewGame(self):
        """
        Initialize engine for a new game
        """
        self._state = GameStates.GAME
        nb = len(words) # number of words in the dictionary
        self._wordToGuess = words[randrange(0, nb)]
        self._guessedLetters = set()
        self._remainingAttempts = attempts

    def _guessedPart(self):
        """
        Returns the word to guess with the already guessed letters in clear
        and a star for the others
        """
        result = list(self._wordToGuess)
        cnt = 0
        for c in result:
            if (not c in self._guessedLetters):
                result[cnt] = '*'
            cnt += 1
        return "".join(result)
        
    def input(self, charStr):
        """ Get a player input and returns a string to display
        """
        if (self._state == GameStates.ASK_NAME):
            if (validName(charStr)):
                self.playerName = charStr
                self._startNewGame()
            else:
                return charStr + " is not a valid name"
            
        elif (self._state == GameStates.GAME):
            # No thorough check of the input. As this program is an exercise...
            letter = charStr[0]
            self._remainingAttempts -= 1 
            if (self._remainingAttempts < 1):
                self._state = GameStates.ASK_NAME
                return "Game over"
            if (letter in self._wordToGuess):
                self._guessedLetters.add(letter)
            if (self._guessedPart() == self._wordToGuess):
                self._state = GameStates.ASK_NAME
                return "You won."
        
        return charStr
    
    def prompt(self):
        """
        Define the prompt according to the state
        """
        if (self._state == GameStates.ASK_NAME):
            return ">: what is your name? "
        elif (self._state == GameStates.GAME):
#                + self._wordToGuess + " "  \
            return "remaining: " + str(self._remainingAttempts) \
                + " >: type a letter " \
                + self._guessedPart() + " "
        return ">: "
            