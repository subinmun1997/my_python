class Simple:
    def seti(self,i):
        self.i = i
    def geti(self):
        return self.i
s1 = Simple()
s1.seti(200)
print(s1.geti())