# map
# map is used to multiply or add or sub or div or square or cube the list or tuple or any function

# ex 1(using Lambda)
number1 = [1,2,3,9,5,6,7]
hari1 =map(lambda x: x+2 , number1)
print(list(hari1))   # We can use list / tuple in  map , filter

# or

# Ex (Using Function)
def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))



# ex 2 
number2 = [1,2,3,9,5,6,7]
hari2 = map(lambda x : x%2==0 , number2) #x% is used in filters
print(list(hari2)) 


# Ex 3

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# or

def func(number1 , number2):    
    return number1 + number2

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(func , numbers1 , numbers2)
print(list(result))


# Ex 4
name1 = ["hari" , "perivi" ,"sangeetham" , "ajay" , "hyma"] 
age = [14 , 15, 25 , 23 , 44]

a = map(lambda x , y : f'name is {x} and age is {y}', name1 , age)
print(list(a))

# or

name2 = ["leo" , "vikram" ,"devil" , "robo" , "I"] 
age1 = [43 , 23, 15 , 64 , 19]

def details(x , y):
    return f'name is {x} and age is {y}'

b = map(details, name2 , age1)
print(list(b))


# ----------------------------------------------------------------------------------------

# filter

# filter is used to seperate the even or odd

# ex 1
number3 =  [8,9,1,2,3,4,5]
krishna1 = filter(lambda x : x%2==0 , number3 )  # It will retutn only the values which are multiply by 2
print(list(krishna1))

# ex 2
number4 =  [8,9,1,2,3,4,5]
krishna2 = filter(lambda x : x>3 , number4 ) # We can use any conditions (i.e. < , > , %value == 0 , .....,)
print(list(krishna2))

# ex 3
number5 =  [8,9,1,2,3,4,5]  
krishna3 = filter(lambda x : x*2 , number5 ) # this is an map method , and we get same numbers
print(list(krishna3))  



# -------------------------------------------------------------------------------------------

# reduce

# ex 1
from functools import reduce # this is important for reduce function

number6 = [8,9,1,2,3,4,5] 
akhil1 = reduce(lambda x ,y : x+y, number6 )
# print(list(akhil1)) # it show an error , it no need list syntax


# ex 2
from functools import reduce

number7 = [8,9,1,2,3,4,5] 
akhil2 = reduce(lambda x,y : x+y , number7 )
print(akhil2)