
#Finally clause

a = input("Enter the number : ")
print(f"multipicatin of table {a}is")
try :
  for m in range(1,11):
    print(f"{int(a)} x {m} =  {int(a)*(m)}")
except :                     # if we enter correct then it will not show
  print("sorry")         
  print("it is wrong")
print("hii")     #starting without space means it is equal to the finally clause





#if we enter wrong integer

d = input("Enter the number : ")
print(f"multipicatin of table {d}is")
try :
  for n in range(1,11):
    print(f"{int(d)} x {n} =  {int(d)*(n)}")
except :   
  print("sorry")
  print("it is wrong")

finally: 
   print("thank u")
  
print("bye")




#if we enter correct integer

e = input("Enter the number : ")
print(f"multipicatin of table {e}is")
try :
  for o in range(1,11):
    print(f"{int(e)} x {o} =  {int(e)*(o)}")
except :   
  print("sorry")
  print("it is wrong")

finally: 
   print("thank u")
  
print("bye")



