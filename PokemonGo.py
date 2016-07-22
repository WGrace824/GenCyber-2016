# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 13:38:33 2016

@author: student
"""
from random import randint

class Pokemon:
    def __init__(self, oriName, oriType, orihp, oriMoves):
        self.name = oriName
        self.type = oriType
        self.hp = orihp
        self.cp = randint(1,600)
        self.moves = oriMoves
        
    def battle(self, myMove, opponent, opponentMove):
#my move and announce it        
        print(self.name + " USED" + myMove + "!!!")        
#opponent health - my attack damage        
        opponent.hp -= (self.moves[myMove] * self.cp)
#Check if they alive        
        print(opponent.name + " HAS" + str(opponent.hp))
        if opponent.hp <= 0:
            print(opponent.name + "DEAD")
            print("YOU WON!!!")
            return
        print(opponent.name + " USED" + opponentMove + " !!!" )
        self.hp -= (opponent.moves[opponentMove] * opponent.cp)
        print(self.name + " HAS" + str(self.hp))
        if self.hp <= 0:
            print(self.name + "DEAD")
            print("YOU LOSE!!!")
            return    
        print("DRAW")


eevee_moves = {"SWIFT": 10, "DIG": 20}   
vee = Pokemon("EEVEE", "Normal", 5, eevee_moves)
print(vee.cp)

tortu_moves = {"DOUBLE-EDGE" : 120, "FOCUS PUNCH" : 150}
tortu = Pokemon("WARTORTLE", "Water", 59, tortu_moves)
print(tortu.cp)

vee.battle("Dig", tortu, "DOUBLE-EDGE")


