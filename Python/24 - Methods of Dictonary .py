#Dictionary Methods

#update

#ex 1
a1 = {"h":1,"h2":2,"h3":3,"h4":5,"h5":6,"h6":7}
a1.update({"hari":4,"krishna":3})     #we can add extra elements
print(a1)

#ex 2
a2 = {"h":1,"h2":2,"h3":3,"h4":5,"h5":6,"h6":7}
a2.update({"h3":9,"h2":8})   # we can change or update 
print(a2)

#ex 3
a3 = {1:2,3:4,4:5,6:7,8:9}
a4 = {1:8,3:4,5:5,6:6,9:8}
a3.update(a4)
print(a3)

# clear
#it is used for clear all elements
a5 = {"h":1,"h2":2,"h3":3,"h4":5,"h5":6,"h6":7}
a5.clear()
print(a5)


# pop
#it is used for remove any dictionary
a6 = {"h":1,"h2":2,"h3":3,"h4":5,"h5":6,"h6":7}
a6.pop("h")
print(a6)



# popitem
#it is used for remove last dictionary
a7 = {"h":1,"h2":2,"h3":3,"h4":5,"h5":6,"h6":7}
a7.popitem()
print(a7)

# delete
a8 = {"h":1,"h2":2,"h3":3,"h4":5,"h5":6,"h6":7}
del a8["h2"]
print(a8)