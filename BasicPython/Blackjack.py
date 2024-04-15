import random


#  Blackjack Game Rules

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

#
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# user = [random.choice(cards)]
# computer = [random.choice(cards)]
# if len(user) < 2 and len(computer):
#     user.append(random.choice(cards))
#     computer.append(random.choice(cards))
# print(f'User:{user}')
# print(f'Computer:{computer}')
#
# userScore = sum(user)
# computerScore = sum(computer)
# print(userScore)
# print(computerScore)

def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculateScore(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.add(1)
    return sum(cards)


userCards = []
computerCards = []
isGameOver=False

for _ in range(2):  # run this loop two times

    userCards.append(dealCard())
    computerCards.append(dealCard())

print(userCards)
print(computerCards)

userScore = calculateScore(userCards)
computerScore = calculateScore(computerCards)
print(userScore)
print(computerScore)

if userScore == 0 or computerScore==0 or userCards > 21:
    isGameOver=True