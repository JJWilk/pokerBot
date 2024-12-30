from constants import *
import random

class Game():
    def __init__(self, players, num_players = NUM_PLAYERS, small_blind = SMALL_BLIND, big_blind = BIG_BLIND):
        self.num_players = num_players
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.turn = 0
        self.players = players
        self.deck = self.make_deck()
        self.deal_cards()
        self.table_cards = []
        self.button = 0 #the button starts on player 0

    def make_deck(self):
        deck = []
        for i in range(len(SUITS)):
            for j in range(len(VALUES)):
                deck.append(Card(VALUES[j], SUITS[i]))
        return deck
    
    def deal_cards(self):
        for player in self.players:
            player.give_card(self.draw_card())
            player.give_card(self.draw_card())
        random.shuffle(self.deck)
    
    def draw_card(self):
        i = random.randint(0, len(self.deck))
        return self.deck.pop(i)
    
    def reveal_cards(self, num_cards):
        for i in range(num_cards):
            self.table_cards.append(self.draw_card())

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return self.value + self.suit