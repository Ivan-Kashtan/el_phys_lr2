# ВЛ с потерями
from numpy import array, round, average, empty, sqrt
from p3 import l0, l1

r0 = 0.096
f = array([50, 100000, 50])
#
# r = array([average([0.04395]), # 0.14735,
#            average([98.7]),  # 98.798,
#            average([0.04395])])  # 0.14735,
# l = array([average([1.7917e-3, 8.9176e-4, 8.876e-4]),
#            average([3.5802e-4, 3.3735e-4, 4.5744e-4]),
#            average([1.1154e-3, 1.112e-3, 1.2173e-3])])
# c = array([average([1.9409e-9, 1.6864e-9, 3.1075e-9]),
#            average([1.9409e-9, 1.6864e-9, 3.1075e-9]),
#            average([1.9409e-9, 1.6864e-9, 3.1075e-9])])

c = array([[[6.8796e-9, 1.9409e-9, 1.6864e-9],
           [1.9409e-9, 5.5971e-9, 3.1075e-9],
           [1.6864e-9,  3.1075e-9, 6.2663e-9]],

           [[6.8796e-9, 1.9409e-9, 1.6864e-9],
            [1.9409e-9, 5.5971e-9, 3.1075e-9],
            [1.6864e-9, 3.1075e-9, 6.2663e-9]],

           # [[6.8796e-9,  1.9409e-9,  1.6864e-9],
           # [1.9409e-9,  5.5971e-9,  3.1075e-9],
           # [1.6864e-9,  3.1075e-9,  6.2663e-9]]
           ])

c_t = array([[6.5970e-9,  1.4711e-9,  1.5667e-9,  9.9593e-10],
       [1.4711e-9,  4.5252e-9,  2.6533e-9,  3.7776e-9],
       [1.5667e-9,  2.6533e-9,  5.9931e-9,  9.6278e-10],
       [9.9593e-10,  3.7776e-9,  9.6278e-10,  2.2726e-9]])
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
v_c0_g = sqrt(1 / (l0 * c1_g))

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

c1_t = c_t_p + 3*c_t_pp
c0_t = c_t_p

z_c1 = sqrt(l1 / c1_t)
z_c0 = sqrt(l0 / c0_t)

v_c1 = sqrt(1 / (l1 * c1_t))
v_c0 = sqrt(1 / (l0 * c1_t))


# '''

print(c1_t)
print(c0_t)
