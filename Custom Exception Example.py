

class AgeException(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeException("Age is less than or equal to 18")

    print("You are Eligible")

except AgeException as e:
    print("Custom Error:", e)