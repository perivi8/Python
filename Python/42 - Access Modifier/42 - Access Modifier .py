# Access Modifiers 
# They are 3 types of modifiers

 # Public Access Modifier
 # Private Access Modifier   
 # protected Access Modifier 


#  Public Access Modifier   

# ex 1
class student:
  def __init__ (self,name,age):
    self.name = name
    self.age = age

  def details(self):
    print(f"the name of the student is {self.name} and his age is {self.age}")

a = student("hari","21")
a.details()  
a.name= 'akhil'
print(a.name)
print(a.age)


# --------------------------------------------------------------------


# Private Access Modifier    

 # ex 1 (Recommended)
class student1:
  def __init__ (self,name,age):
    self.__name = name  # Private Access
    self.__age = age


b = student1("hari1","211")

# print(b.__name)  # it will not work in private access method
# print(b.__age)

print(b._student1__name)    # This will work
print(b._student1__age)

# OR

# ex 2
class student2:
  def __init__ (self,name,age):
    self.__name = name
    self.__age = age
    

  def details1(self):
    print(self.__name)
    print(self.__age)
    
c = student2("hari2","212")
c.details1()

# print(c.__name)  # it gives error  , Atribute Error

print(c._student2__age)

# ----------------------------------------------------------------------------



# protected Access modifier

class student3:
  def __init__ (self,name,age):
    self._name = name
    self._age = age
  
  def _perivi(self):       # Protected Method
    return 'Hello Hari ! How are you !'


d = student3("hari3","213")
print(d._name)
print(d._age)
print(d._perivi())


