

from collections import Counter

#Removing Duplicates

numbers = [1,2,2,3,4,4,4,5]

#convert to set and back to list

unique_numbers = list(set(numbers))

print(unique_numbers)

# First Non repeat characters

text = "aabbccdeff"

#count every character

counts = {}
for char in text:
    counts[char] = counts.get(char,0) + 1

# # Find the first one with a count of 1

for char in text:
    if counts[char] ==1:
        print(f"First Unique: {char}")
        break

# Counting Occurrences


data = [1,2,2,3,3,3]

# Create a frequency map

tally = Counter(data)

print(tally)

