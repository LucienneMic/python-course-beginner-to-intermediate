class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades else {}

class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self, name, grades):
        self.students.append(Student(name, grades))
    def remove_student(self, name):
        self.students = [s for s in self.students if s.name!=name]
    def get_average(self, name):
        for s in self.students:
            if s.name==name:
                return sum(s.grades.values())/len(s.grades)
