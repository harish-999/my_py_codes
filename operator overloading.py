class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1+self.m2
        m2 = other.m1 +other.m2
        s3 = student(m1,m2)
        return s3
    def __gt__(self, other):
        m1 = self.m1+self.m2
        m2 = other.m1 +other.m2
        if m1 >m2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
s1 = student(40,60)
s2 = student(60,120)
s3 = s1 + s2
if s1 > s2:
    print('s1 win')
else:
    print('s2 loss')
print(s1)
print(s2)
