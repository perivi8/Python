
#  constructors 

# they are two types of constructors
  # 1 = parametrized costructor 
  # 2 = default constructor



# 1 = parametried costructor 
class details1():
    def __init__(self , n , r , c) :
        self.name = n
        self.roll_no = r
        self.clas = c

        print(f'Hell {n} ,your Roll no is {r} and your domain is {c}')

    

x = details1('krishna' , 2068 , 'AI')
x = details1('maari' , 3456 , 'MBA')


# -------------------------------------------------------------------------------------------

# default constructor 

# Ex 1
class person2:
  def __init__(self):
    print("my name is akhil and my fav colour is red")
  
z = person2()
# x.info()     # no need to write this


# Ex 2
class details():

    def __init__(self) :
        self.name = 'sangeetham'
        self.roll_no = '123456'
        self.clas = 'AI & DS'
        print(f'Hell {self.name} ,your Roll no is {self.roll_no} and your domain is {self.clas}')

y = details()

# or
class hari :
    Name = "hari"
    roll_no = 206320014
    clas = "b.tech"
    def __init__ (self):
        print(f'{self.Name}{self.roll_no}{self.clas}')

a = hari()



#  ex 3
class hari1 :

    def info1(self):

      self.name = "hari"
      self.roll_no = 20648383
      self.clas = 'ECE'

      print(f'Hii mr {self.name} , {self.roll_no}')

b = hari1()
b.info1()


