# break and continuous

#break
#break is used to where we want stop 
# ex 1
for i in range(13) :
  print('5 x ',i," = ",5*i)
  if (i==10):
      print("end")
      break


# ex 2 (Recommended)
for i in range(13) :
  if (i==11):
        print("end")
        break
  print('5 x ',i," = ",5*i)


# ex 3
for k in range(15):
  print("3 + ", k , " = " ,3+k )
  if (k>=10) :
   print("stop")
   break



#continue
    
 #ex 1 (Recommended)
for h in range(14):
 if(h==10):    #in this example 5 x 10 = 50 was disabled ,remaining same
   print("stop")
   continue
 print('5 x ',h," = ",5*h)



# Ex 2 
for m in range(12):
  print("4 x ",m , " = ",4*m)
  if(m==10) : #in this 4 x 10 = 40 was not disabled
   print("stop")
   continue


# Ex 2 (Used situation)
for i in range (10):
    print(f'{i}')
    if i%2 == 0:
        print("even")
        continue


# --------------------------------------------------------------------------------------------------

# Ex A
for i in range(10):
    if i == 6:
        print('this is number 6')
        break
    print(f'{i}') 

# Difference

for i in range(10):
    print(f'{i}')
    if i == 6:
        print('this is number 6')
        break
    


# Ex B
for i in range(10):
    if i == 6:
        print('this is number 6')
        continue
    print(f'{i}')

# Difference

for i in range(10):
    print(f'{i}')
    if i == 6:
        print('this is number 6')
        continue

