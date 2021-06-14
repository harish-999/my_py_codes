import re
inp = input('enter the file name: ')
fh = open(inp)
lst = list()
for i in fh:
    i = i.rstrip()
    y = re.findall('[0-9]+',i)
    if len(y) == 1:
            num = float(y[0])
            lst.append(num)
    elif len(y) == 2:
        num1 =float(y[0])
        num2 = float(y[1])
        lst.append(num1)
        lst.append(num2)
    elif len(y) == 3:
        num3 = float(y[0])
        num4 = float(y[1])
        num5 = float(y[2])
        lst.append(num3)
        lst.append(num4)
        lst.append(num5)
print('sum:',sum(lst))
