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
        
    def _get_surface(self):
        print "======> private"
        # raise Exception ("Private attribute")

    # properties can be used to create special attributes
    # and activate associated function on
    # reading, writing, deleting and printing help
    # but they cannot have the name of an existing attribute, so cannot be used to enforce a real private property on an existing attribute
    _display = property(_get_surface)
        
classroom = Whiteboard()
classroom.write("Hello")
classroom.write("World")
print classroom.display()

classroom.erase()
classroom.write("Hello World")
print classroom.display()

print classroom._display

print "bye"

