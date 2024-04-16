import random

import replit as replit


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
        cards.append(1)
    return sum(cards)


def compare(userScore, computerScore):
    if userScore == computerScore:
        return "Draw"
    elif computerScore == 0:
        return " lost the opponent has blackjack"
    elif userScore == 0:
        return "win with a blackjack"
    elif userScore > 21:
        return " you went over. you lost"
    elif computerScore > 21:
        return "opponent went over .you win"
    elif userScore > computerScore:
        return "you win"
    else:
        return "you lost"


def BlackJack():
    userCards = []
    computerCards = []
    isGameOver = False

    for _ in range(2):  # run this loop two times

        userCards.append(dealCard())
        computerCards.append(dealCard())

    print(userCards)
    print(computerCards)

    while not isGameOver:
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)
        print(f"Your cards:{userCards},current score: {userScore}")
        print(f"Computer cards:{computerCards[0]}")

        if userScore == 0 or computerScore == 0 or userScore > 21:
            isGameOver = True
        else:
            userShouldDeal = input("Type 'y' to get another card, type 'n' to pass: ")
            if userShouldDeal == 'y':
                userCards.append(dealCard())
            else:
                isGameOver = True

    while computerScore != 0 and computerScore < 17:
        computerCards.append((dealCard()))
        computerScore = calculateScore(computerCards)

    print(f"your final hand is {userCards}, final score: {userScore}")
    print(f"computer  final hand is {computerCards}, final score: {computerScore}")

    print(compare(userScore, computerScore))


while input(" do you went to play a game of Blackjack? type 'y' or 'n': '") == "y":
    replit.clear()
    BlackJack()
