#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:28:10 2020

@author: danielshapiro
"""

def Create_Players(numPlayers):
    player1score = [0,0,0,0,0,0]
    player2score = [0,0,0,0,0,0]
    if numPlayers == 3:
        player3score = [0,0,0,0,0,0]
        return(player1score,player2score,player3score)
    elif numPlayers == 4:
        player3score = [0,0,0,0,0,0]
        player4score = [0,0,0,0,0,0]
        return(player1score,player2score,player3score,player4score)
    else:
        return(player1score,player2score)
        
    