# for loop with else 



# ex 1
for i in range(3):
  print(i)
else :
  print("sorry no i")



# ex 2

for l in range(10):
  print()    # if we do not enter any element in print it will give empty lines (range)
else :
  print("sorry no l")


# ex 3
for m in []:       # [] this is an empty set
  print()
else :
  print("sorry no m")




# ex 4
for x in range(5):
  print("iteraion no {} ".format(x))

else :
  print("else no ")


# ex  5

for a in range(6):
  print(a)
  if a==4:
    break   # loop was not broken . loop was ended

else :
  print("no a")
  
