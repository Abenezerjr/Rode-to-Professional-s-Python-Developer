import random

# Step 1


word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosenWord = random.choice(word_list)
print(chosenWord)
name = chosenWord.split()
chosenList = []
for i in chosenWord:
    chosenList.append(i)
print(chosenList)
print(chosenList[0])
emptyList = []
for n in chosenWord:
    emptyList.append('_')
print(emptyList)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("guess a letter: ").lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

letters = []
for letter in guess:
    letters.append(letter)
print(letters)

if letters[0] == chosenList[0]:
    print(letters[0])
