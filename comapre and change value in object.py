class human():
   def __init__(self,name,age):
       self.name = name
       self.age = age
   def char(self):
       print(self.name,self.age)
   def compare(self,o2): # defining compare method to comapre two objects
        if self.age == o2.age:
            return True
        else:
            return False
o1 = human('harish',23) #constructor - passing values
o2 = human('bhanu',25) #constructor - Automatically calls init method

if o1.compare(o2):
    print('they are same')
else:
    print('they are different')
o1.char()
o2.char()



