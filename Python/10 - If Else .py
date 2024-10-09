#if Else
# ex 1
a = int(input("enter your age :- "))  #must use int,{if we enter age}
print("your age ", a)  #only use (,)
if (a == 18):  #must use (:) at the end
  # we use { < , > , <= , >= , == }
  print("yor are selected")  #staring space is very important
  print("yes")  # we can enter so many like this
else:  #must use the (:) at the end
  print("not selected")  #starting space is very important

# ex 2

appleprice = int(input("enter price"))
budject = int(input("enter budject"))
print(appleprice<=budject)
if(appleprice<=budject):    #this is condition
  print("take it")
else:
  print("don't take")   

#conditonal operators
## we use { < , > , <= , >= , == }
b = int(input("enter your age : - "))
#it will show output is true or false
print(b == 18)
print(b <= 18)
print(b >= 18)
print(b < 18)
print(b > 18)
print(
  b != 18
)  #if we enter lessthan or greaterthan 18 it will show true , if we enter same number then it will show false

#if , else ,elif

c = int(input("enter your age"))
if(c>18):
  print("ok")  # if we enter more than 18 it will come
elif(c==18):
  print("may be")  #if we enter 18 it will come
else:
  print("no")    #if we enter lessthan 18 it will come