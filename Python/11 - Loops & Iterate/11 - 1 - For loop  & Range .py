#for loops
# ex 1
names = ("hari","akhil","sai","bhanu")
for k in names :   #we can use any thing in the place of k
  print(k)       #must enter same as above
  for i in k :   
    print(i)

#ex 2
fruits = ("apple","banana","goa","papaya")
for fruit in fruits : 
  print(fruit)
  for i in fruit :
    print(i)
    for k in i :
      print(k)
      for a in k :
        print(a)

# for loop using with range
#range is used to write the numbers
#ex 1
for b in range(5):    #output is 0,1,2,3,4   #stars from zero
  print(b)

#ex 2
for c in range(5) :#if we want start from 1
 print(c + 1) # output is 1,2,3,4,5

#ex 3
for d in range(2,5) :
  print(d)  #output is 2,3,4

#ex 4 
for e in range(2,5) :
  print(e+1)  #out put is 3,4,5

# ex 5

for f in range(1,12,2) :  #the endining number is used to gap between one number to another number 
  print(f)   #out put is 1,3,5,7,9,11

#ex 6
for g in range(1,12,3) :  #the gap between one num to another num is 3
  print(g) #output is 1,4,7,10

# ex 6
for h in range(1,12,0) :  
  print(h) #output is  Error




# Additional Example 

# If we want to repeat the proces of add , sub , ... then just give range , that many times we can do operator

for i in range(5):  
  a=int(input('Enter first number'))
  b=int(input('Enter second number'))
  sum=a+b
  print(f"Sum of 2 no's {sum}")




#  NOTES


# If we are using for loop or any other loopp then use print
# Ex
# def word(num):
#     for j in range(1,11):
#         time.sleep(1.5)
#         print(f'{num} X {j} = {num*j}')
       
# word(2)


# # If we are using return in loops it will return only one time.
# # Ex
# def word1(num):
#     for j in range(1,11):
#         time.sleep(1.5)
#         return f'{num} X {j} = {num*j}'

# print(word1(4))

