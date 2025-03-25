
class Student:

    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Sam", 20)
student2 = Student("Bob", 29)
student3 = Student("Kim", 28)

print(student2.name)
print(student2.age)
print(Student.class_year)

print(Student.num_students)

        