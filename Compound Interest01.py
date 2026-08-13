


p = 1000  # principle
r = 0.5  # rate
t = 3  # time in year

amount = p * (1 + r)**r
interest = amount - p

print(f"Interest Earned: {interest:.2f}")