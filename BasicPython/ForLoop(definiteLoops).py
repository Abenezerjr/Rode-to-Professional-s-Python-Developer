# # definite Loop
#
# # for loop with number
# for i in [5, 4, 3, 2, 1]:
#     print(i)
# print('i am out of the forloop😁')
#
# # for loop with string
# friends = ['fker', 'hayle', 'abebe', 'yesehak']
#
# for friend in friends:
#     print('wellcome home', friend)
#
# print(' i am out of the forloopString agine')

# example 1
numbers = [3, 41, 12, 9, 74, 15]
largest_number = 0
for number in numbers:
    if number > largest_number:
        largest_number = number

print('largest number is', largest_number)
# example2 count how many loop element in the above example

count = 0

for number in numbers:
    count = count + 1
print('the number or element in the  loop is', count)

# example 3 what is the total of the above list

total = 0

for number in numbers:
    total = total + number

print('the total of the of the list is', total)

# example for what is the avarage of the above list

counts = 0
totals = 0

for number in numbers:
    counts = counts + 1
    totals = totals + number
average = total / counts
print('the average of the above list is', average)

# example 5 list out all numbers above 20

for number in numbers:
    if number > 20:
        print('this number is grater than 20', number)
# example 6 smallest number
smallest = None

for number in numbers:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number

print("the smallest number is", smallest)

# is Operators
# is operator that can used in logical expression it implies 'is the same as' similar to but strong than ==

