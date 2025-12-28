

names = ['sush','SID','lad']
names1 = ['Shwan','TERRY','terry jones']


msg = 'You are invited on sunday class'

#names.extend(names1)
names += names1
for index in range(2):
    names.append(input('Enter a new name: '))


for name in names:
    msg1 = f'{name.title()} ! {msg}'
    print(msg1)


