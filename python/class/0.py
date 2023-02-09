#!/usr/bin/python3


class Student:
    school = "freeCodeCamp.org"
    language = "python"

    def __init__(self, name, course):
        self.name = name
        self.course = course

Student1 = Student("Jane", "JavaScript")
Student2 = Student("John", "Python")

print(Student1.name) # Jane
print(Student2.name) # John
print(Student1.course, Student2.course)
#objects will inherit all the attributes of the class
#Each of these objects, by default, will have all the variables created in the class.
print(Student1.school, Student2.school)
print(Student1.language, Student2.language)
