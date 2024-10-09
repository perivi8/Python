
# multi level Inheritance
class father :
  def __init__ (self, name , age) :
    self.name = name
    self.age = age 

  def fatherdetails (self):
    print(f"My father name is {self.name} and his age is {self.age}")



class mother(father):
  def __init__ (self,name,age ,village):
    father.__init__(self,name,age )
    self.village = village

  def motherdetails(self):
    print(f"my mother name is {self.name} and she age is {self.age} village is {self.village}")



class child(mother):
  def __init__(self , name , age , village , surname ):
    mother.__init__(self , name  , age , village )
    self.surname = surname

  def childdetails(self):
    print(f"my name is {self.name} and my age is {self.age} and my village is {self.village} and my surname is {self.surname}" )

a = child("hari",20,"chavali" , "perivi")
a.childdetails()

b = mother("hyma",45 , "chavali")
b.motherdetails()

c = father("krishnaiah",50)
c.fatherdetails()
 
