#introduction to lists
#lists

a1 = ["apple","banana","2","goa",  5]
#      [0]     [1]     [2]   [3]  [4]       #indexing
#     [-5]    [-4]    [-3]  [-2]  [-1]      #negitive index
print(a1[4])
print(a1[-4])
print(a1[3-4])  #3-4 = -1
print(len(a1))
print(a1[len(a1)-3])
#we can change after a print
a1[1] = 8
print(a1)


# if and else in list

# correct method
a2 = ["hari","akhil","perivi",8]
print(a2)
if 8 in a2 :
  print("yes")
else:
  print("no")

  
#correct method
# ex 1
if "ari"in "hari" :
  print("yes")
else:
  print("no")

# ex 2
if "hari" in a2 :
  print("yes")
else:
  print("no")


#wrong method
if "ari" in a2 :
  print("yes")
else:
  print("no")



# printing elements with particular range

animals = ["cow","bat","cat","horse","lizard","bufallo"]
print(animals[:4])
print(animals[:-4])
print(animals[4:])
print(animals[-4:])
print(animals[:1])
print(animals[3:5])
print(animals[3:1])    #wrong (positive index only increase)
print(animals[-5:-1])
print(animals[-3:-5])  #wrong (negative index only increase) i.e.., -3 , -2 ,-1 , 0 , 1 , 2,..,
print(animals[-3:-2])
print(animals[-3:5]) 
print(animals[3:-1])  
print(animals[-5:1])  # It will empty , Because there is no possibile
print(animals[1:-1]) 

#### ending number is used to skip value ex :- 2 and 3 in below ex
print(animals[0:5:2])  #output is cow,cat,lizard
print(animals[0:5:3])  #output is cow,horse





###### list comprehension not completed # tutoral 22