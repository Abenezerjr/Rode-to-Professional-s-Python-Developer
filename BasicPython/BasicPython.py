# the pyton code is the sequence of instartctiom


# squtinal
x = 10

print(x)
x = x + 20

print(x)
print('-------------------------')
# conditonal
n = 1

if n < 5:
    print('this {n}', n)
else:
    print("grater")

#  repeated step
m = 10

while m > 0:
    print(m)
    m = m - 1
else:
    print('format the loop', m)

# string conversion
# name = input("what is your age ?")
# save = int(name) + 50
# years = 2024 + 50
# print('in', years, "you are", save, 'years old')
# example 2

num2 = '1234'
print(type(num2))
try:
    print(num2 + 1)
except:
    print('error occur b/c num2 is string')

num3 = int(num2)
print(type(num3))
print(num3 + 1)  # expected result 123

# Input

# name=input('what is your name ?')
# print("wellcome" , name)

# Input
# a = input("europium floor?")
# a = int(a)
# usf = a + 1
# print(usf)

# input
# c = int(input('ethiopian floor'))  # change there
# amrican = c + 1
# print(amrican)

# ------------------------------ April-1--------------------------------------------- #

for i in range(5):
    print(i)
    if i > 2:
        print('its bigger than the 2')
    print('this value i is', i)
print('all done:')


# function store and reused

def thinge():
    print('hello')
    print('how are you!')


# invoke the function
thinge()
print('im a breaker')
thinge()

# example two of function

new = 5
print('a im print stetement under new=5')


def print_lyrics():
    """
    this this function ,,,, self defined function  that return 2 print statements this function is defind and store
    or remember but
    :return:
    """
    print('i falling you')
    print('say something if you cache')


# I am calling the above function
print_lyrics()
new = new + 2
print(new)


# Arguments is a value we pass in to the function as its input when w call function
def greet(lang):
    """
    :param lang:
    :return language of which we pass:
    """
    if lang == 'fr':
        print('Bonjour')

    elif lang == 'es':
        print('hola')
    else:
        print('hello')


greet('fr')
greet('es')
greet('what')

print('========================================')


# return value in function
def selam():
    """
    when we use return function we used returen the value returen mean's when some thing get exit this function
    :return:
    """
    return 'endet nehe'


print(selam(), "abebe")
print(selam(), 'selam nw chaletu')

# example 2
print("example 2 ===========================================")


def selameta(lang):
    if lang == 'es':
        return 'hola'
    elif lang == 'fr':
        return 'Bonjour'

    else:
        return 'hello'


print(selameta('fr'), "abenet")

big = max('hello worldz')
print(big)


# multiple parameter

def addtwo(a, b):
    added = a + b
    return added


print(addtwo(10, 20))

# Loops and iteration

# while
# m = 5
# while m > 0:
#     print(m)
#     m = m - 1
# print('blastoff')
# print(n)
# # while with break - it's break inner loop whit that --------------------
# print('while with break ------------')
# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)
# print('done!')

# --------------------continue----

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('done')