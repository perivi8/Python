# instant vs class variable


# ex 1 normal variable

class student:
  def __init__(self,name,age):
    self.name = name
    self.age =age
  
  def details(self):
    print(f"The name of the student is {self.name} and his age is { self.age }")

a = student("hari", "20")
a.details()

a.name = "harikrishna"
a.details()

a1 = student("akhil", 22)
a1.details()




# Instant variable

class student1:
  def __init__(self,name,age):
    self.name = name
    self.age =age
    # self.sex_genger = male  # must use string
    self.sexgender = "male"  #This is instant variable  
    self.hisheight = 6      #  This is instant variable , no need string for numbers
    
  
  def details1(self):
    print(f"The name of the student is {self.name} and his age is { self.age } and his gender is {self.sexgender} and his height is {self.hisheight}")

b= student1("hari", 20)
b.details1()

b.name = "harikrishna"
b.details1()

b.sexgender = "female"   # we can change or edit the instant variables 
b.hisheight = 10
b.details1()



# class variable


class student2:

  favfood = "chickem"
  
  def __init__(self,name,age):
    self.name = name
    self.age =age
  
  def details(self):
    print(f"The name of the student is {self.name} and his age is { self.age } and his fav food is {self.favfood}")

c = student2("hari", "20")
c.details

c.name = "harikrishna"
c.details()

c1 = student2("akhil", 22)
c1.details()

c1.favfood = "mutton"  # we can edit or change the class variable
c1.details()


# another ex  for  class variable 

class student3:
  favgame = "free fire"
  noOfplayers = 0
  def __init__(self,name,age):
    self.name = name
    self.age =age
    student3. noOfplayers += 1 # this is used to increase the value  ( i.e., z = 1 ,  d = 2 , d1 = 3 , d2 = 4 and so on .......,) # we can use (+= , -= .*= ,/= )
    
  def details(self):
    print(f"The name of the student is {self.name} and his age is { self.age } his fav game is {self.favgame} and no of players { self.noOfplayers} ")


student3.favgame = "pubg"      # This is change the  d and d1 , d2 ,........., any variable

z = student3("sangeetham" , 24)
z.details()

z.favgame = 'BGMI'
z.details()

d = student3("hari", "20")
d.details()

d.name = "harikrishna"
d.details()

d1 = student3("akhil", 22)
d1.details()

d2 = student3("kk", 7)
d2.details()






