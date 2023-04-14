def my_generator(n):
    value=0
    while value<n:
        yield value
        value+=2

for value in my_generator(50):
    print(value)