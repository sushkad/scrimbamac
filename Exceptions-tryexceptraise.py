
try:

    num = int(input("Enter a number: "))
    print("30 divided by",num, "is: ",30/num)

    if num > 30:
        raise TypeError("That is: ",num)
    
except ZeroDivisionError as err:
    print("You can't divide by zero")

except ValueError as err:
    print("You can't divide by zero")

finally:
    print("** Thank you for playing!**")