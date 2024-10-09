# Method Overriding

# ex 1
class hari1 :
  def __init__(self , name , age):
    pass

  def height ( self ):
    print("height :" , 5.8)

  def weight (self):
    print("weight is ", 70)

class hari2(hari1):
  
  def height ( self ):           # We need to give the same function name as a parent class , then only it will override
    print("height :" , 6.0)   

  def weight (self):             # We need to give the same function name as a parent class , then only it will override
    print("weight is ", 80)

x = hari2("hari",20)
x.height()
x.weight()



print("--------------------------------------")


class length :
  
  def __init__ (self,x, y) :
    self.x = x
    self.y = y

  def area (self):
    print(self.x * self.y)

a = length(2,3)
a.area()

class length2(length):
  def __init__ (self ,x ,y, z):
    super().__init__ (x , y)
    
    self.z = z

  def area (self):             # We need to give the same function name as a parent class , then only it will override
    print(self.x * self.y *self.z)
  


b = length2(2,3,3)
b.area()



print ( "----------------------------------------")


class pubg1:
  def __init__(self,x , y):
    self.x = x
    self.y = y

  def game2 (self ):
    print(self.x + self.y)

class freefire1(pubg1):
  def __init__ (self,z):
    self.z  = z
    
    super().__init__(z , z)      #  We are Changing the X , Y  as Z

  def game2 (self ):          # We need to give the same function name as a parent class , then only it will override
    print(self.x + self.y+self.z)

m = freefire1(6)
m.game2()    

 



print("------------------------------------")



class pubg:
  def __init__(self,player , id , place):
    self.player= player
    self.id = id
    self.place = place

  def game1 (self ):
    print(f"the name of the player is {self.player} and id is {self.id} his place is {self.place}")

class freefire(pubg):
  def __init__ (self,level):
    self.level  = level
    super().__init__(level ,level , level) 

m = freefire("king")
m.game1() 




# Referrence Link :- https://youtu.be/hlC6deOQOMc [Telugu]

# Referrence Link :- https://youtu.be/46_yfYC36JY [Hindi]