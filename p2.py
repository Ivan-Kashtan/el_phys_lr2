# С потерями
from numpy import array, diag, average, triu, sqrt, shape

r0 = 0.096
f = array([50, 100000, 50])
ro_g = array([100, 1000])
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

# '''
           [[6.8796e-9,  1.9409e-9,  1.6864e-9],
           [1.9409e-9,  5.5971e-9,  3.1075e-9],
           [1.6864e-9,  3.1075e-9,  6.2663e-9]],

           [[6.8796e-9, 1.9409e-9, 1.6864e-9],
           [1.9409e-9, 5.5971e-9, 3.1075e-9],
           [1.6864e-9, 3.1075e-9, 6.2663e-9]]])
# '''

l = array([[[1.7919e-003,  8.9176e-004,  8.8760e-004],
            [8.9176e-004,  1.7946e-003,  9.9361e-004],
            [8.8760e-004,  9.9361e-004,  1.7919e-003]],

           [[1.2367e-003,  3.5802e-004,  3.3735e-004],
           [3.5802e-004,  1.2753e-003,  4.5744e-004],
           [3.3735e-004,  4.5744e-004,  1.2367e-003]],

          [[2.0166e-003, 1.1154e-003, 1.1120e-003],
           [1.1154e-003, 2.0174e-003, 1.2173e-003],
           [1.1120e-003, 1.2173e-003, 2.0166e-003]]])

l_dg = array([diag(l[0]), diag(l[1]), diag(l[2])])
l_tr = array([triu(l[0], k=1), triu(l[1], k=1), triu(l[2], k=1)])

l_p = array([average(l_dg[0]), average(l_dg[1]), average(l_dg[2])])
# l_pp = array([average(l_tr[0]), average(l_tr[1]), average(l_tr[2])])
l_pp = array([(l_tr[0, 0, 1] + l_tr[0, 0, 2] + l_tr[0, 1, 2]) / 3, (l_tr[1, 0, 1] + l_tr[1, 0, 2] + l_tr[1, 1, 2]) / 3,
              ((l_tr[2, 0, 1] + l_tr[2, 0, 2] + l_tr[2, 1, 2]) / 3)])

c_dg = array([diag(c[0]), diag(c[1]), diag(c[2])])
c_tr = array([triu(c[0], k=1), triu(c[1], k=1), triu(c[2], k=1)])

c_p = array([average(c_dg[0]), average(c_dg[1]), average(c_dg[2])])
# c_pp = array([average(c_tr[0]), average(c_tr[1]), average(c_tr[2])])
c_pp = array([(c_tr[0, 0, 1] + c_tr[0, 0, 2] + c_tr[0, 1, 2]) / 3, (c_tr[1, 0, 1] + c_tr[1, 0, 2] + c_tr[1, 1, 2]) / 3,
              ((c_tr[2, 0, 1] + c_tr[2, 0, 2] + c_tr[2, 1, 2]) / 3)])
c1 = c_p + 3*c_pp
c0 = c_p

l1 = l_p + 3*l_pp
l0 = l_p

z_c1 = sqrt(l1 / c1)
z_c0 = sqrt(l0 / c0)

v_c1 = sqrt(1 / (l1 * c1))
v_c0 = sqrt(1 / (l0 * c0))

# print(v_c0)
# print(v_c1)
# print(l_p)
# print(l_pp)
# print(c_p)
# print(c_pp)
# print(triu(l, k=1))
# print(triu(c, k=1))
# print(shape(l_tr))
print(l_tr[0])
print(l_tr[0, 0, 1])
print(l_pp[0])
# c_dg[0, 1] - 0 строка, 1 столбец
# print(diag(l0))
