a = input("Enter the number : ")
print(f"multipicatin of table {a}is")

for i in range(1,11):
  print(f"{int(a)} x {i} =  {int(a)*i}")



b = input("Enter the number : ")
print(f"multipicatin of table {b}is")

for l in range(1,11):
  print(f"{(b)} x {l} =  {(b)*(l)}")   # int tag is must important



# try and except and exception

# if we enter any name or alphabet in input it show an error 
# if it show an error in line 29 then it will not print line 33 and 34
# then we use try and except in the place of error then it will not show error 
# and it print line 33 and line 34


c = input("Enter the number : ")
print(f"multipicatin of table {c}is")
try :
  for m in range(1,11):
    print(f"{int(c)} x {m} =  {int(c)*(m)}")
except Exception as f:    # Exception must be write like this only , no other element work
  print(f)             # f is an error , we can replace any element in place of f

print("above have the the table")
print("above have the the tables")


# only try and except 

d = input("Enter the number : ")
print(f"multipicatin of table {d}is")
try :
  for n in range(1,11):
    print(f"{int(d)} x {n} =  {int(d)*(n)}")
except :   
   print("sorry")

print("above have the the table")
print("above have the the tables")



# Value error and Index error

try :
  num = int(input('enter the number :- '))
  a = [6,3]
  print(a[num])
except ValueError : #if we enter not a integer number then it show
  print ("valueerror")   
except IndexError: #if we enter any ineger except 6,3 then it show
  print("indexerror")

# or 

while True:
    try :
      num = int(input('enter the number :- '))
      if num in (3,6):                          # We can use list (3,6) or Tuples [3,6]
      # or
      # if num == 3 or num == 6 :
          print("This is True condition")
          break
      else:
          print("Please eneter in range !")
    except ValueError : 
      print ("valueerror")   

# or

while True:
    try :
      num = int(input('enter the number :- '))
      if num >3 and num <6:
          print("This is True condition")
          break
      else:
          print("Please eneter in range !")
    except ValueError : 
      print ("valueerror")   
