from game import *

game = None

def set_game(set_game):
    global game
    game = set_game

def raise_action(player, amount = 5):
    player.bet_history.append(amount)
    player.current_chips -= amount
    player.total_bet += amount
    game.add_to_pot(amount)
    print("Player", player.player_num, "RAISED", amount)

def allin_action(player):
    amount = player.current_chips
    player.append(amount)
    player.current_chips -= amount
    player.total_bet += amount
    game.add_to_pot(amount)
    print("Player", player.player_num, "went ALL IN with", amount)

def call_action(player, amount = 5):
    player.bet_history.append(amount)
    player.current_chips -= amount
    player.total_bet += amount
    game.add_to_pot(amount)
    print("Player", player.player_num, "CALLED", amount)

def blind_action(player, amount = 1):
    player.bet_history.append(amount)
    player.current_chips -= amount
    player.total_bet += amount
    game.add_to_pot(amount)

def fold_action(player):
    player.bet_history.append(float('-inf'))
    player.in_game = False
    print("Player", player.player_num, "FOLDED")

def check_action(player):
    player.bet_history.append(0)
    print("Player", player.player_num, "CHECKED")