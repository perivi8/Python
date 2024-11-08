#dir, __dict__ and help method

# dir

#  It is used to show the our given input what type of methods it support   

a = (1,2,3)
print(dir(a))


print("\n")


# __dict__
class hari :
  def __init__ (self , name , age):
    self.name = name 
    self.age = age

a1 = hari("krishna",20)
print(a1.__dict__)


print("\n")




# help method
class hari1 :
  def __init__ (self , name , age):
    self.name = name 
    self.age = age

a2 = hari1("krishna",20)
print(help(a2))      # Below have the reason for  print(help(a2)) 

 # when we run the program it will normally work , but when we use the help() function then output will show only the help functin , remaining [ dir() , __dict__ ] 



# Reference Link :- https://youtu.be/K3cTEULY24A





