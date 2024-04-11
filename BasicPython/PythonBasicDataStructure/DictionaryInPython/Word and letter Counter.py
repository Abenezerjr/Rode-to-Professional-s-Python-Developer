# # counting in the text
#
# wordCounting = {}
# line = input('enter a line of text: ')
#
# words = line.split()
#
# print('Words:', words)
#
# print('Counting....')
#
# for word in words:
#     wordCounting[word] = wordCounting.get(word, 0) + 1
# print(wordCounting)

# counting a litter in the  world

letterCounter = {}

text = input('enter any text with out space: ')

textList = [char for char in text]
print(textList)

for letter in text:
    letterCounter[letter] = letterCounter.get(letter, 0) + 1
print(letterCounter)
