# length of a string

#ex 1
a = "hari"
print(len(a)) #if we want to know how many words are present in given word then we use lengt function
print(a[:4]) #value of length is kept here , in this 0 is defalt

#ex 2
fruit = "mango"
print(len(fruit))
print(fruit[0:4])

#ex 3
fruit2 = "mango"
print(len(fruit2))
print(fruit2[0:len(fruit2)-3])

# ex 4
fruit3 = "mango"
print(len(fruit3))
print(fruit3[0:-2])

# ex 5
a = [1,4,"hari" , "pr=eroivi"]
print(len(a))

# ex 6
b = (1,4,"hari" , "pr=eroivi")
print(len(b))