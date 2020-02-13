#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:55:46 2020

@author: danielshapiro
"""

# This function MUST be called AFTER asking for how many players.
# The number of players will be an input to this function

# This function will generate a random player to be the one to roll the dice
# We need to pair this with a function to move the motor when we get it

import random #DONT FORGET TO IMPORT RANDOM
def random_Choose_to_Roll(num_Players):
    ran = random.randint(1,num_Players)
    #ADD SOMETHING TO MOVE THE MOTOR
    return(ran)