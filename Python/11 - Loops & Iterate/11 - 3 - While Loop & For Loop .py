#Ex 1

# While Loop
i=1
while i<=10:
  print(i)
  i+=1

# For Loop
for j in range(11):
  print(j)

#--------------------------------------------------------------------------------------------

# Ex 2

# While Loop
i=5
while i > 10:
    print('Eneter yoyr Nmae')
    i+=1
else :
    print(f'{i} is not greater than 10')

print('\n')


# For Loop
for i in range(5):
    print('Eneter yoyr Nmae')


#--------------------------------------------------------------------------------------------

# Ex 3

# While Loop
i = 0

while i<10 :
    try:
        if i%2 == 0:
            print(f'{i} is even ')
        else:
            print(f'{i} is Odd')  
            # break 
    except ValueError:
        print("this is not an integer")
    i +=1                                      
else:
    print('Loop was endeeeeed !')       


# For Loop
print("\n")

for i in range(1,10):
    if i%2 == 0:
        print(f'{i} is an EVEN') 
    else :
        print(f'{i} is an ODD')
        
