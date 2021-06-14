from array import*
arr = array('i',[])
n = int(input('enter the length of array:'))
for i in range(n):
    x = int(input('enter the values in array:'))
    arr.append(x)
newarr = array('i',[])
k = n-1
for e in range(len(arr)):
    if(e<n):
        newarr.append(arr[k])
        k-=1
print(arr)
print(newarr)