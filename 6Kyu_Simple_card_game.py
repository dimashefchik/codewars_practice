# Steve and Josh are bored and want to play something. They don't want to think too much, so they come up with a really simple game. 
# Write a function called winner and figure out who is going to win.

# They are dealt the same number of cards. They both flip the card on the top of their deck. 
# Whoever has a card with higher value wins the round and gets one point (if the cards are of the same value, neither of them gets a point). 
# After this, the two cards are discarded and they flip another card from the top of their deck. They do this until they have no cards left.

# deckSteve and deckJosh are arrays representing their decks. They are filled with cards, represented by a single character. 
# The card rank is as follows (from lowest to highest):

# '2','3','4','5','6','7','8','9','T','J','Q','K','A'
# Every card may appear in the deck more than once. Figure out who is going to win and return who wins and with what score:

# 1. "Steve wins x to y" if Steve wins; where x is Steve's score, y is Josh's score;
# 2. "Josh wins x to y" if Josh wins; where x is Josh's score, y is Steve's score;
# 3. "Tie" if the score is tied at the end of the game.

def winner(deck_steve, deck_josh):
    cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    steve_score = 0
    josh_score = 0
    for i in range(0,len(deck_steve)):
        if int(cards.index(deck_steve[i])) > int(cards.index(deck_josh[i])):
            steve_score += 1
        elif cards.index(deck_steve[i]) < cards.index(deck_josh[i]):
            josh_score += 1
    if steve_score > josh_score:
        return f'Steve wins {steve_score} to {josh_score}'
    elif steve_score < josh_score:
        return f'Josh wins {josh_score} to {steve_score}'
    else:
        return "Tie"
