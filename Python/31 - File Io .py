# File lO

# # read

# # ex 1
z = open('31 - harifile.txt' , 'r')
print(z.read())


# ----------------------------------------------------------------------------------

# # write

# # ex 1

z1 = open('31 - harifile1.txt','w')   # write 'w' is used to create a new file



# #ex 2
#  If we Clear the data in PY File , Automatically the data will erase in TXT File also.

z2 = open('31 - harifile2.txt','w')  
print(z2.write('hello'))    


# --------------------------------------------------------------------------------

# append

# How many time we execute the Code , That may times it return the Values
#  It will not Remove data in TXT File , Even If we remove in PY file

z3 = open('31 - harifile3.txt' , 'a')
print(z3.write('gf')) 








