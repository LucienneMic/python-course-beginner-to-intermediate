from student import Student, StudentManager

manager = StudentManager()
manager.add_student("Alice", {"Math":90,"English":85})
manager.add_student("Bob", {"Math":75,"English":80})

for s in manager.students:
    print(s.name, s.grades)
