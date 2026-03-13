from collections import Counter



words = ['apple', 'banana', 'orange', 'grape', 'apple', 'banana']


word_count =Counter(words)

most_common = word_count.most_common(1)

print(most_common)