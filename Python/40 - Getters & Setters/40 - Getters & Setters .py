# Getters and Setters 

#  Getters

# By using 'Getters' we can cnange the 'Parameter' condition. Once we change it apply every time

# But we can't Modify the Values or Names

# ex 1
class myclass:
  def __init__(self,name,age):
     self._name = name
     self._age = age
    
  
  @property
  def details1(self):
    return 'perivi ' + self._name  # We can modify the condition , But we Can't update *********

  @property
  def details2(self):
    return 10 + self._age  # We can modify the condition , But we Can't update
  
a = myclass("hari",10)  # (name , age)

# a.details1 = "kumar"    # we can not change the name or age in getters
# a.details2 = "28"

print(a.details1)    # must use print @property in Getters
print(a.details2)     # must use print @property in Getters

#  OR 

a = a.details1
print(a)


print('\n')


# ex 2
class myclass1:
  def __init__(self,name,age):
     self._name = name
     self._age = age
    

  def show(self):
    print(f"the name is {self._name}")
    print(f"the age is {self._age}")
 
  @property
  def details3(self):
    return self._name
    
  @property
  def details4(self):
    return self._age + 20   # We can modify the condition , But we Can't update
  
  

b= myclass1("hari1", 100)
c= myclass1("hari2", 20)

b.show()

print(b.details3)
print(b.details4)

c.show()

print(c.details3)
print(c.details4)


print('\n')
# ----------------------------------------------------------------------------------
print('\n')


# setters 

# ex 1
class myclass2:
  def __init__(self,name,age):
     self._name = name
     self._age = age
    
  def info(self):
    print(f'Heloo Mr - {self._name} nd your age was {self._age}')

  @property
  def value1(self):
    return self._name
   
  @value1.setter           # It will Help to 'Update' the Data
  def details1(self,newname):
    self._name = newname
    
    
  @property 
  def value2(self):
    return self._age

  @value2.setter            # It will Help to 'Update' the Data
  def details2(self,newage):
    self._age = newage
  
  

c = myclass2("hari3", 8888)
c.info()

# c.value1 = 'kondari'     # It show error because this function is Not belongs to -  ' SETTER '
# c.value2 = '23'

c.details1 = "sangeetham"
c.details2 =  8106


print(c.details1)
print(c.details2)

c.info()


print('\n')


#ex 2
class myclass3:
  def __init__(self,name1,age1):
     self._name1 = name1
     self._age1 = age1
    
  
  @property
  def value3(self):
    return self._name1

  @value3.setter                   # It will Help to 'Update' the Data
  def details3(self,newname1):
    self._name1 = newname1
    
    
  @property
  def value4(self):
    return self._age1

  # @value4.setter                 # It will Help to 'Update' the Data
  # def details4(self,newage1):
  #   self._age1 = newage1
  
  

d = myclass3("perivi",10000)

d.details3 = "krishna1"
# d.details4 = "2888"     # it will not work when we not use setter

print(d.details3)
# print(d.details4)
