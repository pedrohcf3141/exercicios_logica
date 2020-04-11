# 1066

par = 0
impar = 0
positivo = 0
negativo = 0
for n in range(0,5):
    x = int(input())
    if x % 2 == 0:
        par += 1
    else:
        impar += 1
    if x > 0:
        positivo += 1
    elif x < 0:
        negativo += 1

print('%i valor(es) par(es)'%par)
print('%i valor(es) impar(es)'%impar)
print('%i valor(es) positivo(s)'%positivo)
print('%i valor(es) negativo(s)'%negativo)
