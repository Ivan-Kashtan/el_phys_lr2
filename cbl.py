# ВЛ с тросами - cable
from numpy import array, round, average, empty, sqrt
from p1 import l0, l1

c_t = array([[6.5970e-9,  1.4711e-9,  1.5667e-9,  9.9593e-10],
             [1.4711e-9,  4.5252e-9,  2.6533e-9,  3.7776e-9],
             [1.5667e-9,  2.6533e-9,  5.9931e-9,  9.6278e-10],
             [9.9593e-10,  3.7776e-9,  9.6278e-10,  2.2726e-9]])

# c_t = array([[6.5970e-9,  1.4711e-9,  1.5667e-9,  0],
#              [1.4711e-9,  4.5252e-9,  2.6533e-9,  0],
#              [1.5667e-9,  2.6533e-9,  5.9931e-9,  0],
#              [9.9593e-10,  3.7776e-9,  9.6278e-10, 0]])

l = array([[1.7919e-003,  8.9176e-004,  8.8760e-004,  9.1480e-004],
             [8.9176e-004,  1.7946e-003,  9.9361e-004,  1.2356e-003],
             [8.8760e-004,  9.9361e-004,  1.7919e-003,  9.5901e-004],
             [9.1480e-004,  1.2356e-003,  9.5901e-004,  2.3591e-003]])
# '''
# Трос заземлен
c_t_g_p_a = c_t[0, 0] + c_t[0, 3]
c_t_g_p_b = c_t[1, 1] + c_t[1, 3]
c_t_g_p_c = c_t[2, 2] + c_t[2, 3]

c_t_g_p = average([c_t_g_p_a, c_t_g_p_b, c_t_g_p_c])
c_t_g_pp = average([c_t[0, 1], c_t[0, 2], c_t[1, 2]])
c1_g = c_t_g_p + 3*c_t_g_pp
c0_g = c_t_g_p

z_c1_g = sqrt(l1 / c1_g)
z_c0_g = sqrt(l0 / c0_g)

v_c1_g = sqrt(1 / (l1 * c1_g))
v_c0_g = sqrt(1 / (l0 * c0_g))

# '''
# '''
# Трос не заземлен
c_t_ = empty([len(c_t), len(c_t[0])])
# for i in c_t_[0]:
#     c_t_[]
# c_t_ = array([с_t[0, 1] c_t[]])
c_t_[0, 0] = c_t[0, 3] * c_t[3, 3] / sum(c_t[:, -1])
c_t_[0, 1] = c_t[0, 3] * c_t[1, 3] / sum(c_t[:, -1])
c_t_[0, 2] = c_t[0, 3] * c_t[2, 3] / sum(c_t[:, -1])

c_t_[1, 1] = c_t[1, 3] * c_t[3, 3] / sum(c_t[:, -1])
c_t_[1, 2] = c_t[1, 3] * c_t[2, 3] / sum(c_t[:, -1])
c_t_[2, 2] = c_t[2, 3] * c_t[3, 3] / sum(c_t[:, -1])

c_t_p_a = c_t[0, 0] + c_t_[0, 0]
c_t_p_b = c_t[1, 1] + c_t_[1, 1]
c_t_p_c = c_t[2, 2] + c_t_[2, 2]

c_ab = c_t[0, 1] + c_t_[0, 1]
c_ac = c_t[0, 2] + c_t_[0, 2]
c_bc = c_t[1, 2] + c_t_[1, 2]

c_t_p = average([c_t_p_a, c_t_p_b, c_t_p_c])
c_t_pp = average([c_ab, c_ac, c_bc])

c1 = c_t_p + 3*c_t_pp
c0 = c_t_p

z_c1 = sqrt(l1 / c1)
z_c0 = sqrt(l0 / c0)

v_c1 = sqrt(1 / (l1 * c1))
v_c0 = sqrt(1 / (l0 * c0))

# '''

print(v_c1)
print(v_c0)

print(v_c1_g)
print(v_c0_g)

print((c_t[:, -1]))
