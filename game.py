from constants import *
import random

class Game():
    def __init__(self, players, num_players = NUM_PLAYERS, small_blind = SMALL_BLIND, big_blind = BIG_BLIND):
        self.num_players = num_players
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.players = players
        self.button = None
        self.round_is_over = False
        self.reset_table()

    def make_deck(self):
        deck = []
        for i in range(len(SUITS)):
            for j in range(len(VALUES)):
                deck.append(Card(VALUES[j], SUITS[i]))
        return deck
    
    def reset_table(self):
        if not self.button or self.button == self.num_players - 1:
            self.button = 0
        else:
            self.button += 1
        self.current_bid = self.big_blind
        self.pot = 0
        self.turn = 0
        self.table_cards = []
        self.deck = self.make_deck()
        for player in self.players:
            player.discard()
        self.deal_cards()
    
    def deal_cards(self):
        for player in self.players:
            player.give_card(self.draw_card())
            player.give_card(self.draw_card())
        random.shuffle(self.deck)
    
    def draw_card(self):
        i = random.randrange(0, len(self.deck))
        return self.deck.pop(i)
    
    def reveal_cards(self, num_cards):
        for i in range(num_cards):
            self.table_cards.append(self.draw_card())

    def add_to_pot(self, amount):
        self.pot += amount

    def get_possible_decisions(self, player):
        possible_decisions = [FOLD]
        #if we are not settled up
        money_bet = player.total_bet
        if money_bet < self.current_bid:
            if (self.current_bid - money_bet) >= player.current_chips:
                possible_decisions.append(ALLIN)
                return possible_decisions
            else:
                possible_decisions.append(CALL)
                possible_decisions.append(RAISE)
        else:
            possible_decisions.append(CHECK)
        return possible_decisions

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return self.value + self.suit