def show_man(name,age,height):
    print(name,age,height,sep=',')

p=('Yoon',22,180)
show_man(*p)

p2=['Park',23,188]
show_man(*p2)
