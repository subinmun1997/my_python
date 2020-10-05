class Simple:
    def __init__(self):
        self.i=0
    def seti(self,i):
        self.i=i
    def geti(self):
        return self.i

s=Simple()
print(s.geti())
s.seti(25)
print(s.geti())