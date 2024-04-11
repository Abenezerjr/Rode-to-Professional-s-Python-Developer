programmingDictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                         "Function": "A piece of code that you can easily call over and over again."}

# print(programmingDictionary)
# print('----------------------------------------------------------------')
# print(programmingDictionary['Bug'])
# print('-------------------------------')

# Dic = {'key': 'value'}
#
# print(Dic)
# print(Dic['val'])
# print()

"""what is dice: As you can see from the example, data is stored in key:value pairs in dictionaries, which makes it 
easier to find values.
it is allow us to do fast database-like operation in python

"""

studentScore = {
    "joe": 100,
    'jon': 87,
    'arson': 54,
    'berry': 86,
    'simon': 67,
}

# if 91 < 93 <= 100:
#     print(True)
# else:
#     print(False)

newDictionary = {}  # creating empty Dictionary

for key in studentScore:
    # print(key)
    # print(studentScore[key])
    if 91 < studentScore[key] <= 100:
        newDictionary[key] = 'Outstanding'  # adding new kay:value in the new string
    elif 81 < studentScore[key] <= 90:
        newDictionary[key] = 'exceedsExpectation'
    elif 71 < studentScore[key] <= 80:
        newDictionary[key] = 'Acceptable'
    else:
        newDictionary[key] = 'Fail'

print(newDictionary)

name = dict()

name["anenezer"] = 12
name['chala'] = 15
name['gemeda'] = 24
print(name)
name['anenezer'] = name['anenezer'] + 3  # using anenezer key add in to the varible of 12 and the expacting output is
# 'qbenezer':15
print(name)

# Counting
# count=dict()
count = {}
names = [
    "a",
    'b',
    'c',
    'a',
    'c',
]

for name in names:
    # if name not in count:
    #     count[name] = 1
    # else:
    #     count[name] = count[name] + 1

    count[name] = count.get(name, 0) + 1  # equale to the above if stetement
    # we used the get() and provide a default value of 0 when the
    # key is not yet in the dictionary-and then just add one
print(count)

# if name in count:
#     x = count[name]
#     print(x)
# else:
#     x = 0


# get method for dictionaries
"""the pattern of checking to see if a  key is already in the dictionary and assuming a default value if the key is 
not there is so common thet there is method called get()"""
# loop in dictionary
studentMark = {
    "joe": 100,
    'jon': 87,
    'arson': 54,
    'berry': 86,
    'simon': 67,
}
print(studentMark['joe'])
print('===============')
for key in studentMark:
    print(key,studentMark[key])
# Retrieving lists of keys and values
print(list(studentMark)) # using a list, we can retrieve the kay
print(studentMark.keys())
print(studentMark.values())
