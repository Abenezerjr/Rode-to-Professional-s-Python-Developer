import random
from game_data import data
import art

# Start HigherLowerGame


def formateData(account):
    """
    the function take account in the data list
    :return string of an account
    """
    accountName = account['name']
    accountDescription = account['description']
    accountCountry = account['country']
    return f'{accountName}, a {accountDescription}, form {accountCountry}'


def checkAnswer(guess, aFollowers, bFollowers):
    if aFollowers > bFollowers:
        return guess == 'a'
    else:
        return guess == 'b'


score = 0
gameContinue = True
accountB = random.choice(data)  # choose random ig data and save in the accountB

while gameContinue:
    accountA = accountB  # the user right saves the data be in the data a
    accountB = random.choice(data)  # another data and save in data b

    while accountA == accountB:
        accountB = random.choice(data)  # if there is equal change data b

    print(f'compare A:{formateData(accountA)}')
    print(art.vs)
    print(f'Against B:{formateData(accountB)}')

    guss = input("who has more followers? Type 'A' or 'B'.").lower()

    aFollowerCount = accountA['follower_count']
    bFollowerCount = accountB['follower_count']

    isCorrect = checkAnswer(guss, aFollowerCount, bFollowerCount)

    if isCorrect:
        score += 1
        print(f'you right! current score: {score}')
    else:
        gameContinue = False
        print(f'sorry that wording , final score {score}')
