h_1 = int(input())
m_1 = int(input())
s_1 = int(input())
h_2 = int(input())
m_2 = int(input())
s_2 = int(input())
h_s = 3600
m_s = 60
t_1 = ((h_1 * h_s) + (m_1 * m_s) + s_1)
t_2 = ((h_2 * h_s) + (m_2 * m_s) + s_2)
print(int(t_2) - int(t_1))
