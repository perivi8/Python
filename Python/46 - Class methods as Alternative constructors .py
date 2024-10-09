
# class method as alternative constructor

# ex 1

class Student:
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll
    
    @classmethod
    def AlternateConstructor(cls, student_string):
        student_string = student_string.split("-")
        return cls(student_string[0], int(student_string[1]), int(student_string[2]))

Sam = Student("Sam", 18, 32)
Max = Student.AlternateConstructor("Max-19-22")

print(Sam.__dict__)
print(Max.__dict__)

print("\n")

# ex 2
class student :
  school = "hari"
  def __init__ (self , name , age):
    self.name = name
    self.age = age
  @classmethod
  def change (cls , string):

    
    name , age  = string.split("-")
    return cls(name , age)
    
    # or 

    string = string.split("-")
    return cls(string[0], string[1])



a = student("krishna",20)

# b = student("hk",89)      # wrong method
# b.change("krisshna1-30")

c = student.change("krisshna1-30")

# strimg = "ajay-66"                    # wrong Method
# d = student(string[0],string[1])



print(a.name)
print(a.age)
# print(b.name)
print(c.__dict__)
# print(d.__dict__)




