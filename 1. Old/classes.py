class Person:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
# returns Full name of person and email      
    def full_name(self): 
        return  self.first_name + (" ") + self.last_name
        
    def __str__(self):
        return self.full_name() + (" ") + ("Email") + (" ") + self.email

  

class Teacher(Person):
    def __init__(self, first_name, last_name, email, employee_number, room_number, subject_taught,
                 years_taught):
        super().__init__(first_name, last_name, email)
        self.employee_number = employee_number
        self.room_number = room_number
        self.subject_taught = subject_taught
        self.years_taught = years_taught
#retuns employee number      
    def __str__(self):
        return super().__str__() + (" ") + ("Employee Number") +str(self.employee_number) + (" ")\
            + ("Room Number") + (" ") + str(self.room_number) + (" ")\
            + ("Subject Taught") +(" ") + str(self.subject_taught) + (" ")\
            + ("Years Teaching") +(" ") + str(self.years_taught) +(" ")
    
    
class Student(Person):
    def __init__(self, first_name, last_name, email, age, grade):
        super().__init__(first_name, last_name, email)
        self.age = age
        self.grade = grade
#returns age
    def __str__(self):
        return super().__str__() + (" ") + ("Age") + (" ") + str(self.age) +(" ")\
            + ("Grade") + str(self.grade) 

class Faculty(Person):
    has_access = True

    def __init__(self, first_name, last_name, email, employee_number, years_worked):
        super().__init__(first_name, last_name, email)
        self.employee_number = employee_number
        self.years_worked = years_worked
#returns employee number
    def __str__(self):
        return super().__str__() + (" ") + ("Employee Number") + str(self.employee_number) + (" ")\
            +("Years Worked") + str(self.years_worked)


teacherList = [
    ("Rodney", "Hess", "rhess@school.com", 124, "B231", "History", 14),
    ("Gavin", "Belson", "gbelson@school.com", 186, "B230", "Economics", 6),
    ("Hannah", "Lynch",  "hlynch@school.com", 132, "B218", "Government", 2),
    ("Carley", "England", "cengland@school.com", 121, "B407", "Algebra", 7),
    ("Veronica", "Sanders",  "vsanders@school.com", 190, "B400", "Health", 8),
    ("Frank", "Collins",  "fcollins@school.com", 120, "B301", "Gym", 6),
    ("Denise", "Erikson","derikson@school.com", 175, "B242", "English", 8)
]

studentList = [
    ("Dean", "Jones",  "djones@school.com", 16, "10th Grade"),
    ("Mary", "Watts", "mwatts@school.com", 18, "12th Grade"),
    ("Allison", "Keller",  "akeller@school.com", 17, "11th Grade"),
    ("Mason", "Ingram",  "mingram@school.com", 15, "10th Grade"),
    ("Flynn", "White",  "fwhite@school.com", 15, "9th Grade")
]

# All employee numbers for faculty are a string and begin with F
facultyList = [
    ("Carrie", "Burton",  "cburton@school.com", "F001", 4),
    ("John", "Jameson",  "jjameson@school.com", "F002", 2),
    ("Peter", "Hendricks",  "phendricks@school.com", "F003", 1)
]
#creates dictionary of people
people = {}

teachers = []
for teacher in teacherList:
    teachers.append(Teacher(*teacher))
    
people["teacher"] = teachers
    
students = []
for student in studentList:
    students.append(Student(*student))
    
people["student"] = students

facultyMembers = []    
for faculty in facultyList:
    facultyMembers.append(Faculty(*faculty))

people["faculty"] = facultyMembers
   
for person in people:
    print(person)

    
def find_person_by_last_name_and_role(last_name, role):
    print('last_name:', last_name)
    print('role:', role)
    for person in people[role]:
        if person.last_name == last_name:
            return person
            
# takes in information        
role = input('Enter role: ')
last_name = input('Enter last name: ').title()
print(find_person_by_last_name_and_role(last_name, role))

