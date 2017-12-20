#!/usr/bin/python
# -*- coding:utf-8 -*

print ("First objects")

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
        print ("destructor:", vars(self))
        
    def __repr__(self):
        return ("Person => name: {}, firstname: {}, age: {}".format(self._name, self._firstname, self._age))
    
class Agent(Person):
    
    def __init__(self, name, id, firstname = "John", age = 33):
        self._id = id
        Person.__init__(self, name, firstname, age)

    def id(self):
        return self._id
        
p = Agent ('Bond', 'James', age = 40)
print ("We have ", Person.nb, " persons")

# to dump all attributes
print (vars(p))

assert(issubclass(Agent, Person))
assert(isinstance(p, (Agent, Person)))

print ("bye")

