# Walrus Operator 

h = True
print(h)
print(h := False)  
# print(h = False)  # this is wrong
print(i := True)



print("-----------------------------")

a = (1,2,3,4,5,6,3,2)

# if (n := len(a) > 2):
if (n :=len(a)) > 2 :
  print("This is correct")
  print("the length of (a) is ", a)
  print(n)

print("----------------------")

b = (7,8,9,0)
m = len(b)
if m >2 :
  print("awsome")
  print("lengtgh is ", m)

