data = 'harishsachin999@gmail.com cricket loves :cricket 113notout'
pos = data.find('h')
pos1 = data.find('s')
pos2 = data.find('a',pos1)
res1 = data[pos:pos2-1]
print(res1)
pos3 = data.find('.')
pos4 = data.find('l',pos3)
pos5 = data.find(' ',pos4)
res2 = data[pos4:pos5]
print(res2)
pos6 = data.find(':')
pos7 = data.find(' ',pos6)
res3 = data[pos6+1:pos7]
print(res3)
pos8 = data.find('1')
res4 = data[pos8:]
print(res4)
