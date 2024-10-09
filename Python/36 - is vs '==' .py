from typing_extensions import TypeVarTuple


a = "hari"
b = "hari"
c = True 

print(a==b==c)
# print(a=b)  # wrong method
print(a is b is c)
print(a is True)

print('--------------------------------------------------------------------------')

d = None
e = True

print(d==e)
print(d is e)

print('--------------------------------------------------------------------------')

f = True
g = True

print(f==g)
print(f is g)

print('--------------------------------------------------------------------------')

# Ex (LIST)

z  = [2 ,3 ,4]
z1 = [2 ,3 ,4]

print(z is z1)  # It will check the Location , Location is different for every list
print(z == z1)  # It will check the Model and Values

print('--------------------------------------------------------------------------')

# Ex (Tuple)

x  = (1 ,2 , 3)
x1 = (1 ,2 ,3)

print( x is x1)  # Tuples , immutable are  will create only time , and location will same
print(x == x1)   # Tuples , immutable are  will create only time , and location will same