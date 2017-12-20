#!/usr/bin/python
# -*- coding:utf8 -*

"""
  Exercise OC TP1
  
  * the computer select a word (8 char max)
  * the player can guess letters 
  * score = remaining attempts to guess the word (out of 8)
  * computes and record player score
  
@startuml

[*] --> AskName
AskName --> [*]

AskName : What is your name?

AskName -> Game : name
Game --> [*]

Game --> Attempts : start
Attempts --> Game : 8th
Attempts --> Attempts : letter
Attempts --> [*]

@enduml

"""

# Python libraries
from random import randrange
from enum import Enum

# Project libraries
# first form gives access and requires fully specified names 
import hangman.config
# second form gives access and allows short names
from hangman.config import *
from hangman.dictionary import *

# print "hangman.config.attempts = ", hangman.config.attempts
# print "attempts = ", attempts

# print "list in order"
# i = 0
# for w in words:
#     print "words[", i, "]", w
#     i += 1
    
nb = len(words)
print "number of words = ", nb

# generate a random number and display the word
print "words out of order"
for x in range(0, nb):
    rd = randrange(0, nb)
    print "\t-> ", words[x], " : ", rd, words[rd]

def help():
    """ Lists supported commands """

    hlp = """Small command interpretor
    command:
        help : print this
        quit : exit the interpretor
    """
    print hlp

class States(Enum):
    ASK_NAME = 1
    GAME = 2
    ATTEMPTS = 3
    
def interpretor():
    """ The interpretor event loop """
    
    state = States.ASK_NAME
    
    try:
        while True:
            line = raw_input(">: ")
            print line
            if (line == "quit"):
                break
            elif (line == "help"):
                help()
            state = States.GAME
            state = States.UNKNOW
            
    except:
        all
    
interpretor()

print "bye"

