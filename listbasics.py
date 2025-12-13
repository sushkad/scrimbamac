

friends = ['sushant','kadam','siddesh','lad','nitin']
print('friends: ', friends)

print(friends[2],friends[4])

print(friends[:])
print(friends[:-2])


print(friends.count('sushant'))
print(friends.count('kadam'))


# Sorted

friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)