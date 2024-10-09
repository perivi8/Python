

class parent_class:
  def __str__ (self):
    return "hlo this is parent 1"
  def parent(self):
    print("this is an part of parent class ")

  def good (self):
    print("i am a good boy")


class child(parent_class):
  def __str__(self):
    return "hlo this is an child class"

  def child(self):
    print("this is an part of child class")

  def good (self):
    print("i am a bad boy")


a = child()
print(a)
a.parent()
a.child()
a.good()   

print("\n")

b = parent_class()
b.good()