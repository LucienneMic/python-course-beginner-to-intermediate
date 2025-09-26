# Week 12 Solutions

# Exercise 1
def add(a,b):
    return a+b
assert add(2,3)==5

# Exercise 2
def subtract(a,b):
    return a-b
assert subtract(5,3)==2

# Exercise 3
def is_palindrome(s):
    return s==s[::-1]
assert is_palindrome("racecar")==True
assert is_palindrome("hello")==False
