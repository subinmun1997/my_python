class Simple:
    def __init__(self,i):
        self.i=i
    def geti(self):
        return self.i

Simple.n=7
print(Simple.n)

s1=Simple(3)
s2=Simple(5)
print(s1.n,s1.geti(),sep=',')
print(s2.n,s2.geti(),sep=',')