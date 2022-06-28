class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


class Teacher(Person):
    def __init__(self, first_name, last_name, email, employee_number, room_number):
        super().__init__(first_name, last_name, email)
        self.employee_number = employee_number
        self.room_number = room_number


class Student(Person):
    def __init__(self, first_name, last_name, email, age, grade):
        super().__init__(first_name, last_name, email)
        self.age = age
        self.grade = grade


class Faculty(Person):
    has_access = True

    def __init__(self, first_name, last_name, email, employee_number):
        super().__init__(first_name, last_name, email)
        self.employee_number = employee_number


# Giving each class an example of a person that would inhabit the position
teacher1 = Teacher("Ben", "Parker", "ben@school.com", 789, "B132")
faculty1 = Faculty("Randy", "Smith", "rsmith@school.com", 185)
student1 = Student("Ben", "Parker", "ben@school.com", 16, "10th Grade")

# Examples of attributes being printed
print(teacher1.first_name)
print(faculty1.employee_number)
print(student1.age)

# print(help(Teacher))
