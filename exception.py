try:
    age = int(input("Enter your age: "))
    print(50/age)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Invalid Entry")
finally:
    print("Goodbye")