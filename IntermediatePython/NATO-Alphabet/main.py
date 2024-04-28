import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
out_put = [phonetic_dict[letter] for letter in word]
print(out_put)
