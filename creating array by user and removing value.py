from array import*
arr = array('i',[])
u = int(input('enter the length of array:'))
for i in range(u):
    x = int(input('enter the values:'))
    arr.append(x)
print(arr)
val = int(input('enter the value to be removed:'))
k = 0
for e in arr:
    if(val==e):
        print('index value of',val,':',k)
        arr.remove(val)
        print(arr)
        break
    k+=1



