# 1071

n_1 = int(input())
n_2 = int(input())

s = 0
menor = 0
maior = 0
if n_1 <= n_2:
       menor = n_1
       maior = n_2
else:
    menor = n_2
    maior = n_1
for x in range(menor+1,maior):
    if x % 2 != 0:
        s += x
print(s)
