import random
from game_data import data


# Start HigherLowerGame


def formateData(account):
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
accountB = random.choice(data)

while gameContinue:
    accountA = accountB
    accountB = random.choice(data)

    while accountA == accountB:
        accountB = random.choice(data)

    print(f'compare A:{formateData(accountA)}')
    print("Vs")
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
