#!/usr/bin/python
# -*- coding:utf8 -*

print "First objects"

class Person:
    """
    This class handle a person
    """
    nb = 0
    
    # There is no private attribute in Python, the convention is to prefix them by an underscore
    
    # You cannot have attributes and methods with the same name.
    
    def __init__(self, name, firstname = "John", age = 33):
        """ Constructor """
        self._name = name
        self._firstname = firstname
        self._age = age
        Person.nb += 1
        
    def familly_name(self):
        return self._name
    
    def age(self):
        return self._age
    
    def __del__(self):
        """ Destructor """
        print "destructor:", vars(self)

p = Person('Doe', age = 25)

p2 = Person("Smith")

p = Person('Dalton', age = 60)

print "We have ", Person.nb, " persons"

# direct access to attributes
print "p.name = ", p._name

# to dump all attributes
print vars(p)

print p.familly_name(), p.age()

# but no accessor per default
try:
    # print p.name()
    pass
except Exception as e:
    print "Exception raised: ", e
    
print "dir(p) = ", dir(p)


print "bye"

