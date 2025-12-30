# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."



friends = {'sushant','sid','nitin','sush','John'}
my_friends = {'Reg','Colin','John',}

cars = ['900','420','V70','996']

print('sid' in friends and 'John' in friends)
print(friends.intersection(my_friends))

print(my_friends.symmetric_difference(friends))

# print(friends.union(my_friends))
print(friends & my_friends)


cars_no_dupl = list(set(cars))
print(cars_no_dupl)