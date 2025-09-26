# Week 4 Solutions

# Exercise 1
numbers = [2, 5, 8, 3, 7]
print("Sum:", sum(numbers))
print("Average:", sum(numbers)/len(numbers))

# Exercise 2
numbers.append(10)
numbers.remove(3)
numbers.sort()
print(numbers)

# Exercise 3
tup = (1, 2, 3, 4)
for item in tup:
    print(item)

# Exercise 4
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
