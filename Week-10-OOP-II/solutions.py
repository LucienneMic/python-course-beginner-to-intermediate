# Week 10 Solutions

# Exercise 1
class Employee:
    def __init__(self, name):
        self.name = name
    def role(self):
        print("Employee")

class Manager(Employee):
    def role(self):
        print("Manager")

m = Manager("Alice")
m.role()

# Exercise 2
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private
    def get_balance(self):
        return self.__balance
    def set_balance(self, amount):
        self.__balance = amount

acc = BankAccount(100)
print(acc.get_balance())
acc.set_balance(200)
print(acc.get_balance())
