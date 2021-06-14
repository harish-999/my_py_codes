from array import *
arr1 = array('i',[5,4,20,1])
arr2 = array('i',[1,4,5,2])
arr3 = array('i',[])
k = 0
for i in arr1:
    p = 0
    for j in arr2:
        x = (arr1[k]+arr2[p])
        k+=1
        p+=1
        arr3.append(x)
    print(arr3)
    break






