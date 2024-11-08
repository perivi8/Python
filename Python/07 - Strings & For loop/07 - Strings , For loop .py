#string concept and {for loop} concept

name0 = "hari"
friend0 = "prabhas"
print(
  "hello " + name0
)  #if we want to combine { word or sentence or number then use the symbool (+ or ,)}

name = "hari"
friend = "prabhas"
print("hello ", name)

name1 = "krishna"
friend1 = "perivi"
print("hii  " + name1 + "  " + friend1)  #if we space then use string like this

name2 = "krishna"
friend2 = "perivi"
print("hii  " + name2 + "     " + friend2)



# if we want to write continue lines then use only single (') or (") , starting and ending

apple = "hlo hari ,mkjdfi hvsl.kjhs jghsuh;gz  irhk;e jnre rkglen  jg;ozhglwr rgoh;g ohilz   ghrwoghl wrg  zrhgurh ;zrgiorhg  ;o irhwf;io  rhgioshglh g;"
print(apple)



# if we want to write single or half line then give three (''') or (""") starting and ending

banana = '''hlo hari
i am "good 
how are you 
hlo
jdjrsg 
eneof
                  

fine''' 
print(banana)


# String how to use by index

a = "hari,krishna "
print(a[1])

b = "hari", "krishna", 8
print(b[1])

c = "hari krishna", 8
print(c[1])


# FOR LOOP

# Ex 1
a1 = "Hari Krishna"

for character in a1:  
  print(character) 


# Ex 2
z = ["hari" , "krishna" , "perivi"] 

for i in z :
  print(i)