from constants import *
from player import *
from game import *
from actions import *
import time

game = None

def print_game(hidden = False):
    print("Player", game.turn + 1, "turn")

    table_card_string = ""
    for card in game.table_cards:
        table_card_string += str(card) + "   "
    print("Table Cards:", table_card_string)

    print("Current Pot:", game.pot, '\n')

    player_strings = []
    for player in game.players:
        if not player.in_game:
            player_strings.append(player.folded_string())
        elif hidden and player.player_type is not HUMAN:
            player_strings.append(player.hidden_string())
        else:
            player_strings.append(str(player))
    print_players(player_strings)
    print("=" * 22 * game.num_players, '\n')

def print_players(players):
    player_lines = [player.splitlines() for player in players]
    formatted_lines = []
    for line_parts in zip(*player_lines):
        formatted_line = "    ".join(f"{line_part:<20}" for line_part in line_parts)
        formatted_lines.append(formatted_line)
    output = "\n".join(formatted_lines)
    print(output)

def setup_game():
    global game
    players = []
    for i in range(NUM_PLAYERS):
        players.append(Player((i + 1), STARTING_CHIPS, DEFAULT_PLAYER_TYPES[i]))
    game = Game(players)
    set_game(game)
    take_blind_turn()
    print_game(HIDDEN)

def take_turn():
    current_player = game.players[game.turn]
    if not current_player.in_game:
        return
    decisions = game.get_possible_decisions(current_player)
    current_player.make_decision(decisions)
    if game.turn == len(game.players) - 1:
        game.turn = 0
    else:
        game.turn += 1

def take_blind_turn():
    player1 = game.players[game.button]
    blind_action(player1, game.small_blind)

    time.sleep(TIME_BETWEEN_ACTIONS)

    player2 = game.players[game.button + 1]
    blind_action(player2, game.big_blind)
    game.turn = 2

def play_poker():
    while not game.round_is_over:
        take_turn()
        bets = set()
        for player in game.players:
            if player.in_game:
                bets.add(player.total_bet)
        #if everyone is settled
        if len(bets) == 1:
            cards_on_table = len(game.table_cards)
            if cards_on_table == 0:
                game.reveal_cards(3)
                print_game(HIDDEN)
            elif cards_on_table == 3 or cards_on_table == 4:
                game.reveal_cards(1)
                print_game(HIDDEN)
            else:
                game.round_is_over
                print_game(HIDDEN)
        time.sleep(TIME_BETWEEN_ACTIONS)

print("POKER GAME 1.0")
print("dealing cards...\n")
time.sleep(TIME_BETWEEN_ACTIONS)
setup_game()
play_poker()
