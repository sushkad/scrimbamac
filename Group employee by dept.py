


emp = {"rahul": "HR" , "Amit":"HR", "Siddesh":"IT","Sushant":"QA" }



dict = {}

for e , d in emp.items():

    dict.setdefault(d,[]).append(e)

print(dict)


print(bool("False"))

print( 0 or 27)

x = None
print(type(x))

add = lambda x , y: x + y