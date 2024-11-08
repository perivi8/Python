# seek() function


with open("./33 - seek() , tell() , truncate()/33 - X .txt",'r') as f :
  print(f.seek(4) )                # it hide the data 
  print(f.read())          # continue after hiden data



#-----------------------------------------------------------------------------

# tell() function  

# It is used to show the No.of Seek() & No.of Read()
 
# ex 1
with open("./33 - seek() , tell() , truncate()/33 - Y .txt",'r') as h :
  print(h.seek(7))
  print(h.tell())    #output = 7


# Ex 2
with open("./33 - seek() , tell() , truncate()/33 - Y1 .txt",'r') as g :
  print(g.read())   # If we not use any read()/seek() means tell() will show 0
  print(g.tell())   # It will count entire part of the Count in that file including lines(---)


# Ex 3
with open("./33 - seek() , tell() , truncate()/33 - Y1 .txt",'r') as g1 :
  print(g1.read(8))   # If we Given 8 or some value
  print(g1.tell())   # Here also Show same value which we enter in Read() 

#-----------------------------------------------------------------------------

# truncate()

i = open('./33 - seek() , tell() , truncate()/33 - Z .txt' , 'w')
print(i.write('Hello Hari!!'))
print(i.truncate(4))   # only 'hell' is write in '33 - Z .txt' file

i1 = open('./33 - seek() , tell() , truncate()/33 - Z .txt' , 'r')
print(i1.read())

  
