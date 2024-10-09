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
hari = lambda x : x*x*3
print(hari(2))  # out put is 12


# ex 5 create a mutipication table
#previous mutipication table is in screen shot 51

a = lambda x , y : (f"{x} x {y} = {x *y}")
for y in range(1,11):
  print(a(2,y))


# ex 6
b = lambda x ,y,z : (x + y+ z ) / 3
print(b(3,4,5))

