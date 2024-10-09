# Super class

#  It is used to acces the Parent Class Data from Child Class

# Ex 1

class parent_class :
  def parentclass(self):
    print("this is an parent class ")

  def extraclass (self):
    print("this is an extra class ")


class child_class(parent_class):
  def childclass(self):
    print("this is an child class ")
    
    super().parentclass() 
    super().extraclass()

  def additionalclass(self , name , age):
    print(f'this is an additional class {name} , {age}')

    super().extraclass()

a = child_class()
a.childclass()
a.additionalclass('nani' , 15)

# a1 = parent_class()
# a1.parentclass()
# a1.extraclass()

      # or

a.parentclass()
a.extraclass()



print("\n")



# ex 2                             

class employee :
  def __init__(self , name , id):
    self.name = name
    self.id = id 

  
  def ajay (self):
    print(f"the candidate is {self.name} , and his id is {self.id} ")


class additionaldetails(employee):
  
  def __init__(self,name , id , lang):
    super().__init__(name , id )       # It will directly import the parent class , # No need to mention SELF
    self.lang = lang
    
  def hari(self):
    print(f'the name is {self.name} and id is  {self.id} and lang is {self.lang}')
   
    # or

    super().ajay()                   # It will directly import the parent class , # No need to mention SELF
    print(f'and lang is {self.lang}')


x = employee("sai",75)
print(x.name)
print(x.id)
x.ajay()


print("\n")


y = additionaldetails("krishna",20 , "tel")
y.hari()
print(y.name)
print(y.id)
print(y.lang)

    

