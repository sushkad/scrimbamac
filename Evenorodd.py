from selectors import SelectSelector

num  = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Max and Min


numbers = [ 34,10,89,100,405]

hig = max(numbers)
low = min(numbers)

print(f"max {hig} , min {low} ")



# Palindrome

def is_palindrome(word):
    return word == word[::-1]   # reverse the string and compare


print(is_palindrome("radar"))
print(is_palindrome("Python"))

