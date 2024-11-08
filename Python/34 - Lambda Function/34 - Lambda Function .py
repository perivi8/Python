# lambda function 
# this function  is only used for to short the lines 

# ex 1 ( normal method )
def hari(x):
  return x * 2
print(hari(2))

# ex 2 ( lambda method )

krishna = lambda a : a * 2
print(krishna(4))

# ex 3 
cube = lambda x : x*x*x
print(cube(5))


# ex 4
hari1 = lambda x : x*x*3
print(hari1(2))  # out put is 12


# ex 5 create a mutipication table
#previous mutipication table is in screen shot 51

a = lambda x , y : (f"{x} x {y} = {x *y}")
for y in range(1,11):
  print(a(2,y))

# or

for i in range(1,11):
    a = lambda x , i : f'{x} X {i} = {x*i} '
    print(a(3,i))

# or

for i in range(1,11):
    a = lambda x , i : print(f'{x} X {i} = {x*i} ')
    a(3,i)

# Normal Function method 

def func(n):
    for j in range (1,12):
       print(f'{n} X {j} = {n*j} ')
func(5)

# or

def func():
    n = int(input("Enter Number"))
    for j in range (1,12):
       print(f'{n} X {j} = {n*j} ')
func()


# ex 6
b = lambda x ,y,z : (x + y+ z ) / 3
print(b(3,4,5))

