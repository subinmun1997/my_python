class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return '({0},{1},{2})'.format(self.x,self.y,self.z)

def main():
    p = Point3D(24,17,31)
    print(p.x,p.y,p.z)
    print(p.__dict__['x'],p.__dict__['y'],p.__dict__['z'])
    print(p.__dict__)

main()