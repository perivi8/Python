# Static Method 

# while using @staticmethod we no need to use self

# ex 1 ( without @staticmethod)

class hari1 :
  def krishna1(self,n,m):
    # self.n = n
    # self.m =m
    print(n+m)

a = hari1()
a.krishna1(8,9)



# ex 2 

# class hari3 :
#   def do_that1 (a,b):    # we use self compulsary , other wise it show an error 
#    print(a*b)
  
# c = hari3()
# c.do_that1(5,5)


# ex 3  (using @staticmethod)



class hari2:
  @staticmethod
  def krishna2(a,b):
    print(a+b)

b = hari2()
b.krishna2(2,3)



# class hari4:
#   @staticmethod
#   def krishna4(self , a,b):   # no need to use  "self" , other wise it show an error
#     print(a+b)

# b = hari4()
# b.krishna4(2,6)






