import random

# Rock Paper Scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)_________
          ___________)
          ___________)
         ____________)
---._________________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

yourChoose = int(input("what do you you choose? type 0 for Rock. 1 for Paper or for 2 Scissors . "))
try:
    answer = rps[yourChoose]
    print(answer)
    computerChoose = random.choice(rps) # i coose choice

    print(f"Computer Chose: \n {computerChoose}")

    if answer == rock and computerChoose == rock:
        print("it Draw")
    elif answer == scissors and computerChoose == scissors:
        print("it Draw")
    elif answer == paper and computerChoose == paper:
        print('it Draw')
    elif answer == rock and computerChoose == scissors:
        print('You win')
    elif answer == rock and computerChoose == paper:
        print('You lost! computer won')
    elif answer == scissors and computerChoose == paper:
        print('You win')
    elif answer == scissors and computerChoose == rock:
        print('You lost computer won')
    elif answer == paper and computerChoose == scissors:
        print('You lost computer won')
    elif answer == paper and computerChoose == rock:
        print(' you win')
    else:
        print('Invalid number')


except :
    print('Invalid number')




