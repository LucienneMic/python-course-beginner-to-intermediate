# Week 3 Solutions

# Exercise 1
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Exercise 2
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print(add(5, 3))
print(subtract(5, 3))
print(multiply(5, 3))
print(divide(5, 3))

# Exercise 3
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))

# Exercise 4
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))
