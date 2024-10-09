# Hybrid Inheritance

 # ex 1
class a :
  def display (self):
    print("this is a class")

class b(a):
  def show (self):
    print("this is an b class")

class c:
  def display(self):
    print("this is an c class")

class d (b,c):
  def display1(self):
    print("this is an d class")
 
#   def display(self):               # If we write here means then it will choose this one 
#     print('This is d classs')
  

obj = d()
obj.show()
obj.display()  # output is = ' this is a class '

print("--------------------------------------")


# ex 2
class parent :
  def __init__ (self , name , age ):
    self.name = name 
    self.age = age

  def show(self):
    print(f"The name iss {self.name} and his age is {self.age}")

class parent1(parent):
  def __init__(self,name , age , id ):
    parent.__init__(self ,name, age)
    self.id = id

  def display (self):
    print(f'the id is {self.id}')

class parent2 :
  def __init__ (self):
    pass
  def display(self):
    print("this is an parent2 class")

class child(parent1,parent2):
  def __init__ (self , name ,age, id):
    self.age = age
    self.name = name
    self.id = id
    
  def show1(self):
    print(f"the name is {self.name} and his id is {self.id}")

    
k = child("hari",20 ,206320014)
k.display() 
k.show()


