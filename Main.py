#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:17:25 2020

@author: danielshapiro
"""


#MAKE MORE FUNCTIONS.  DONT FORGET THIS PART, ITS IMPORTANT
import random
import pandas
import time

def main():
    Categories,Questions = CSV_Read_Pandas(QUESTION FILE) #csv filename
    Categories,Answers = CSV_Read_Pandas(ANSWER FILE) #csv filename
    
    numPlayers = Get_Num_Players() #gets number of players
    
    players = Create_Players(numPlayers) #List of players
    
    while not Game_Over:
        whose_turn = random.randint(1,numPlayers) #move random whoseturn outside, 
                #then turn is to answerer
        print('Player',whose_turn,', roll the dice.')
        
        #DETERMINE COLOR FUNCTION GOES HERE, but for now...
        random_category_number = random.randint(0,5)
        current_category = Categories[random_category_number]
        print('The category is',current_category,'.')
        
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        
        #CHECK IF QUESTION IS UNANSWERED
        random_question_number = random.randint(0,9)
        current_question = Questions[current_category][random_question_number]
        print(current_question)
        
        user_answer = input('Enter your answer here: ')
        if user_answer == Answers[current_category][random_question_number]:
            print('Correct')
            players[whose_turn][1][current_category] = 1
            players[whose_turn][0] += 1
        else: #ALL THIS NEEDS TO CHANGE WHEN WE GET BUZZERS
            print('That is incorrect. All players may now buzz in to answer the question')
            time.sleep(1)
            print(3)
            time.sleep(1)
            print(2)
            time.sleep(1)
            print(1)
            time.sleep(1)
            new_current_player = players[0]
            print(current_question)
            whose_turn = new_current_player
            user_answer = input('Player 1, enter your answer here: ')
            if user_answer == Answers[current_category][random_question_number]:
                print('Correct')
                players[whose_turn][1][current_category] = 1
                players[whose_turn][0] += 1

            
        Game_Over = check_Game_Over(whose_turn)
            
        










def CSV_Read_Pandas(filename):
    data = pandas.read_csv(filename) #Reads csv into python, data type is dataframe
    Column_Headers=[] #creates empty list for column headers
        #Column headers will be the categories
    columns = [] #creates empty list for the columns of array
        #Columns are either questions or answers
    for col in data.columns:
        Column_Headers.append(col) #Creates list of column headers
    for header in Column_Headers:
        whole_column_raw = data[[header]]
        whole_column = whole_column_raw.to_numpy().tolist()
        column = []
        for element in whole_column:
            string_element = str(element[0])
            column.append(string_element)
        columns.append(column)
    return(Column_Headers,columns)

def Get_Num_Players():
    numPlayers = float(input('How many players are there? Enter 2,3, or 4: '))
    if ((numPlayers == 2) or (numPlayers == 3) or (numPlayers == 4)):
        return(numPlayers)
    else:
        print('Sorry, only 2,3, or 4 players may play this game.')
        return(Get_Num_Players())

def Create_Players(numPlayers):
    player1categories = [0,0,0,0,0,0]
    player1correct = 0
    player1 = [player1correct,player1categories]
    player2categories = [0,0,0,0,0,0]
    player2correct = 0
    player2 = [player2correct,player2categories]
    if numPlayers == 3:
        player3categories = [0,0,0,0,0,0]
        player3correct = 0
        player3 = [player3correct,player3categories]
        return([player1,player2,player3])
    elif numPlayers == 4:
        player3categories = [0,0,0,0,0,0]
        player3correct = 0
        player3 = [player3correct,player3categories]
        player4categories = [0,0,0,0,0,0]
        player4correct = 0
        player4 = [player4correct,player4categories]
        return([player1,player2,player3,player4])
    else:
        return([player1,player2])

def check_Game_Over(whose_turn):
    if sum(players[whose_turn][1]) == 6:
        print('Player',whose_turn,'wins!')
        return(True)
    elif #if one category has no questions left
        #player with most points wins (use max function)
        return(True)
    else:
        return(False)