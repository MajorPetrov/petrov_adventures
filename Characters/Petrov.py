"""
This module contains only the class for the major Petrov
"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from .character.character import Character

class Petrov(Character):
    """
    Represents the main character (the major Petrov) of the game.
    """

    def __init__(self):
        Character.__init__(self, "Major Petrov", 10, 10)
        self.number_victims = 0

    def __del__(self):
        print("Game Over")
