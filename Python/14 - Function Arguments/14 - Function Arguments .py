#function arguments
#  they are totally 4 type of arguments 
# 1 = default  argument
# 2 = keywoard  argument
# 3 = variable length argument
# 4 = required argument



# Default argument
# ex 1
def name(a = "hari",b = "krishna"):
  print("hello", a , b)
  
a = "akhil" 
name(a)
#or
name("akhil")

#ex 2
def name1(a,b="hari",c="krishna"):
  print(a,b,c)  

name1("perivi","akhil")  





# keyword argument
def name2(e  ,f ,g ):
  print("hello",e,f,g)

f ="hari"  
g = "krishna"

name2(f = "akhil",g = "kumar",e = "perivi" )



# required argument

#if we have e , f , g  are 3 characters but we give only e , f then it shows error

def name3(e  ,f ,g ):
  print("hello",e,f,g)

f ="hari"  
g = "krishna"

# name3(f = "akhil",g = "kumar" )   #it shows error




# variable length argument 

# Ex 1
def name4(*name):
  print("hello",name[0],name[1])    #we use only numbers

name4("hari","krishna","perivi")   # No need to mention Index value


# Ex 2
def name8(*name):
  print("hello",name['a'],name['b'])   

# name8("hari","krishna","perivi")    # It show error


# Ex 3
def name4(*name):
  print("hello",name["a"],name["b"])   

# name4(a= "hari",b="krishna","perivi")    # It show error

# ------------------------------------------------------------------------


#                    extra argument
#keyword arbitary argument

#correct method
def name5(**name):
  print("hello",name["p"],name["h"],name["k"]) #we use letters or words

name5(h="hari",k="krishna",p="perivi")



#wrong method 1
def name6(**name):
  print("hello",name["0"],name["1"],name["2"])

# name6(1="hari",2="krishna",0="perivi")     # it shows error

# wrong method 2
def name7(**name):
  print("hello",name[0],name[1],name[2])

# name7(1="hari",2="krishna",0="perivi")  #it shows error




#### return statement not completed  #tutorial 21