#!/usr/bin/python
# -*- coding:utf8 -*

""" A class to study properties and Python conventions
"""

class Person:
    """Classe specifying a person with :
    - a name ;
    - a first name ;
    - an age ;
    - an address """

    
    def __init__(self, name, firstname):
        """ Constructeur de notre classe """
        self.name = name
        self.firstname = firstname
        self.age = 33
        self._address = "Paris" # _address is private by convention
        
    def _get_address(self): 
    """
        Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut 'address'"""
        print("Accessing to address !")
        return self._address
    
    def _set_address(self, new_address):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
                self.firstname, new_address))
        self._address = new_address
    # On va dire à Python que notre attribut address pointe vers une
    # propriété
    address = property(_get_address, _set_address)
