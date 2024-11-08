# list methods

#append
l1 = [1,2,5,6,4,8]
l1.append(9)    #append is used to add the element in last
print(l1)


#sort
#ex 1
l2 = [1,2,5,6,4,8]
l2.sort()      # sort is used to increase the order of elements
print(l2)

#ex 2
l3 = ["banana","apple","goa","cow"]
l3.sort()      # sort is used to  increase the order of elements
print(l3)

#reverse sort
#ex 1
l4 = [30,40,45,20,35,25,50]
l4.sort(reverse=True)    #reverse = True is high to low
print(l4)

#ex 2
l4 = [30,40,45,20,35,25,50]
l4.sort(reverse=False)     #reverse = False is low to high
print(l4)

#reverse
l5 = [20,21,32,25,64,49,48,50]
l5.reverse()  # it is reverse the order
print(l5)

#Index
# it is used to find the index of the  using element
l5 = [20,21,32,25,64,49,48,25,50]
print(l5.index(25))              #only use circle brackets


#it is used to find the element using index
l5 = [20,21,32,25,64,49,48,25,50]
print(l5[4])               #only use square brackets



#count
l6 = ["apple","banana",3,5,3,4,6,4,3,4,2,1,"apple","goa"]
print(l6.count("apple"))   #output is 2
print(l6.count(4))   #output is 3



#change the list
l8 = [3,4,56,67,7,3,89,4,5]
l8[2] = "red"
print(l8)


#insert
#ex 1
l9 = [3,5,7,78,9]
l9.insert(2,"yellow")  #o/p is [3,5,'yellow',7,78,9]
print(l9)


# ex 2
a9 = [3,5,7,78,9]
a9.insert(4, 3)        #o/p is [3,5,7,78,3,9] 
print(a9)



#copy 
# ex 1
l8 = [2,3,4,5,6,67,7,8,9,10]
m = l8.copy()
n = m.copy()     
o = l8.copy()
print(l8)
print(m)
print(n)


#ex 2
l7 = [2,3,4,5,6,67,7,8,9,10]
m = l7.copy()
l7[0] = 0    #it is used to change the list
m[2] =3             #it is used to change the list
print(l7)
print(m)



#extend
#ex 1
e1 = ["red","yellow",1,2,"green",3]
e2 = ["pink","sai",3,4,"blue"]
e1.extend(e2)
print(e1)

# ex 2 
e3 = ["red","yellow",1,2,"green",3]
e4 = ["pink","sai",3,4,"blue"]
e4.extend(e3)
print(e4)
