#!/usr/bin/python
# -*- coding:utf-8 -*

"""
  Exercise OC TP1
  
  * the computer select a word (8 char max)
  * the player can guess letters 
  * score = remaining attempts to guess the word (out of 8)
  * computes and record player score

The program is a finite state machine

@startuml

[*] --> waitForPlayer
waitForPlayer --> [*] : quit

waitForPlayer : What is your name?

waitForPlayer -down-> GameInProgress : name
waitForPlayer -up-> waitForPlayer : inccorectName

GameInProgress --> GameInProgress : letter
GameInProgress --> waitForPlayer : 8th

@enduml

Classes and responsibilities

UserInterface: Get user inputs, display status
GameEngine: Manages the game states.

@startuml

Title: Title

class GameEngine{
    string input(string) : returns a string to display
    boolean gameCompleted()
}
note right : This is a note

UserInterface "1" --> "1" GameEngine : triggers

@enduml

"""

# Python libraries

# Project libraries
# first form gives access and requires fully specified names 
# import hangman.config
# second form gives access and allows short names
from hangman.config import *
from hangman.dictionary import *
from hangman.game_engine import GameEngine
    
def help():
    """ Lists supported commands """

    hlp = """Small command interpretor
    command:
        help : print this
        quit : exit the interpretor
    """
    print (hlp)
    
def interpretor():
    """ The interpretor event loop """
    
    ge = GameEngine()
        
    while True:
        try:
            line = input(ge.prompt())
            print (line)
            if (line == "quit"):
                break
            elif (line == "help"):
                help()
            else:
                # process an input according to the state
                result = ge.input(line)
                if (result != ""):
                    print(result)
                            
        except Exception as e:
            print ("User exception caught")
            print (e)
            # all
    
interpretor()

print ("bye")
