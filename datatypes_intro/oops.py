# l=[1,2,3]
# l.append(100)
# print(l)
class student:
    def __init__(self, first_name, last_name,courses): #methods
      self.first_name=first_name     #datamembers,attributes
      self.last=last_name
      self.course=courses
      print(self.print_name)
      print(self.courses)
    def print_name(self):     #behaviour
        return self.first_name+" "+self.last
        return full_name
courses_1=["python","java","c++"]
courses_2=["webdesign","sap",".net"]
mahi=student(first_name="mahendra",last_name="perugu",courses_1)
divya=student(first_name="divya",last_name="k",courses_2)
print(divya.first_name)
print(divya.print_name())
print(mahi.first_name)
print(mahi.print_name())
print(student.print_name(mahi))
# class student:
#     pass
# student_obj_2=student()
# print(student_obj_1)
# student_obj_1=student()
# print(student_obj_2)