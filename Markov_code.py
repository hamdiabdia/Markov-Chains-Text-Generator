# import required packages
import numpy as np

# Load the data set
shrek = open('shrek.txt', encoding='utf8').read()

# print(shrek)

# Split the data set into words
list_of_words = shrek.split()
print(list_of_words)

# Create pairs to keys
def make_pairs(list_of_words):

    for i in range(len(list_of_words) - 1):
        yield (list_of_words [i], list_of_words[i + 1])


pairs = make_pairs(list_of_words)

#Appending the dictionary
word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

#Build the markov model
first_word = np.random.choice(list_of_words)

while first_word.islower():
    first_word = np.random.choice(list_of_words)

chain = [first_word]

n_words = 20

for i in range (n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

#Predictions
a = (' '.join(chain))
#print(a)
string = a.replace("-", "")
print(string) # result: "abcdef"

list_of_chars = ['{', '}', '-']
for character in list_of_chars:
    string= a.replace(character, '')
print(string + ".")
