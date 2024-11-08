# decorator

# It combine the Functions...

# Ex 1
def hari(fu):
    def perivi():
        print('x')
        fu()
        print('y')
    return perivi

@hari
def details():
    print("hello")

details() 

# or

def hari(fu):
    def perivi():
        print('x')
        fu()
        print('y')
    perivi()

@hari
def details():
    print("hello")

# Ex 2

def hii(nm):
    def func(x,y):
        print(f'x = {x}')
        print(f'y = {y}')
        nm()
        print(x+y)
    func(2,4)

@hii
def detail():
    print("bye")

# Ex 3
def my_decorator(func):
  def wrapper():
    print("hii")
    func()
    print("bye")

  return wrapper

@my_decorator
def do_that():
  print("hlo hari")


@my_decorator
def do_this():
  print("baby")


do_that()   # it is used when we use decorate
do_this()


# -------------------------------------------------------------------------------------


# if we use add or any method then above method will not work add *args ,**kwargs then it will work

def my_decorator1(func):
  def wrapper(*args ,**kwargs):  # just add *args ,**kwargs
    print("hii")
    func(*args ,**kwargs) # just add *args ,**kwargs
    print("bye")

  return wrapper

# @my_decorator1
def do_that1(a,b):
  print(a*b)


# @my_decorator1
def do_this1():
  print("baby")
 


my_decorator1(do_that1)(2,5) # it is used when we not use decorate in above
my_decorator1(do_this1)()

# or

do_that1(2,4)   # it is used when we use decorate
do_this1()

