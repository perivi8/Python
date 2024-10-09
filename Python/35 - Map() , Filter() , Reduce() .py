# map
# map is used to multiply or add or sub or div or square or cube the list or tuple or any function

# ex 1
number1 = [1,2,3,9,5,6,7]
hari1 =map(lambda x: x+2 , number1)
print(list(hari1))

# ex 2 
number2 = [1,2,3,9,5,6,7]
hari2 = map(lambda x : x%2==0 , number2) #x% is used in filters
print(list(hari2)) 



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