arr = [1, 10, 20, -4, 45, -99, 99]

unique = set(arr)

unique.remove(max(arr))

second_largest = max(unique)

print(second_largest)