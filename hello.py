def greet(name):
    return f"Hello, {name}!"

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(greet("Mark"))
print(factorial(5))
# This is a simple Python script that defines two functions: greet and factorial.
# The greet function takes a name as an argument and returns a greeting string.
# The factorial function takes a number as an argument and returns its factorial.
