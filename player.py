from constants import *
from actions import *
import random

class Player():
    def __init__(self, player_num, starting_chips, player_type):
        self.player_num = player_num
        self.current_chips = starting_chips
        self.total_bet = 0
        self.player_type = player_type
        self.cards = []
        self.bet_history = []
        self.in_game = True
    def __str__(self):
        string = "Player: " + str(self.player_num) + '\n' + "Type: " + str(self.player_type) + '\n' + "Chips: " + str(self.current_chips) + '\n' + "Cards: " + str(self.cards[0]) + ", " + str(self.cards[1])
        return string 
    def hidden_string(self):
        string = "Player: " + str(self.player_num) + '\n' + "Type: " + str(self.player_type) + '\n' + "Chips: " + str(self.current_chips) + '\n' + "Cards: " + "XX" + ", " + "XX"
        return string 
    def folded_string(self):
        string = "Player: " + str(self.player_num) + '\n' + "Type: " + str(self.player_type) + '\n' + "Chips: " + str(self.current_chips) + '\n' + "Cards: " + "FOLDED"
        return string 
    def give_card(self, card):
        self.cards.append(card)
        
    def discard(self):
        self.cards = []

    def prompt_human(self, possible_decisions, functions):
        print("Please Select an Option")
        for i in range(len(possible_decisions)):
            print(str(i + 1) + ": " + possible_decisions[i])
        print()
        selection = int(input()) - 1
        action = possible_decisions[selection]
        print("You have decided to", action)
        if action == RAISE:
            print("Choose Raise Amount, Maximum Raise is:", self.current_chips)
            raise_amount = input()
            self.raise_action(raise_amount)
        else:
            functions[action](self)

    def make_decision(self, possible_decisions):
        #check which type of agent you are
        agent = self.player_type
        functions = {"RAISE": raise_action, FOLD: fold_action, CALL: call_action, CHECK: check_action}
        
        if agent == HUMAN:
            self.prompt_human(possible_decisions, functions)
        elif agent == RANDOM:
            action = random.choice(possible_decisions)
            functions[action](self)
        elif agent == AUTO:
            raise Exception("AUTO not currently supported")
        elif agent == AI:
            raise Exception("AI not currently supported")