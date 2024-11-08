# Function Catching is nothing but it store the data Temporarly 

# If the data take time to Return , again same data will retuern fast another time , withot any Lag

import time

from functools import lru_cache

@lru_cache(maxsize=None)

def hari(n):
    print(f'The Enter value is {n}')
    time.sleep(3)
    return n * n


# First it will take some time
print(hari(2))   
print(hari(3))
print(hari(5))

print('---------------------------------------')

# It will not take any time
print(hari(2))
print(hari(3))
print(hari(5))
print(hari(8))  # It will take some time







#  Reference Link :- https://youtu.be/vjQqLDe9Lnc