class human:            # Naming the class as Human
    def char(self):     # defining method as character,self is the object we are passing
        print('age:23,gender: male,height:5"9')
        print('age:25,gender: male,height:5"7')
harish = human()     # creating harish as a object and assiging it to human class
bhanu = human()      # creating bhanu as a object and assiging it to human class
harish.char()        # calling the method
bhanu.char()         # calling the method
print(type(harish))  # this says what class harish belongs to
print(type(bhanu))   # this says what class bhanu belongs to