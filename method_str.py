class Simple:
    def __init__(self,i):
        self.i = i
    def __str__(self):
        return 'Simple({0})'.format(self.i)

s = Simple(10)
print(s)
print(s.__str__())