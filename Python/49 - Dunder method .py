

# __init__

class hari1 :
  
  def __init__(self , name , age ):
    self.name = name
    self.age = age

a = hari1("krishna",20)
print(a)      # output is <__main__.hari1 object at 0x7fb9debe7e80> like this
print(a.name)
print(a.age)


# -----------------------------------------------------------------------------------------

# __str__

#  https://youtu.be/POTRSwwTPYU   ( for reference video link )

# it run individual objects

# ex 1
class hari2a :
  
  def __str__(self):
    return "good boy"
    # print("good boy")     # print type not support , only it support return type

b = hari2a()
print(b)    # output is good boy   



# ex 2
class hari2b :

  def __init__(self , name , age ):
    self.name = name 
    self.age = age 
     
  def __str__(self):
    return f"The {self.name} is an good boy and his age is {self.age}"

c = hari2b("ajay",19)
print(c)


print("\n")



# ------------------------------------------------------------------------------------------

# __repr__

# it run group of individual objects

# individual objects first preority is __str__

# if we have  individual objects  , but __str__ is not there means then it will  run in __repr__

#  Group of individual objects only work in __repr__ 

class hari3 :

  def __init__(self , name , age ):
    self.name = name 
    self.age = age 
     
  def __repr__(self):
    return f"The {self.name} is an good boy and his age is {self.age}  repr \n"
      # print type not support

  def __str__(self):
    return f"The {self.name} is an good boy and his age is ('{self.age}' )str \n"
        # print type not support
  


      # individual objects
d = hari3("vijay",19)
e = hari3("sudheer",30)

       # Group of individual objects
hari3list = [hari3("hari1",31),
             hari3("hari2",32), 
             hari3("hari3",33)
]


print(d)               # it will run in __str__ 
print(e)               # it will run in  __str__
 
print(hari3list)       # it will run in __repr__


print("\n")


# ----------------------------------------------------------------------------------------


# __call__


# ex 1

class hari4:
  def __call__(self):
    print("very bad boy")
    # return "very very bad boy"          # return type will not support

f = hari4()
f()

# ex 2

class hari4b:
  def __init__(self,place):
    self.place = place

  def __call__(self):
    print(f"the hari birth place is {self.place}")
     # if we can comment above 2 lines then output is in red colour , and it shows the object is not callable 


g = hari4b("chavali")
g()


# ---------------------------------------------------------------------------------------

# __len__  


class employee :
  def __init__(self , author ,book , pages):
    self.author = author
    self.book =book
    self.pages = pages

  def __len__(self):    # If we are not use __len__ means then it show error 
    return self.pages
  
z = employee('Alex' , 'google' , 32581)
print(len(z))      # must have same ( i.e., __len__ = len(z))
