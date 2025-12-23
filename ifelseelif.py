
is_cold = True
is_raining = False
print("Good Morning")

if is_raining and is_cold:
    print("Raining and Jacket")

elif is_raining and not (is_cold):
    print("Bring Umbrella")
elif not(is_raining) and is_cold:
    print("Jacket")
else:
    print("Umbrella")

