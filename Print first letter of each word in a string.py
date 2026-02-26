
from collections import Counter

string = "Sushant kadam"

first_letters = ''.join([word[0] for word in string.split()])
print("First letter of each word:", first_letters)