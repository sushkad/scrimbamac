
print('python101 - Enumerate')
friends =['sush','sid','sam']
efriends =['max','clark','jhonson']

#i = 51
#for friend in friends :
#    print(i,friend)
#    i = i + 1

for num ,friend in enumerate (friends,51) :
    print(num,friend)
for friend in enumerate (friends,5) :
    print(friend)
for friend in (enumerate (friends,51),-100) :
    print(friend)

for num ,lettter in enumerate ('python',start= 5):
    print(num,lettter)

print(type(enumerate(friends)))
print(list(enumerate(friends)))