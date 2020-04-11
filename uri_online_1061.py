# 1061
d = input().split()
d_1 = int(d[-1])
h_1,m_1,s_1 = input().split(':')
h_1 = int(h_1)
m_1 = int(m_1)
s_1 = int(s_1)
d = input().split()
d_2 = int(d[-1])
h_2,m_2,s_2 = input().split(':')
h_2 = int(h_2)
m_2 = int(m_2)
s_2 = int(s_2)

if s_2 < s_1:
    m_2 -= 1
    s_2 += 60
if m_2 < m_1:
    h_2 -= 1
    m_2 += 60
if h_2 < h_1:
    d_2 -= 1
    h_2 += 24
d = d_2 - d_1
h = h_2 - h_1
m = m_2 - m_1
s = s_2 - s_1
print('%i dia(s)'%d)
print('%i hora(s)'%h)
print('%i minuto(s)'%m)
print('%i segundo(s)'%s)


