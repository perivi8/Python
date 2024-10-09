# CLASS METHOD   

# it is used to change or edit the class values
# when we print the ' print(obj.classvariable) ' , then the output will be change the class variable

# best example is Ex - 2 ( using @classmthod ) and Ex - 3 ( without @classmethod , but change the class method)


# ex 1
class student1 :
  school = 'vema'

  def __init__(self,name,age):
    self.name  = name
    self.age = age

  def details(self):
    print(f'{self.name},{self.age},{self.school}')

  # @classmethod
  def changeschool(cls,anotherschool):
    cls.school = anotherschool

b0= student1("hk" , 20)
# b0.school = "king"         # Don't change like this in @classmethod , If you change like this means it will change only one variable

b0.details()                 # output is vema


b= student1("hk" , 20)
b.changeschool("vema2")     # In this b variable only the school was changed as 'vema2'
b.details()


b1= student1("pk" , 39)
b1.details()                 # output is vema (because we are not using @classmethod ) 
b0.details()                 # output is vema (because we are not using @classmethod ) 

print(student1.school)       # output is vema (because we are not using @classmethod )  

print("\n")


print("\n")


# ex 2 ( own example )

class village :
  village = "chavali"
  mandal = "tirupathi"
  
  def __init__(self, name ,land) :
    self.name = name 
    self.land = land

  def details (self):
    print(f"The farmer name is {self.name} and he have {self.land} aceres land in {self.village} village and {self.mandal} mandal" )

  @classmethod
  def anothervillage(cls,village1,mandal1):
    cls.village = village1
    cls.mandal = mandal1
    
a = village("hari",10)
a.details()

a0 = village("sai",15)
a0.details()

a1 = village("akhil",20)
a1.details()

a1.anothervillage("nyp","nellore")
a1.details()

a2 = village("hyma",50)
a2.details()
a.details()     # output is nyp

print(village.village)   # Output is 'nyp'


#  Ex 3

class villagez :
  village = "chavali"
  mandal = "tirupathi"
  
  def __init__(self, name ,land) :
    self.name = name 
    self.land = land

  def details3 (self):
    print(f"The farmer name is {self.name} and he have {self.land} aceres land in {self.village} village and {self.mandal} mandal" )


villagez.village = 'bhadrabad'
villagez.mandal = 'haridwar'

z = village('sudheer' , 23)
z.details()
a.details()

print(villagez.village)
