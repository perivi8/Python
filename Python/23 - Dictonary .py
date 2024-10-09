#Dictionary


#Ex 1
dic = {
  "hari"    : "First Name" ,
  "krishna" : "Second Name"
}
print(dic)
print(dic["hari"])

#Ex 2
dic1 = {1:"hari",2:"kriishna",3 :"perivi"}
print(dic1[3])

# Ex 3
dic1 = {1:"hari",
        2:"kriishna",
        3 :"perivi"}
print(dic1[2])


#Ex 4
info = {"name": "hari","age":20,"sex":"male"}
print(info)
print(info["age"])
# print(info["age1"]) # it shows error
print(info.get("age1"))  # .get is used for solve error 

# Ex 5
info = {"name": "hari","age":20,"sex":"male","mother":"hyma"}
print(info)
print(info.keys())
print(info.values())

for key in info:
  print(info[key])

#or

for hari in info.keys():
  print(info[hari])


for hari in info.keys():
  print(info)

# using F-string 

#by keys

data = {"name": "hari","age":20,"sex":"male","mother":"hyma"} 
print(data.keys())
for details in data.keys():
  print(f"the given key {details} and value is {data[details]}")


#by items
#by values  then use items syntax
 
data1 = {"name": "hari","age":20,"sex":"male","mother":"hyma"} 
print(data1.items())
for key,value in data1.items():
  print(f"the given data1 {key} and value is {value}")


