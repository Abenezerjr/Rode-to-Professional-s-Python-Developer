import random

# Step 1
word_list = ["aardvark", "baboon", "camel"]

chosenWord = random.choice(word_list)
print(chosenWord)

gamesGoing = True

emptyList = []
for _ in chosenWord:
    emptyList.append('_')
print(emptyList)

guess = input("guess a letter: ").lower()
for position in range(len(chosenWord)):
    letter = chosenWord[position]
    if guess == letter:
        emptyList[position] = letter
print(emptyList)
