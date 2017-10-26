"""
This module contains only the class for characters
"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Character:
    """
    Represents a character of the game.
    """

    def __init__(self, name, life_points, power_points):
        """
        constructor takes by parameters:
        - name
        - life points
        - power points
        to represents the character
        """
        self.name = name
        self.life_points = life_points
        self.power_points = power_points

    def __repr__(self):
        """
        this method allows to represent the class by string in the interpreter
        """
        return "Character: name({}), life points({}), power points({})".format(
            self.name, self.life_points, self.power_points)

    def __delattr__(self, name_attibute):
        """
        Throws an exception in case th user tries to delete the name attribute
        """
        raise AttributeError("You can't delete any attribute")
