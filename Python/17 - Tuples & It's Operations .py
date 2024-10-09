#tuples

t1 = (3,4,56,7,6)
print(t1)
print(type(t1))
print(len(t1))
print(t1[1])
# t1[4] = 2      # it shows error

t2 = ("red","yellow","green",2,3,3,4,5,65,6)
print(t2[0])
print(t2[-3])
print(t2[2])
print(t2[-1])
print(t2[1])
print(t2[5:-3])
print(t2[:3])

t3  = (2,4,5,6,7,"red",78,234,45,"yellow",6)

#correct method
if "red"in t3:
  print("yes it is there")
else:
  print("no")

  #correct method
if "re"in "red":
  print("yes it is there")
else:
  print("no")

  #wrong method
if "re"in t3:
  print("yes it is there")
else:
  print("no")      #it shows no


#operation in tuples
#tuple are immutable 
# so first we have to convert the tuples into lists
# then we do same as list operationn

t4 = (2,3,4,5,5,6,5,7,6,5,6,5,6,5,6)
tup = list(t4)       #convert tuples into lists
tup.append("russia")    #add the element in last
print(tup)



t5 = (2,3,4,5,5,6,5,7,6,5,6,5,6,5,6)
tup = list(t5)  
tup.pop(2)               #remove item
print(tup)



t6= (2,3,4,5,5,6,5,7,6,5,6,5,6,5,6)
tup = list(t6)  
tup[0] = "india"       # change item
print(tup)


#count
tup3 = (3,5,7,87,5,3,3,6,5,5,4,5,3)
har = tup3.count(3)
print(har)


#index
tup3 = (3,5,7,87,5,3,3,6,5,5,4,5,3)
har = tup3.index(5)
print(har)


#length
tup3 = (3,5,7,87,5,3,3,6,5,5,4,5,3)
har = len(tup3)
print(har)


tup3 = (3,5,7,87,5,3,3,6,5,5,4,5,3)
har = tup3.count(3)
print(har)


tup3 = (3,5,7,87,5,3,3,6,5,5,4,5,3)
har = tup3.count(3)
print(har)