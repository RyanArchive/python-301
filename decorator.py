def my_decorator(func):
    def wrapper(num1, num2):
        print("Trying addition...")
        func(num1, num2)
        print("...Operation ends")
    return wrapper

@my_decorator
def add(num1, num2):
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")

add(15, 28)