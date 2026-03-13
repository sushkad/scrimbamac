
word = "abcdefghijklmn"
def LongestWord(sentence):
    words = sentence.split()
    return max(words, key=len)


print(LongestWord("abcdefghijklmn"))




