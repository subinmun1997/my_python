dc = {
    '코카콜라':900,
    '바나나맛우유':750,
    '비타500':600,
    '삼다수':450
}
print(dc)

v = dc['삼다수']
print(v)

dc['삼다수'] = 550
print(dc)

dc['카페라떼'] = 1300
print(dc)

del dc['비타500']
print(dc)