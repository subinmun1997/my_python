fs='{0}...{1}...{2}'
ms = fs.format('Robot',125,'Box')
print(ms)

fs='{}.{}.{}'.format('Robot',125,'Box')
print(fs)

fs='{0}.{1}.{2}'.format('R',1,'B')
print(fs)

fs='{2}.{0}.{1}.{1}'.format('Robot',125,'Box')
print(fs)

fs='{toy}..{num}..{item}'.format(toy="Robot",num=125,item="Box")
print(fs)