
# inheritance

# import the parent class into the child class

class employee:    # this is parent class
  def __init__ (self,name,id) :
    
    self.name = name
    self.id = id

  def showdetails(self): 
    print(f"the name of the employee is {self.name} and his id is {self.id}" )

  def parentlass(self):
    print('This is parent class')

class additionaldetails(employee): # This is child calss
  def child(self) :
    print("his  is  child telugu ")
    

a = employee("hari","821")
a.name="perivi"
a.showdetails()
a.parentlass()
# a.child()


b = additionaldetails("akhil",'1')
b.showdetails()
b.parentlass()
b.child()


# They arev five types of inheritance
  # 1 . single inheritance
  # 2 . multiple inheritance
  # 3 . multilevel inheritance
  # 4 . hierarchical inheritance
  # 5 . hybrid inheritance

