class Person:
    def __init__(self, first_name, last_name, full_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.email = email


class Teacher(Person):
    def __init__(self, first_name, last_name, full_name, email, employee_number, room_number, subject_taught,
                 years_taught):
        super().__init__(first_name, last_name, full_name, email)
        self.employee_number = employee_number
        self.room_number = room_number
        self.subject_taught = subject_taught
        self.years_taught = years_taught


class Student(Person):
    def __init__(self, first_name, last_name, full_name, email, age, grade):
        super().__init__(first_name, last_name, full_name, email)
        self.age = age
        self.grade = grade


class Faculty(Person):
    has_access = True

    def __init__(self, first_name, last_name, full_name, email, employee_number, years_worked):
        super().__init__(first_name, last_name, full_name, email)
        self.employee_number = employee_number
        self.years_worked = years_worked


teacherList = [
    ("Rodney", "Hess", "Rodney Hess", "rhess@school.com", 124, "B231", "History", 14),
    ("Gavin", "Belson", "Gavin Belson", "gbelson@school.com", 186, "B230", "Economics", 6),
    ("Hannah", "Lynch", "Hannah Lynch", "hlynch@school.com", 132, "B218", "Government", 2),
    ("Carley", "England", "Carley England", "cengland@school.com", 121, "B407", "Algebra", 7),
    ("Veronica", "Sanders", "Veronica Sanders", "vsanders@school.com", 190, "B400", "Health", 8),
    ("Frank", "Collins", "Frank Collins", "fcollins@school.com", 120, "B301", "Gym", 6),
    ("Denise", "Erikson", "Denise Erikson", "derikson@school.com", 175, "B242", "English", 8)
]

studentList = [
    ("Dean", "Jones", "Derrick Jones", "djones@school.com", 16, "10th Grade"),
    ("Mary", "Watts", "Mary Watts", "mwatts@school.com", 18, "12th Grade"),
    ("Allison", "Keller", "Allison Keller", "akeller@school.com", 17, "11th Grade"),
    ("Mason", "Ingram", "Mason Ingram", "mingram@school.com", 15, "10th Grade"),
    ("Flynn", "White", "Flynn White", "fwhite@school.com", 15, "9th Grade")
]

# All employee numbers for faculty are a string and begin with F
facultyList = [
    ("Carrie", "Burton", "Carrie Burton", "cburton@school.com", "F001", 4),
    ("John", "Jameson", "John Jameson", "jjameson@school.com", "F002", 2),
    ("Peter", "Hendricks", "Peter Hendricks", "phendricks@school.com", "F003", 1)
]

# This prints out the student in the 0 index of the list and the next argument prints out the specific index of
# the student you want, like if you wanted the grade, you would have the second argument [5]
print(studentList[0][5])

# Giving each class an example of a person that would inhabit the position
teacher1 = Teacher("Rodney", "Hess", "Rodney Hess", "rhess@school.com", 124, "B231", "History", 14)
student1 = Student("Dean", "Jones", "Derrick Jones", "djones@school.com", 16, "10th Grade")
faculty1 = Faculty("Carrie", "Burton", "Carrie Burton", "cburton@school.com", "F001", 4)

# Examples of attributes being printed
print(teacherList[0])
print(teacher1.full_name)
print(teacher1.employee_number)
print(teacher1.years_taught)

# print(student1.age)
# print(faculty1.employee_number)


# print(help(Teacher))
