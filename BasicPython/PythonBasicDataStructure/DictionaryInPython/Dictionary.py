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
easier to find values."""

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
