#!/usr/bin/python
# -*- coding:utf8 -*

print "Object management"

class Whiteboard:
    """
    A whiteboard simulator"""
    
    def __init__(self):
        self._surface = ""
        
    def write(self, str):
        if self._surface != "":
            self._surface += "\n"
        self._surface += str
    
    def display(self):
        return self._surface
    
    def erase(self):
        self._surface = ""
        
classroom = Whiteboard()
classroom.write("Hello")
classroom.write("World")
print classroom.display()

classroom.erase()
classroom.write("Hello World")
print classroom.display()

print "bye"

