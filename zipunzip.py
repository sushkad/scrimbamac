
nums = '1234'
letters =['a','b','c','d','e']
names =['John','Eric','Michael','Graham','Joe']

combo = list(zip(nums,letters,names))
print(combo)


num , let , name = zip(*combo)

print(num , let, name)




