from constants import *
from player import *
from game import *

game = None

def print_game():
    print("")

def setup_game():
    global game
    players = []
    for i in range(NUM_PLAYERS):
        players.append(Player((i + 1), STARTING_CHIPS, PLAYER_TYPES[1]))
    game = Game(players)

def take_turn():
    pass

def take_first_turn():
    #player on button and next to them must small and big blind
    pass

setup_game()