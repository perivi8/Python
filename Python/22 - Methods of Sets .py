# Methods of Sets

#union method
#this method is used to combine two sets into a one set

p1 = {1,2,7,4,5}
p2 = {6,7,8,9}
p3 = p1.union(p2)
print(p3)
#or
print(p1.union(p2))

#update method

h1 = {1,2,5,6}
h2 = {2,3,6,7}
# print(p1.update(p2))  wrong method
h1.update(h2)         #in update direct we can write
print(h1)


#intersection

k1 = {1,2,5,6}
k2 = {2,3,6,7}
k3 = k1.intersection(k2)
print(k3)
#or
print(k1.intersection(k2))


#intersection update
k4 = {1,2,5,6}
k5 = {2,3,6,7}
k4.intersection_update(k5)      #in update direct we can write
print(k4)



# symmetric_difference
l1 = {1,2,5,6}
l2 = {2,3,6,7}
l3 = l1.symmetric_difference(l2)
print(l3)
#or
print(l1.symmetric_difference(l2))


#symmetric_difference_update
l4 = {1,2,5,6}
l5 = {2,3,6,7}
l4.symmetric_difference_update(l5)
print(l4)


#difference
m1 = {1,2,5,6}
m2 = {2,3,6,7}
m3 = m1.difference(m2)
print(m3)
#or
print(m1.difference(m2))

#difference_update
m4 = {1,2,5,6,8}
m5 = {2,3,6,7}
m4.difference_update(m5)
print(m4)



#isdisjoint

#ex 1
n1 = {3,5,7,9}
n2 = {2,4,6,8}
n3=n1.isdisjoint(n2)
print(n3)
#or
print(n1.isdisjoint(n2))

#ex 2
n4 = {1,2,3,4,5,6,7}
n5 = {2,4,6,8}
n6=n4.isdisjoint(n5)
print(n6)
#or
print(n4.isdisjoint(n5))


#issuperset

#ex 1
o1 = {2,4,6,8}
o2 = {1,3,5,7}
o3 = o1.issuperset(o2)
print(o3)
#or
print(o1.issuperset(o2))

#ex 2 
o4 = {2,4,6,8}
o5 = {2,4,6,8}
o6 = o4.issuperset(o5)
print(o6)
#or
print(o4.issuperset(o5))

#issubset

#ex 1
p1 = {1,4,5,7,9}
p2 = {2,4,6,8,0}
p3 = p1.issubset(p2)
print(p3)
#or
print(p1.issubset(p2))

# ex 2
p4 = {2,4,6,8}
p5 = {1,2,3,4,5,6,7,8}
p6 = p4.issubset(p5)
print(p6)
#or
print(p4.issubset(p5))


#add
#if we want to add 1 number or element then use add
q1 = {"hari","krishna"}
q1.add("periv")
print(q1)

#update
# if we want update more than one element then use update
q2 = {1,2,3,4}
q3 = {5,6,7,8,9}
q2.update(q3)
print(q2)

#remove 
r1 ={"akhil","kumar","perivi",2000}
r1.remove(2000)
print(r1)

#discard
#it does not show error
r2 = {"akhil","kumar","perivi",2000}
r2.discard("hari")
print(r2)



#pop
#delete 
#clear 
#above 3 topics are not completed #tutorial 32