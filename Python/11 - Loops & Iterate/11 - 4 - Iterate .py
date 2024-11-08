# ITER
a = [1,'apple', 'Banana' , True , 1.5]

iterate = iter(a)

print(iterate)

print(next(iterate))
print(next(iterate))
print(next(iterate))
print(next(iterate))


# Ex
b = (1,'apple', 'Banana' , True , 1.5)

iterate1 = iter(b)

print(next(iterate1))
print(next(iterate1))
print(next(iterate1))




# GENERATOR (File 60)

data = [23,'cake' , False , 3.5 , "Dog"]
def func():     
    for m in data:
        yield m

func1 = func()

print(next(func1))   
print(next(func1))      
print(next(func1))   
print(next(func1))   

# or 

# If we want to Iterate all the data from List / Tuples / Sets ...,

# for m1 in func1:
#     print(m1)  