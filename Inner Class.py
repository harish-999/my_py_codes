class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.lap = self.laptop() : creating object inside outter class
    def show(self):
        print(self.name ,self.age)
        # self.lap.show() : calling show so that both student and laptop info is obtained
    class laptop:
        def __init__(self,brand,cpu):
            self.brand = brand
            self.cpu = cpu
        def show(self):
            print(self.brand,self.cpu)
s1 = student('harish',23)
s2 = student('bhanu',25)
lap1 = student.laptop('dell','i5') #creating objects outside outer class
lap2 = student.laptop('hp','i7') #student. mentioned because laptop class is part of student class
s1.show() # here we are calling student and laptop info seperately
lap1.show()
s2.show()
lap2.show()
