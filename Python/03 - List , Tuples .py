# list
# lists only use square brackets
# list is used for set the data in an order (fruits,numbers,integers,negative values,point values)
# it his starts from 0,1,2,3,4,5.....,,
# if we enter any number then it shows that number place value
# in this we change the elements any time. see example 3

# ex 1
list1 = ["apple","banana","goa"]
print(list1)

#ex 2
list3 = ["apple","banana","goa"]
print(list3[1])    #use only square bracket 

# ex 3
list2 = [2,3,3.5,-4.5,"apple"]
list2[3]="lion"    # we can change in list
print(list2)
 

# tuple
# tuple use only round brackets
# in tuple we cannot change the element once we run the program

#ex 1
tuple1 = ("lion","tiger","ant")
print(tuple1)

#ex 2 
tuple3 = ("apple",2,"boy","hero")
print(tuple3[2])     #use only square brackets

#ex 3

tuple2 = ("apple",2,"boy","hero")
tuple2[0] = 1   #it shows error . because tuple does not change
print(tuple2)