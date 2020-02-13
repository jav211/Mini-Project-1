#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:53:41 2020

@author: burcukose
"""
from random import randint
import pandas as pd

df = pd.read_csv('qbank.csv')

food_bank = df[df['category'] == 'food']
rutgers_bank = df[df['category'] == 'rutgers']

def determine_color():
    my_rand = randint(1,2)
    if my_rand == 1:
        color = 'blue'
    else:
        color = 'red'
    return color

def determine_category(color):
    if color == 'blue':
        category = 'food'
    else:
        category = 'rutgers'
    return category

def get_correct_bank(category,food_bank,rutgers_bank):
    if category == 'food':
        #THEN RANDOMLY PICK QUESTION FROM FOOD_BANK
        return food_bank
    else:
        return rutgers_bank
        
def select_question(correct_bank):
    question = correct_bank.sample(n=1)
    return question
        
def display_q(question):
    print(question['question'].iloc[0])
    return

def get_guess():
    guess = input('Answer here:... ')
    return guess

def check_answer(user_guess,question):
    answer = question['answer'].iloc[0]
    if user_guess == answer:
        return True
    else:
        return False
    
def give_feedback(valid):
    if valid:
        print('You are a champ!!!!')
    else:
        print('C\'mon... Not even close')
        
def remove_question(my_bank,my_q):
    
    my_bank = my_bank[my_bank.index != my_q.index[0]]
    return my_bank
    
def play_single_turn():    
    color = determine_color()
    category = determine_category(color)
    my_bank = get_correct_bank(category,food_bank,rutgers_bank)
    my_q = select_question(my_bank)

    display_q(my_q)
    the_guess = get_guess()
    valid = check_answer(the_guess,my_q)
    give_feedback(valid)
    remove_question(my_bank,my_q)
    return valid

i = 0
while i < 3:
    points = 0
    score = play_single_turn()
    if score:
        points += 1
    i += 1









