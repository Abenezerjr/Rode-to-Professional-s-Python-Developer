import random
from HangmanWords import word_list
from HangmanArt import logo, HANGMANPICS

print(logo)

# Step 1
# word_list = ["aardvark", "baboon", "camel"]

chosenWord = random.choice(word_list)
print(chosenWord)
countLive = 0
gameContinue = True

emptyList = []
for _ in chosenWord:
    emptyList.append('_')
print(emptyList)

while gameContinue:
    guess = input("guess a letter: ").lower()
    if guess in emptyList:
        print(f'you already guessed {guess}')

    for position in range(len(chosenWord)):
        letter = chosenWord[position]
        if guess == letter:
            emptyList[position] = letter
    print(emptyList)
    if guess not in chosenWord:
        countLive += 1
        print(f'your guess {guess} is not in the letter now you have {6-countLive} lives left ')
        if countLive == 6:
            gameContinue = False
            print('You lose The man is dia')
    print(f"{''.join(emptyList)}")
    if "_" not in emptyList:
        gameContinue = False
        print(f'the letter computer generated{chosenWord} you guss is{guess} ')
        print('Congratulation you win')
    print(HANGMANPICS[countLive])