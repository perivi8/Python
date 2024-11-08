# raising custom errors

# the Raise is used to to create an error . 

# We are raising error , even if condition is True


# a = int(input("Enter value : "))
# if a == 3:
#     raise ValueError("Wrong value")
# else:
#     print("This is Not 3")



a = int(input("enter value in between 5 and 9 = "))
if (a>5 or a<9):
  raise ("wrong")
else:
   print("This are not in between 5 and 9")


