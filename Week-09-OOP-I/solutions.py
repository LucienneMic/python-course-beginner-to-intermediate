# Week 9 Solutions

# Exercise 1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s = Student("Alice", 20)
s.display()

# Exercise 2
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount()
acc.deposit(100)
acc.withdraw(30)
acc.show_balance()
