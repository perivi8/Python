
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
    name = 'sangeetham'
    roll_no = '123456'
    clas = 'AI & DS'
    def __init__(self) :
        print(f'Hell {self.name} ,your Roll no is {self.roll_no} and your domain is {self.clas}')

y = details()


# ------------------------------------------------------------------------------------

#  Combine the Both means

class details1():
    # name = 'perivi'              # In constructor Don't write Here
    # roll_no = 'TMS6301'
    # clas = 'ML'
    
    def __init__(self , n , r , c) :
        self.name = n
        self.roll_no = r
        self.clas = c

        print(f'Hell {n} ,your Roll no is {r} and your domain is {c}')

    def info1(self):
        print(f'Helo Mr {self.name} , {self.roll_no}, {self.clas}')
    

x = details1('krishna' , 2068 , 'AI')
y = details1('perivi' , 8008 , 'DS')

x.info1()   # It is used to print the ' info1(self) '
y.info1()


print(x.name)
print(x.roll_no)
print(x.clas)



