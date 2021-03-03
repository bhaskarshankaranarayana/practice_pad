# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:02:41 2020

@author: eefhiio
"""
from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

my_cards = [(s,r) for s in SUITE for r in RANKS] #list comprehension

#equivalent for loop
#my_cards = []
#for s in SUITE:
#    for r in RANKS:
#        my_cards.append((s,r))


class Deck:
    
    def __init__(self,my_cards):
        print("Creating new card DECK!")
        self.all_cards = my_cards
        
    def shuffle(self):
        print("SHUFFLING the DECK!")
        shuffle(self.all_cards)
    
    def split_in_half(self):
        return (self.all_cards[:int(len(self.all_cards)/2)],self.all_cards[int(len(self.all_cards)/2):])
    
class Hand:
    def __init__(self,cards):
        self.cards = cards
        
    def __str__(self):
        return f'Contains {len(self.cards)} cards'
    
    def add_cards(self,added_cards):
        self.cards.extend(added_cards)
        
    def remove_cards(self):
        return self.cards.pop()
    
class Player:
    
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
    
    def play_card(self):
        drawn_cards = self.hand.remove_cards()
        print(f'{self.name} has placed:{drawn_cards} \n')
        return drawn_cards
    
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_cards())
            return war_cards
    
    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0
    
print("Welcome to war,, Let's begin..")

d= Deck(my_cards)
d.shuffle()
half_1,half_2 = d.split_in_half()

comp = Player("Computer",Hand(half_1))

name = input("What is your name?")
user = Player(name,Hand(half_2))

total_rounds = 0
war_counts = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds +=1
    print("Time for New round!")
    print("Here are the current standings")
    print(user.name + "has the count: "+str(len(user.hand.cards)))
    print(comp.name + "has the count: "+str(len(comp.hand.cards)))
    print("Play a card! \n")
    
    table_cards = []
    
    c_cards = comp.play_card()
    p_cards = user.play_card()
    
    table_cards.append(c_cards)
    table_cards.append(p_cards)
    
    if c_cards[1] == p_cards[1]:
        war_counts +=1
        
        print("WAR!!!")
        
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())
        
        if RANKS.index(c_cards[1]) < RANKS.index(p_cards[1]):
            user.hand.add_cards(table_cards)
            
        else:
            comp.hand.add_cards(table_cards)
        
    else:
        if RANKS.index(c_cards[1]) < RANKS.index(p_cards[1]):
            user.hand.add_cards(table_cards)
            
        else:
            comp.hand.add_cards(table_cards)
            
print(f"Game OVER!, number of rounds : {str(total_rounds)}")
print("war happend",str(war_counts)," times")

print(f"Computer has cards?? {str(comp.still_has_cards())}")
print(f"{user.name} has cards?? {str(user.still_has_cards())}")