# import date

from datetime import date
print(date.today())

print("---------------------------------------------------------------------------------")

# import time
import time
print(time.time())

print("---------------------------------------------------------------------------------")

# time.sleep()
   # ex 1
import time
print("start :-" , time.time())
time.sleep(5)
print("end" ,time.time())

print("-----------------------------")

  # ex 2
import time
time.sleep(3)
print("this is printed after 3 sec" , time.localtime())

print("----------------------------------------------------------------------------------")

# GMT (time)

# %a = day , %d = month , %b = year , %Y = Year , %H = Hours , %M = Minutes , %S = Seconds 

# strftime() = String Formate Time

from time import gmtime, strftime
s = strftime("%a, %d %b %Y %H:%M:%S",  gmtime())
print(s)

print("-----------------------------")

# Local Time (GMT+05:30) , It is Our Indian Time

from time import gmtime, strftime
s1 = strftime("%a, %d %b %Y %H:%M:%S",  time.localtime())
print(s1)




# for more details visit 
     #  https://www.geeksforgeeks.org/python-time-module/