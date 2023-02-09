class student:

    #pass
    sname = "sname"
    fname = "Ayo"
    Age = 15
    try:
        if not isinstance(Age, int):
            raise ValueError("Age must be an integer")
    except NameError:
        pass
    def __init__(self, name, course):
        self.name = input("Enter name: ")
        self.course = input("Enter course: ")

#Student1 = student(name, course)
#Student2 = student()
Student3 = student("Ade", "gbite")

print(Student3.course)
print(Student3.name)
print(Student3.Age)

#print(Student2.sname)
#print(Student2.fname)
#print(student.self.course)
#print(student3.name, student3.course)
