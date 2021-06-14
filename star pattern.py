i = 1
while(i<5):
    print('# ',end='')
    j=1
    while(j<5):
        print('# ',end='')
        j=j+1
    i=i+1
    print()
#-------------------------------------------------------------------------------------
#anothe way
for i in range(0,4):
    for j in range(0,4):
        print('# ',end='')
    print()

