# Hierarchical INheritance

# ex 

class human :
  def display (self):
    print("They have alive")

class man (human):
  def display1(self):
    print("he can do job")

class women(human):
  def display2(self):
    print("she can do every work")

m =women()
m.display()
# m.display1()
m.display2()


n = man()
n.display()
n.display1()
# n.display2()
