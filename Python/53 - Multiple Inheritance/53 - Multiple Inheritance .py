
class parent_class1 :
  def __init__(self , name , age):
    self.name = name 
    self.age = age 
    
  def show (self):
    print(f"The name is {self.name} and his age is {self.age }")



class parent_class2:
  def __init__(self , id ) :
    self.id = id 
    
  def show1 (self):
    print(f"The user id is {self.id}")



class parent_class3(parent_class1,parent_class2):
  def __init__(self,name,age,id , clan):   # we need must enter above classes , add we can add extra also
    self.name = name
    self.age = age
    self.id = id
    self.clan = clan

  def agerestriction(self):
    if self.age > 19:
      print("eligible")

    else :
      print("not eligible")
    
  
  def show3 (self):
    print(f"THE NAME IS {self.name} AND ID IS {self.id} AND AGE IS {self.age} AND HIS CLAN IS {self.clan}")

a = parent_class3("hari", 20 , 815003420 , "D.C")
print(a.name)
print(a.id)
print(a.age)

print("----------------------")

a.show()
a.show1()
a.show3()
a.agerestriction()