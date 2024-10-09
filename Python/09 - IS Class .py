#in this must use {.} before upper and lower and strip and rstrip and replace and 
#if we want the upper letters then use upper case

a = "hari"
print(a.upper())

#if we want lower case letters then
b = "HARI"
print(b.lower())  

#strip is used to remove the space before and after string
c = "         HARI          " 
print(c.strip())

#rstrip is usesd to remove the trailind characters ex :- ! @ # $ % ^ 
d = "@@@@@@ HARI @@@@@@@@"
print(d.rstrip("@")) #it will remove trailinmg characters only after the word or text


#replace is to replace any letter in between the word
e = "krishna"
print(e.replace("ri","lt")) #only use {,} 


#split is used for to seperate the sentence
#split is used to make list easily
f = "hari krishna @ 8"
print(f.split(" ")) #must use space in between the (" ")


#capitalize is used to write the first letter as a captial
g = "hari is a good boy"
print(g.capitalize())


#the center is used to create the how much we want length
#ex:- if we want length 50 but we have only 25 then use center 
#ex:- 1
h ="akhil kumar"
print(h.center(50))

#ex:- 2
i = "akhil kumar"
print(i.center(50,"^")) 

#count is used to how many repeat words are present in sentence
j = "hari krishna , hari boy"
print(j.count("a"))    #which letter you want to check , then enter

#ends with
#it says true or false
#ex - 1
k = "hari krishna "
print(k.endswith("$$$$$"))  #then output is false
print(k.startswith("k"))  #it shows false

#ex - 2 
l = "hari krishna $$$$"
print(l.endswith("$"))   #it shows true
print(l.startswith("h")) # it shows true


#find
#find is used to find the index of any letter

#ex 1
m = "hari is a good boy and he  is also a badboy"
print(m.find("is"))   #output is (5) it shows index of the word

# ex ; 2
m = "hari is a good boy and he  is also a bad boy"
print(m.find("mn"))   #if not there means it shows (-1)

#index
#index is used to find word's index
#ex 1
o= "hari krishna"
print(o.index("ri"))   #it shows 2

#ex 2
# p = "hari krishna"
# print(p.index("kh"))  #it not there means it shows error




#isalnum
#ex 1
q = "harikrishna8"
print(q.isalnum())    #it shows true {when sentence have alphabets or numbers only}

#ex 2
r = "hari krishna @ 8"
print(r.isalnum())    #it shows false {when sentence have space (or) special characters}

#iaplpha
#ex 1
s = "Harikrishna"
print(s.isalpha())  #it show true {when sentence have only alphabets}

#ex 2
t = "hari krishna @ 8"
print(t.isalpha())  #it shows false {when sentence have space , special characters , numbers}

#islower
u = "hari krishna"
print(u.islower()) #it shows true, if any  single captial letter is there means it will show false

#isupper
v = "HARI KRISHNA"
print(v.isupper()) #it shows true , if any single small letter is       there means it will show false

#isprintable
w = "hari \& krishna @ 8 " 
print(w.isprintable()) # it shows true , if it contain non printed words like (\n) then it will show false

#isspace
#ex 1
x = "            "
print(x.isspace())  #it will show true

#ex 2
y = "     hari     krishna        "
print(y.isspace()) # it shows false , because if any word or letter present means it shows false

#istitle
#ex 1
z1 = "Akhil Hari" 
print(z1.istitle())  #it shows true , if we enter all small letters or all captial letters then it shows false

#ex 2
z2 = "Akhil hari"
print(z2.istitle()) #it shows  false


#swapcase
#it is sed for change the upper case to lower case and lower case to upper case 
a1 = "Hari Krish"
print(a1.swapcase()) #it shows hARI kRISHNA 

#title
#it is used for write the tittle 
#it write every starting lettr as a capital letter
b1 = "hari is a good boy , and he his also an anger person"
print(b1.title()) #then it shows Hari Is A Good Boy \ , And He Is An Anger Person