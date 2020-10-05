class SoSimple:
    def geti(self):
        return self.i

ss=SoSimple()
ss.i=23
print(ss.geti())

ss.hello = lambda : print('hi~')
ss.hello()

del ss.i
del ss.hello
