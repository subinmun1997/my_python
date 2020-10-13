class Point3D:
    def __init__(self,x,y,z):
        self.x = x #x좌표
        self.y = y #y좌표
        self.z = z #z좌표
    def __str__(self):
        return '({0},{1},{2})'.format(self.x,self.y,self.z)

def main():
    p1 = Point3D(1,1,1)
    p2 = Point3D(24,17,31)
    print(p1)
    print(p2)
    print(p1.__dict__)
    print(p2.__dict__)

main()