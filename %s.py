s = 'My name is %s' % 'YOON'
print(s)

s = 'My friend %s is %d years old and %.1fcm tall.' % ('Jung',22,178.8)
print(s)

friends = [('Jung',22),('Hong',23),('Park',24)]
for f in friends:
    print('My friend %s is %d years old' % (f[0],f[1]))

s='My friend %s is %s years old and %scm tall.' %('Jung',22,178.9)
print(s)

print('%f' %25)
print('%d' %3.14)