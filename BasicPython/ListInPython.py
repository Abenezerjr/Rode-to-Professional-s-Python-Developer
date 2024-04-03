# List
# List is like allows us to put many values in a single 'variable'
# List constants are surrounded by square bracket, and the elements in the are separated by commas
friends = ['hale', 'Glenn', 'Sally', 'joe']
print(friends)
print([1, 2, 3])
print([1, [2, 3], 5])
for i in [1, 2, 3, 4, 6]:
    print(i)
print("endloop")
# iteration in-the loop
for friend in friends:
    print('hello gus selam', friend)
print('done')
# lists are Mutable
"""
 " immutable" b/c we cannot change the contents of a string-
we must mack a new string to make any change Eg : Strings
"""
# example 2 Immutable
fruit = "banana"
print(fruit[0])  # b
# fruit[0] = "B"
print(fruit)  # error b/c  strings is immutable if we went to change we must used new string

"""
mutable : change element of list using index eg list
"""
# example mutable
name = ['abebe', 'chala', 'muchayehu', "chaletu"]
print(name)
name[0] = 'kebenicha'
print("change")
print(name)
print(len(name))
# concatenating list using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b  # + using concatenating
print(a)  # [1,2,3]
print(b)
print(c)
# list Methods -----------------

print(type(name))
name.append('chebude')  # add in the list
print(name)
name.sort()
print(name)
name.pop()
print(name)

# build in function in a list
numberss = [10, 5, 6, 8, 3, 5, 1]

print(len(numberss))
print(max(numberss))
print(min(numberss))
print(sum(numberss))
print(sum(numberss) / len(numberss))

# example one

# numlist = []
#
# while True:
#     inp = input('enter the number: ')
#     if inp == 'done': break
#     value = float(inp)
#     numlist.append(value)
# average = sum(numlist) / len(numlist)
# print(f'the average of the number er you add {average}')

# while True:
#     inp=input('enter the number')
#     if inp=='done':break
#     value=float(inp)

# about split()
ListofName="abebe chala gemega"
print(ListofName.split())
listofage='12;35;65'
print(listofage.split(';'))


