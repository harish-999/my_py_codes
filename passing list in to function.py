lst = list()
n = int(input('enter the no. of names:'))
for i in range(n):
    val = (input('enter the list of names:'))
    lst.append(val)
print(lst)
def names(lst):
    for i in lst:
        if(len(i)>=5):
            print(i,':greater than 5 letters')
        else:
            print(i,':less than 5 letters ')
names(lst)










