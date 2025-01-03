from game import Card

# Compares two hands, both players have two cards + 5 table cards
def compare(player1, player2, table_cards):
    pass

# returns the highest card
def get_high_card():
    pass

# returns all card with a match (full house, pair, three of a kind, two pair)
def get_duplicate():
    pass

# given 7 cards, return the 5 cards that make a straight if any
def get_straight(cards):
    sorted_cards = sorted(cards, key=Card.compare_rank, reverse=True)
    sorted_cards.extend(get_low_aces(sorted_cards))
    print(sorted_cards)
    prev_card = sorted_cards[0]
    straight = [prev_card]
    for card in sorted_cards:
        if prev_card.int - card.int == 1:
            straight.append(card)
        else:
            straight = [card]
        if len(straight) >= 5:
            return straight
        prev_card = card
    return []

# helper method to duplicate aces and make them low
def get_low_aces(cards):
    aces = True
    i = 0
    low_aces = []
    while aces:
        if cards[i].value != "A":
            aces = False
            return low_aces
        card = Card("A", cards[i].suit)
        card.make_low_ace()
        low_aces.append(card)
        i += 1

# given 7 cards, return if 5 are the same suit
def get_flush(cards):
    sorted_cards = sorted(cards, key=Card.compare_suit)
    prev_card = sorted_cards[0]
    flush = [sorted_cards[0]]
    for card in sorted_cards[1:]:
        if prev_card.suit == card.suit:
            flush.append(card)
        else:
            flush = [card]
        if len(flush) >= 5:
            return flush
        prev_card = card
    return []

# "♥", "♦", "♣", "♠"
cards = [Card("A", "♠"), Card("A", "♦"), Card("3", "♠"), Card("10", "♠"), Card("J", "♠"), Card("K", "♠"), Card("Q", "♣")]
print(get_flush(cards))