# Week 7 Solutions

# Exercise 1
import math
print(math.sqrt(16))
print(math.factorial(5))

# Exercise 2
import random
for i in range(5):
    print(random.randint(1, 100))

# Exercise 3
# custom_module.py
def greet(name):
    print(f"Hello, {name}!")
# In main.py
import custom_module
custom_module.greet("Alice")

# Exercise 4
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
