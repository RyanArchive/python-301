def get_exponential_value():
    for num in range(10):
        yield num ** num

exponential_value = get_exponential_value()
list_value = list(exponential_value)
print(list_value)

for value in get_exponential_value():
    print(value)