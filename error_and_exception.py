age = input("Enter your age: ")

try:
    age = f"Your age is {int(age)}"
except ValueError:
    age = "Invalid age"

print(age)