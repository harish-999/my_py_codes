class human(): #class creation , intialisation basically init ->to define variables
    def __init__(self,surname,age):#self->objetcs,surname and age are other 2 variables
        self.surname=surname #surname is assinging to objects which are taken by self
        self.age=age   #age is assinging to objects which are taken by self
    def char(self): #defining method
        print('char is',self.surname,self.age)
harish = human('mali',23) #object creation ,init is not called anywhere in the code
bhanu = human('mali',25) #init is automatically called
harish.char()
bhanu.char()