#1080
m = 0
c = 0
for x in range(1,101):
    nro = int(input())
    if nro > m:
        m = nro
        c = x
print(m)
print(c)