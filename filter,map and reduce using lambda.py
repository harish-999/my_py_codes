from functools import reduce
lst = [1,2,3,4,5,6,7,8,9,10]
o = list(filter(lambda a : a % 2 != 0,lst))
print('using filter:',o)
trip = list(map(lambda a : a * 3,o))
print('using map:',trip)
add = reduce(lambda a,b : a + b,trip)
mul = reduce(lambda a,b : a * b,trip)
print('using reduce:',add)
print('using reduce:',mul)

