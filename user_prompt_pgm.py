largest = -1
smallest = None
count = 0
sum = 0
print ('before largest:',largest)
print('before smallest:',smallest)
print('before count:',count)
print('before sum:',sum)
print('before avg: dont know')
while True:
    nam = input('enter the number: ')
    if nam == 'done':
        break
    try:
        na = int(nam)
    except:
        print('invalid input')
        continue
    count = count + 1
    sum = sum + na
    if na > largest:
        largest = na
    if smallest is None:
        smallest = na
    elif na < smallest:
        smallest = na
print('largest:',largest)
print('smallest:',smallest)
print('count:',count)
print('sum:',sum)
print('avg:',sum/count)
