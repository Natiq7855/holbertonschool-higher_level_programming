#!/usr/bin/python3
from abc import ABC
"""first task of abc abstarct class"""


class Animal(ABC):
    """Aimal class"""

    @abstractmethod
    def sound(self):
        """sound function"""

        pass

class Dog(Animal):
    """dog fuction"""

    def sound(self):
        return "Bark"

class Cat(Animal):
    """cat fuction"""
    
    def sound(self):
        return "Meow"
