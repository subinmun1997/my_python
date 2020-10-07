class Fruit:
    pass

class Apple(Fruit):
    pass

class SuperApple(Apple):
    pass

sa = SuperApple()
print(isinstance(sa,SuperApple))
print(isinstance(sa,Apple))
print(isinstance(sa,Fruit))
