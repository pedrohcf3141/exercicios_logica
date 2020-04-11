#1072

r = int(input())
i = []
o = []
for c in range(r):
    nro  = int(input())
    if 10 <= nro <= 20:
        i.append(nro)
    else:
        o.append(nro)
print('%i in'%len(i))
print('%i out'%len(o))

