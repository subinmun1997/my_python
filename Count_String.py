sr=["father","mother","brother"]
cnt=0
for s in sr:
    for c in s:
        if c == 'r':
            cnt+=1

print(cnt)