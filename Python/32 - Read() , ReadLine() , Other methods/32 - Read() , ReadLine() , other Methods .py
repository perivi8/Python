# readline()

#if we use direct readline method , it will read only the first line . See Ex - 2 

# ex 1

a = open('./32 - Read() , ReadLine() , Other methods/32 - X.txt','r')
print(a.read())

# ex 2 

a1 = open('./32 - Read() , ReadLine() , Other methods/32 - X.txt' , 'r')
print(a1.readline())


# ---------------------------------------------------------------------


# WriteLines()

# We can use Wite() in place of WriteLines() .......

c1 = open('./32 - Read() , ReadLine() , Other methods/32 - Z.txt','w')
print(c1.writelines('Perivi\n''Hari\n'))
c1.close()

#  Ex
c1 = open('./32 - Read() , ReadLine() , Other methods/32 - Z1.txt','w')
print(c1.write('Perivi\n''Hari\n'))
c1.close()
