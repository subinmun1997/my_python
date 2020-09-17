dc1={'코카콜라':900,'삼다수':450}
dc2={'새우깡':700,'콘치즈':850}
print(dc1)
print(dc2)

dc2['새우깡']=950
print(dc2)

if '새우깡' in dc2:
    dc2['새우깡']=850

print(dc2)

if '콘치즈' in dc1:
    print(dc1)

if '카페라떼' not in dc1:
    dc1['카페라떼'] = 1300

print(dc1)
print(dc2)