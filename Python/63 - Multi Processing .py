#  If it showing  error in VS code means trt in online comiplier

import multiprocessing
import time

#Ex 1

def print_number():
    for i in range(1,6):
        time.sleep(1)
        print(f'The number is {i}')

def print_letters():
    for letters in 'ABCDEF':
        time.sleep(1.5)
        print(f'the letters are {letters}')


thread1 = multiprocessing.Process(target=print_number)
thread2 = multiprocessing.Process(target=print_letters)


thread1.start()
thread2.start()


thread1.join()
thread2.join()


print('Both threads are completed')



# # Ex 2

def word(num):
    for j in range(1,11):
        time.sleep(1.5)
        print(f'{num} X {j} = {num*j}')

def word1(num , num1):
    for j in range(1,11):
        time.sleep(1.5)
        print(f'{num} X {j} = {num1*j}')


thread3 = multiprocessing.Process(target=word , args=[3])
thread4 = multiprocessing.Process(target=word1 , args=[4 , 1])

thread3.start()
thread4.start()

thread3.join()
thread4.join()





# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()

# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()



#  Reference link :- https://youtu.be/rzRUSDNjggo