#1079

c = int(input())
for i in range(c):
    n1,n2,n3 = input().split(' ')
    m =(((float(n1)*2)+(float(n2)*3)+(float(n3)*5))/10)
    print('%.1f'%m)
