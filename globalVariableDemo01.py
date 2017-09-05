# Changing a global variable inside a function
# NOTE: some consider this a harmful practice

students = []  # an empty list of students

studentCount = 0

def makeStudent(name,perm):
    thisStudent = {}
    thisStudent["name"]=name
    thisStudent["perm"]=perm
    return thisStudent

def addStudent(name,perm):
    newStudent=makeStudent(name,perm)
    # students = students + [newStudent]
    students.append(newStudent)
    global studentCount
    studentCount = studentCount + 1
    

