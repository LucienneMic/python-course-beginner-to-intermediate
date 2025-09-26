# Week 2 Solutions

# Exercise 1: Odd or Even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Exercise 2: Number Guessing Game
import random
secret = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
if guess == secret:
    print("Correct!")
else:
    print(f"Wrong! The number was {secret}")

# Exercise 3: Multiplication Table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# Exercise 4: Factorial Calculator
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")
