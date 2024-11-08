#enumerate
# it is used for write the index of list, tuples,strings
# ex 1
levels = [1000,20000,3000,4000,5000,6000,7000,8000,9000,10000]
for index,money in enumerate(levels):
  print(index,money)


print("\n")

# Wrong
levels = [1000,20000,3000,4000,5000,6000,7000,8000,9000,10000]
for index,money in enumerate(levels,start=0):
  print(index ,money)
  if(index == 1):
    print("wrong")
    continue

print("\n")

# Correct
levels = [1000,20000,3000,4000,5000,6000,7000,8000,9000,10000]
for index,money in enumerate(levels,start=0):
  if(index == 1):
    print("wrong")
    continue
  print(index ,money)


