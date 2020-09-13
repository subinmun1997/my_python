st=[1,2,3,4,5]
st.clear()
print(st)

st=[1,2,3,4,5]
st[:] = []
print(st)

st=[1,2,3,4,5]
st[2:] = []
print(st)

st=[1,2,3,4,5]
del st[:]
print(st)

st=[1,2,3,4,5]
del st[3:]
del st[0]
print(st)
