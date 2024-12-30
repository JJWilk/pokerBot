from constants import *
import random

class Player():
    def __init__(self, player_num, starting_chips, player_type):
        self.player_num = player_num
        self.current_chips = starting_chips
        self.player_type = player_type
        self.cards = []
    def __str__(self):
        string = "Player: " + str(self.player_num) + '\n' + "Type: " + str(self.player_type) + '\n' + "Chips: " + str(self.current_chips) + '\n' + "Cards: " + str(self.cards[0]) + ", " + str(self.cards[1])
        return string
    def give_card(self, card):
        self.cards.append(card)
    def bet(self, bet_value):
        if bet_value > self.current_chips:
            #go all in
            self.current_chips = 0
        self.current_chips -= bet_value

    def make_decision(self, possible_decisions):
        #check which type of agent you are
        agent = self.player_type
        
        if agent == "HUMAN":
            self.prompt_human(possible_decisions)
        elif agent == "RANDOM":
            random.choice(possible_decisions)
        elif agent == "AUTO":
            raise Exception("AUTO not currently supported")
        elif agent == "AI":
            raise Exception("AI not currently supported")
        

    def prompt_human(self, possible_decisions):
        print("Please Select an Option")
        for i in range(len(possible_decisions)):
            print(str(i + 1) + ": " + possible_decisions[i])
        print()
        selection = int(input()) - 1
        selection = possible_decisions[selection]
        print("You have decided to", selection)
        if selection == "RAISE":
            print("Choose Raise Amount, Maximum Raise is:", self.current_chips)
            raise_amount = input()

pl = Player(1, 100, "HUMAN")
pl.make_decision(ACTIONS)
