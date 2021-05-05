class student(object):
    def __init__(self,name,age,gender,level,grades = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades
    def setGrade(self,course, grade):
        self.grades[course] = grade
    def getGrade(self,course):
        return self.grades[course]
    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)
john = student("John",12,"male",6,{"math":3.3})
jane = student("Jane",11,"female",5,{"science":3.1})
print(john.getGPA())
print(jane.getGPA())
