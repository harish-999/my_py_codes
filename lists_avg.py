x = list()
while True:
    inp = input('enter the number: ')
    if inp == 'done':
        break
    value = float(inp)
    x.append(value)
print(sum(x))
print(len(x))
print('avg:',sum(x)/len(x))
