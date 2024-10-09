

# -----------Ex-------------- #

# --While Loop--#

i=1
while i<=10:
  print(i)
  i+=1 #i=i+1

# --For Loop--#

for j in range(11):
  print(j)

# -----------Ex-------------- #

i=1
while i<=10:
  print(i)
  i+=1 
else :                                          # It will return else statement also , even IF condition was satisfied
    print(f'{i} is not greater than 10')
    


i=5
while i > 10:
    print('Eneter yoyr Nmae')
    i+=1
else :
    print(f'{i} is not greater than 10')


# -----------Ex-------------- #

print('\n')
for i in range(5):
    print('Eneter yoyr Nmae')


# -----------Ex-------------- #

i=555
n=567
while i<=n:
  if i%2 == 0:
    print(i)
  i+=1
  
else :
  print("not Possible")


# -----------Ex-------------- #

while True:
    a = int(input("enter a number !!! :-"))
    if a > 18:
        print('You are eligible!')
        break
    elif a == 18:
        print('Your appliation was on Hold !')
    else:
        print('You are no eligible !!')  

# -----------Ex-------------- #

while True :
    name = input('Eneter Your name :- ')
    if name.isalpha():
        print(f'welcome Mr/Miss : {name}')    
    else :
        print("please enter valid Nanme")
        









# -------Error---------#


while True:
    i = 1
    if i <= 16:
        print('Yahoooo!')                     # If Condition is satisfied , but output will not stop 
        i += 1
    else:                                          
        print(f'{i} is not greater than 10')



while True:
    i = 1
    if i <= 16:
        print('Yahoooo!')                      # It will run only one time
        break
    else:                                      # It will not show because the If condition is satisfied
        print(f'{i} is not greater than 10')



while True:
    i = 1
    if i > 16:
        print('Yahoooo!')                      # If condition Not satisfied
        i +=1
    else:                                          
        print(f'{i} is not greater than 10')   # It will not stop 


while True:
    i = 1
    if i > 16:
        print('Yahoooo!')                      # If condition Not satisfied
        break
    else:                                          
        print(f'{i} is not greater than 10')   # It will not stop 





