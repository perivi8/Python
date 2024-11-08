#  WHILE Loop

# Ex 1
i=1
while i<=10:
  print(i)
  i+=1 # i = i+1


# Ex 2
i=5
while i > 10:
    print('Eneter yoyr Nmae')
    i+=1
else :
    print(f'{i} is not greater than 10')

#--------------------------------------------------------------------------------------------

#Ex 3
#  It given While condition is Correct means

i=555
n=567
while i<=n:
  try:
    if i%2 == 0:
      print(i)
    i+=1 
  except ValueError:
      print("not Possible")
else:
   print('Loop was endeed !!')

# It given While condition is wrong means
i=555
n=567
while i>=n:
  try:
    if i%2 == 0:
      print(i)
    i+=1 
  except ValueError:
      print("not Possible")
else:
   print('Loop was endeed !!')


#--------------------------------------------------------------------------------------------

# Ex 4
while True:
    a = int(input("enter a number !!! :-"))
    if a > 18:
        print('You are eligible!')
        break
    elif a == 18:
        print('Your appliation was on Hold !')
    else:
        print('You are no eligible !!')  



# Ex 5
while True :
    name = input('Eneter Your name :- ')
    if name.isalpha():
        print(f'welcome Mr/Miss : {name}')    
        break
    else :
        print("please enter valid Nanme")


#--------------------------------------------------------------------------------------------


# Ex 6
count = 0

while count < 5:
    try:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        print("That's not a valid number. Please try again.")
    count += 1

print("Loop has ended.")

# -------------------
while True:
    try:
        num = int(input('Enter your name :- '))
        if num>10:
            print(f'{num}  is greater than 10 ')
        else :
            print(f'{num}  is Less than 10 ')
            
    except ValueError:
        print('Error')
        break


# Ex 7
i = 0

while i<10 :
    # num = int(input('enter nember :- '))           # Don't use here ,  It will correct but if we enter any 'string' it will show error
    try:
        num = int(input('enter nember :- '))  
        if num>10:
            print(f'f{num} is greater than 10')
        else:
            print(f'f{num} is less than 10')   
    except ValueError:
        print("this is not an integer")
    i +=1                                       # It will help to repeat up to while condition was satisfied (Up-to = n Times)
else:
    print('Loop was Endeeed')  



# Ex 8
i = 0

while i>10 :        
    try:
        num = int(input('enter nember :- '))  
        if num>10:
            print(f'f{num} is greater than 10')
            break                                   # It help to Break the Loop
        else:
            print(f'f{num} is less than 10')   
    except ValueError:
        print("this is not an integer")
    i +=1                                      
else:
    print('Loop was Endeeed')        


#--------------------------------------------------------------------------------------------


# Ex 9
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

# -----------------

i = 0

while i<10 :
    try:
        m = int(input('Enter Number :-'))
        if m%2 == 0:
            print(f'{m} is even ')
        else:
            print(f'{m} is Odd')  
            # break 
    except ValueError:
        print("this is not an integer")
    i +=1                                      
else:
    print('Loop was endeeeeed !')       




# Ex 10

i = 1

while i<10:
    try:
        num = input('Enter your name :- ')
        if num.isalpha():
            print(f'Hello Mr/Miss :- {num}')
            break
        else :
            print('Please eneter only alphabets')
        i +=1
    except ValueError:
        print('Error')


# Ex 11

while True:
    try:
        num = input('Enter your name :- ')
        if num.istitle():
            print(f'Hello Mr/Miss :- {num}')
            break
        elif num.isalpha():
            print('Please enter Title Formate !')
        else :
            print('Please eneter only alphabets')
            
    except ValueError:
        print('Error')




        
























