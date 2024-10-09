# break and continuous

#break
#break is used to where we want stop 
# ex 1
for i in range(13) :
  print('5 x ',i," = ",5*i)
  if (i==10):
    break

# ex 2
for k in range(15):
  print("3 + ", k , " = " ,3+k )
  if (k>=10) :
   print("stop")
   break

#continue
    
 #ex 1 (correct method)
for h in range(14):
 if(h==10):    #in this example 5 x 10 = 50 was disabled ,remaining same
   print("stop")
   continue
 print('5 x ',h," = ",5*h)



#ex 2 (wrong method)
for m in range(12):
  print("4 x ",m , " = ",4*m)
  if(m==10) : #in this 4 x 10 = 40 was not disabled
   print("stop")
   continue