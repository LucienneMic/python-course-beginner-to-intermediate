# Week 5 Solutions

# Exercise 1
phonebook = {"Alice": "123", "Bob": "456", "Charlie": "789"}
for name, number in phonebook.items():
    print(name, number)

# Exercise 2
set1 = {1,2,3}
set2 = {2,3,4}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Exercise 3
students = {
    "Alice": {"Math":90, "Science":85},
    "Bob": {"Math":75, "Science":80}
}
for student, grades in students.items():
    avg = sum(grades.values())/len(grades)
    print(student, "average:", avg)

# Exercise 4
nums = [1,2,2,3,4,4,5]
unique_nums = list(set(nums))
print(unique_nums)
