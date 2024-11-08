# yield    (generators)

# If we use return we got only one value
# If we are using YIELD means we will get all values , It will consume less memory , and read large files easily


# normal condition (return)

def generators():
  for i in range(15):
    return i

gen = generators()      
print(gen)   # out put = 0

print("---------------------------------------")

def generators1():
  for z in range(10):
    print(z)             # It will return all numbers in between range (0,1,2,3,4,5,6,7,8,9,none)

# gen1 = generators1()      
# print(gen1)            # If we are using print means then it show (0,1,2,3,4,5,6,7,8,9,none)
 
generators1()            # Directly we can call the function

print("---------------------------------------")

# But in Generators it print all the values upto range 


def generators2():
  for k in range(10):
    yield k

# generators2()            # It will not work in "YIELD" method

gen2 = generators2()      # this is very easy , and it calulate large nubers
print(gen2)
for k in gen2:
  print(k)     # out put = (0,1,2,3,.....8,9)



print("---------------------------------------")

# yield 
# in this method we can customise the values

def generate3():
  for m in range (7):
    yield m

gen3 = generate3()

print(next(gen3))     # it is also easy , but large numbers are difficult to calculate
print(next(gen3))
# print(next(gen3))   
print(next(gen3))
print(next(gen3))
print(next(gen3))
print(next(gen3))
# print(next(gen3))   # from this it show error
# print(next(gen3))
# print(next(gen3))




# In list / tuples  first we need to store after that it will return
#  Ex z = [1,2,3,4..............]
# But in Generators it will generate the values , without store the data(no need to write in list/tuples)