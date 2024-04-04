import random

chose = input('choose on of them Head or Tail').lower()
head = 1
tail = 2
c = random.randint(head, tail)

if c % 2 == 0:
    print(f' your choose {chose} the result is Head')
else:
    print(f' your choose {chose} the result is Head')
