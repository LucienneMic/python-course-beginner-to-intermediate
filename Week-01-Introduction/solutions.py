# Week 1 Solutions

# Exercise 1: Hello World
print("Hello, World!")

# Exercise 2: Variables and Types
x = 10        # int
y = 3.14      # float
name = "Alice" # string

print(x, type(x))
print(y, type(y))
print(name, type(name))

# Exercise 3: Simple Calculations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)

# Exercise 4: Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")
