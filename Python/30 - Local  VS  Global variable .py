# Local vs Global variable

#  in thios method we can change the global variable 

# ex 1

x = 4  # Global variable 
print(x)

def hari():
  y = 5    # Local variable
  print(y)

hari()  #compulsary we need to enter , what we enter in def
print(x) # out put is 4 
# print(y)  # it show an error because x is an global  variable and y is the local variable






# ex 2

m = 6
print(m)

def krishna():
  global m
  m = 1
  n = 7

krishna()

print(m) #out put is 1
# print(n) #print(n) shows an error because only m is global variable and n is local varable
