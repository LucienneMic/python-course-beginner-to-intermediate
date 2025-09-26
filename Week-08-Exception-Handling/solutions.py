# Week 8 Solutions

# Exercise 1
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a/b)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Exercise 2
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")

# Exercise 3
num = int(input("Enter a number: "))
if num < 0:
    raise ValueError("Negative number not allowed!")

# Exercise 4
def safe_div(a, b):
    try:
        return a/b
    except Exception as e:
        with open("errors.log", "a") as f:
            f.write(str(e)+"\n")
        return None
print(safe_div(10,0))
