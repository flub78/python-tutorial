#!/usr/bin/python
# -*- coding:utf8 -*

"""
Unit tests for hangman game engine

execution:
    python test_game_engine.py
    or
    python -m unittest discover
"""


from hangman.dictionary import *
from hangman.game_engine import GameEngine
from hangman.game_engine import validName
import unittest

class GameEngineTest(unittest.TestCase):
    """ Test case for game engine """

    def test_basic(self):
        ge = GameEngine()
        self.assertTrue(ge, "Game engine instance created")
        
    def test_validName(self):
        self.assertTrue(validName("Fred"), "Fred is a valid name")        
        self.assertTrue(validName("Player1"), "Player1 is a valid name")        
        self.assertTrue(not validName("&é'(-è_')"), "unvalid name")        

    def test_prompt(self):
        ge = GameEngine()
        prompt = ge.prompt()
        self.assertEqual(prompt, ">: what is your name? ", "prompt after init == " + prompt)        

    def test_guessedPart(self):
        # The python community considers that private functions unit test should be covered
        # by public entries unit tests.
        # 
        # In this case, due to the random part in the game, not having any view or control 
        # on the internal of the object makes the tests more complicated.
        #
        # Remark: not unit testing private functions, prevent to check their robustness
        # and unit testing is by definition a white box approach as you need access to the class
        # organization that a regular user has not. So it is taking the risk to accumulate
        # potentially a lot of code that will only wait for a slight reorganization before to break.
        #
        # Note that there is also an efficiency consideration. By using only public entries
        # to trigger private method, it can be cumbersome.
        #
        # https://docs.python.org/3/library/unittest.mock.html
        ge = GameEngine()
        ge.input("Player1")
        guessed = ge._guessedPart()
        expected = '*' * len(ge._wordToGuess)
        self.assertEqual(guessed, expected, "guessed after init == " + guessed)        

if __name__ == '__main__':        
    unittest.main()


