"""
Main module for the game The major Petrov against cosmopolitans
main algorithm for the run the game is implemented here
"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from characters.Character import Character
from characters.Petrov import Petrov
#from items.Rifle import Rifle

if __name__ == "__main__":
    MAJOR = Petrov()
    ENNEMI = Character("a vegan", 10, 10)
    MAJOR.attack(ENNEMI)

    if ENNEMI.life_points == 0:
        del ENNEMI

# At the end of the script, the shell shows "Game Over" which is in the __del__
# function of Petrov...