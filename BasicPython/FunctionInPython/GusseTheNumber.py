import random

# print('Welcome to the number Guessing game!')
# print("'i'm thinking of number between 1 and 100")

"""
the inefficient way to build high low game
"""
# isGameOn = True
# computerThinkingNumber = random.choice(range(1, 101))
# print(computerThinkingNumber)
#
# easy = 10
# hard = 5
# difficulty = input("Type 'easy' or 'hard': ")
# if difficulty == "easy":
#     print(f"You have {easy}  attempts remaindering to guess the number")
# elif difficulty == 'hard':
#     print(f"You have {hard}  attempts remaindering to guess the number")
#
# while isGameOn:
#     if difficulty == 'easy':
#         guess = int(input('Make a guess: '))
#         if guess > computerThinkingNumber:
#             print('Too high')
#             easy = easy - 1
#
#             print(f"You have {easy}  attempts remaindering to guess the number")
#             if easy == 0:
#                 isGameOn = False
#                 print('you lose')
#         elif guess < computerThinkingNumber:
#             print('Too low')
#             easy = easy - 1
#             print(f"You have {easy}  attempts remaindering to guess the number")
#             if easy == 0:
#                 isGameOn = False
#                 print('you lose')
#
#         elif guess == computerThinkingNumber:
#             isGameOn = False
#             print("yo got it ")
#
#     elif difficulty == 'hard':
#         guess = int(input('Make a guess: '))
#         if guess > computerThinkingNumber:
#             print('Too high')
#             hard = hard - 1
#
#             print(f"You have {hard}  attempts remaindering to guess the number")
#             if hard == 0:
#                 isGameOn = False
#                 print('you lose')
#         elif guess < computerThinkingNumber:
#             print('Too low')
#             hard = hard - 1
#
#             print(f"You have {hard}  attempts remaindering to guess the number")
#             if hard == 0:
#                 isGameOn = False
#                 print('you lose')
#
#         elif guess == computerThinkingNumber:
#             isGameOn = False
#             print("yo got it ")
"""
efficient way to the game
"""
eastLevel = 10
hardLevel = 5


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def setDifficulty():
    difficulty = input("Type 'easy' or 'hard:")
    if difficulty == 'easy':
        return eastLevel
    else:
        return hardLevel


def highAndlow():
    print('Welcome to the number Guessing game!')
    print("'i'm thinking of number between 1 and 100")

    computerThinkingNumber = random.randint(1, 100)
    print(computerThinkingNumber)
    turns = setDifficulty()

    guess = 0

    while guess != computerThinkingNumber:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guss: "))
        turns = check_answer(guess, computerThinkingNumber, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            # return
        elif guess != computerThinkingNumber:
            print("Guess again.")


highAndlow()
