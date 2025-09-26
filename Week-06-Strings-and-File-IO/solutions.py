# Week 6 Solutions

# Exercise 1
s = "Python"
print(s[::-1])
print(sum(1 for c in s if c.lower() in "aeiou"))
print(s.upper())

# Exercise 2
with open("sample.txt", "w") as f:
    f.write("Hello world from Python\nThis is a test file.")
with open("sample.txt", "r") as f:
    text = f.read()
words = text.split()
print("Word count:", len(words))

# Exercise 3
import csv
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name","Age"])
    writer.writerow(["Alice",30])
    writer.writerow(["Bob",25])
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Exercise 4
with open("log.txt", "a") as f:
    user_input = input("Enter text to log: ")
    f.write(user_input + "\n")
