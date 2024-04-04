print('Welcome to Love💖 Calculator!')
name1 = input('what is your name? ').lower()
name2 = input('what is there name? ').lower()

combined_string = name1 + name2
changeLowerCase = combined_string.lower()

t = changeLowerCase.count('t')
r = changeLowerCase.count('r')
u = changeLowerCase.count('u')
e = changeLowerCase.count('e')

true = t + r + u + e
l = changeLowerCase.count('l')
o = changeLowerCase.count('o')
v = changeLowerCase.count('v')
e = changeLowerCase.count('e')

love = l + o + v + e

loveScore = str(true) + str(love)

print(f'you have {loveScore}% chance to be your love or wife')
