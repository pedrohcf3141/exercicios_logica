#1064

p = []
for n in range(0,6):
    nro = float(input())
    if nro > 0:
        p.append(nro)
c = len(p)
m = sum(p) / c

print('%i valores positivos'%c)
print('%.1f'%m)

