class Simple:
    def __init__(self,n,s):
        self._n = n
        self._s = s
    def __str__(self):
        return '{0}: {1}'.format(self._n,self._s)

def main():
    sp = Simple(10,'my')
    print(sp)
    print(sp.__dict__)
    sp.__dict__['_n'] += 10
    sp.__dict__['_s'] = 'your'
    print(sp)
    print(sp.__dict__)

main()