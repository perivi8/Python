# Operator Overloading

# __add__
# __sub__
# __mul__
# __gt__
# __lt__


print("----------------------------------------")

class krishna :
  def __init__ (self,m):
    self.m = m

  def __str__(self):
    return f" it is  {self.m} "

  def __sub__(self,k):
    return self.m + k.m  # we can use (+ , - , * , / , < , >) 
                         # the all types are support in every dunder method
    # return self.m - k.m
    # return self.m * k.m
    # return self.m / k.m
    # return self.m > k.m
    # return self.m < k.m 

a1 = krishna(3)
a2 = krishna(4)

print(a1)
print(a2)

print(a1-a2)   # must have same ( i.e., __add__ = (a1+a2))
                             #  ( i.e., __sub__ = (a1-a2)) like this

print("---------------------------------------")

class hari :
  def __init__(self , x , y):
    self.x = x
    self.y = y

  def __str__ (self):
    return f" x is {self.x} and y is {self.y}"

  def __sub__ (self , z):
    return f"{self.x + z.x } + {self.y+z.y}  = {(self.x +z.x)+(self.y +z.y)}"  # The condition is our wish

   
     
a = hari(2,4)
b = hari(5,6)
c = hari(10 , 20)
print(a)
print(b)

print(b-c)  # This one satisfy the operator 
# print(a*b)


