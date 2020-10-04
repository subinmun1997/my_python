my=['Robot',125,'Box']

ps='{}.{}.{}'.format(*my)
print(ps)

my=['Box',(24,31)]
ps = '{0[0]}..{0[1]}..{0[2]}..{1[0]}..{1[1]}..'.format(*my)
print(ps)

d={'toy':'Robot','price':3500}
ps='toy={0[toy]}, price={0[price]}'.format(d)
print(ps)