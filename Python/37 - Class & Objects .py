class Details :
  name = "hari"
  rollno = "206320014"
  clas   = "b.tech"

a = Details()
print(a.name)
# or
print(Details.name)



# we can change or edit the details
class Details1 :
  name1 = "hari"
  rollno1 = "206320014"
  clas1   = "b.tech"

b = Details1()
b.name1 = "akhil"
print(b.name1,b.rollno1 , b.clas1)

# or

Details1.name1 ="akhil"
print(Details1.name1)


# ex 
  # if we use this method starting details will not consider  , only last details will cosider 

class list :
  name = "jdk"
  clas = "okdp"
  branch = "djndck"
  
  name = "ekmf"
  clas = "lkmva"
  branch = "mvoa"
  
  name = "klnmel"
  clas = "nfa;an"
  branch = "nedEJIO"
  
  name = "fnefefl"     # this one only will show 
  clas = "MLwow"
  branch = "avpoiam"  

# it will take only above the def remaing not will show
  
  
  def info1(self):
  
    print(f"my name {self.name} and my clas {self.clas} and my branch {self.branch}")

z = list() 
z.name = "hari"
z.clas  = "b.tech"
z.branch = "e.c.e"
z.info1()


# if we enter more data by using f'' string , then follow this method 

class krishna():
  name = "1"  # default
  post = "2"  # default

  def info2(self2):
    print(f"the {self2.name} is an {self2.post}")

m = krishna()
n = krishna()
o = krishna()

m.name = "hari"
n.name = "akhil"
o.name = "sai"

m.post = "king"
n.post = "magistrate"
# o.post = "warior"     # if we not enter it will take default value or character

# or
m.name = "hari"
m.post = "king"

n.name = "akhil"
n.post = "magistrate"

o.name = "sai"
# o.post = "warior"   # if we not enter it will take default value or character



m.info2()
n.info2()
o.info2()