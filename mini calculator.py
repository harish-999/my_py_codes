def sum(a,b):
    c = a + b
    print('Addition of',a,b,'is:',c)
def sub(a,b):
    s = a - b
    print('subtraction of',a,b,'is:',s)
def mul(a,b):
    m = a * b
    print('multiplication of',a,b,'is:',m)
def div(a,b):
    d = a/b
    print('Division of',a,b,'is:',d)
print('welcome to mini calculator :)')
a = int(input('enter the first number:'))
b = int(input('enter the second number:'))
o = (input('enter the operation to perform:'))
if(o == '+'):
    sum(a,b)
elif(o == '-'):
    sub(a,b)
elif(o == '*'):
    mul(a,b)
elif(o=='/'):
    div(a,b)
else:
    print('invalid operation')