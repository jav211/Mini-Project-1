#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:57:14 2020

@author: danielshapiro
"""

def Get_Num_Players():
    numPlayers = float(input('How many players are there? Enter 2,3, or 4: '))
    if ((numPlayers == 2) or (numPlayers == 3) or (numPlayers == 4)):
        return(numPlayers)
    else:
        print('Sorry, only 2,3, or 4 players may play this game.')
        return(Get_Num_Players())
        
Get_Num_Players()