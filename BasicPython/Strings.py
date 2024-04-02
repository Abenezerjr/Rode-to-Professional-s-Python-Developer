# string is a sequence of characters

fruit = 'banana'
for letter in fruit:
    print(letter)
print("the length od the string is", len(fruit))
# example looping in string using index
index = 0
for letter in fruit:
    index = index + len(letter)
    print(f"the is index is {index},and the letter is {letter}")
# example 2 count the number of a in the fruit

count = 0
for letter in fruit:
    if letter == 'a':
        count = count + 1
print(f'the number of "a" in the word banana is {count}')
# in key word in python see uncanceled in sues
# More String Operation
# slice ###########
# when we used a slice we use [a:b] a and b is the integer number
# b is one beyond the end of the slice 'up to but not including"
#   0123456789101112
s = 'good😁morning'

print(s[0:4])  # good
print(s[:5])  # good😁
print(s[7:8])  # r
print(s[4:8])  # 😁mor

print(s[-4:4])  #

# string concatenation
a = 'hello'
b = 'there'
print(a, b)
print(a + b)
print(a + "" + b)
print(a + " " + b)

# String default function
c = '  hello world  '
d = c.upper()
print(d)
print(d.lower())
print(c.find('r'))  # find the index of the element
print(c.replace('hello', 'greeting'))  # change the "hello" to "greeting"

print(c.lstrip())  # remove whitespace at the left
print(c.rstrip())  # remove whitespace at the right
print(c.strip())  # remove whitespace at the both

well = 'pleas have a nice day'
print(well.startswith('pleas')) # ask to start the line of the string
