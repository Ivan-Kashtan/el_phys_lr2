# 1.  Определение параметров трехфазной ВЛ без потерь
from numpy import pi, log, e, prod, array, sqrt

from in_dat import *

mu0 = 4*pi*1e-7
e0 =  8.8541878188e-12

# d = array([sqrt(x[0]**2 + (h[1] + h[0])**2), sum(x), sqrt(x[1]**2 + (h[1] + h[0])**2)])
# x = array([sqrt(x[0]**2 + (h[1] - h[0])**2), sum(xx), sqrt(x[1]**2 + (h[1] - h[0])**2)])
# D = array([2*h[0], sqrt((2*h[1])**2 + x[0]**2), sqrt((2*h[0])**2 + (x[0] + x[1])**2)])

d = array([sqrt(x[0]**2 + (h[1] - h[0])**2), sum(x), sqrt(x[1]**2 + (h[1] - h[0])**2)])
D = array([2*h[0], sqrt((2*h[1])**2 + x[0]**2), sqrt((h[0] + h[1])**2 + x[1]**2)])

h_av = prod(h)**(1/3)
d_av = prod(d)**(1/3)
D_av = prod(D)**(1/3)
# r_e = ()**(1/3)
l_av = mu0 / (2*pi) * log(2*h_av / r_w)
m = mu0 / (2*pi) * log(D_av / d_av)
a_p = 1 / (2*pi*e0) * log(2*h_av / r_w)
a_pp = 1 / (2*pi*e0) * log(D_av / d_av)

c1 = 1 / abs(a_p - a_pp)
c0 = 1 / (a_p + 2*a_pp)

c_p = c0
c_pp = (c1 - c_p) / 3

l1 = abs(l_av - m)
l0 = l_av + 2*m
# l_p =

# l_p = mu0 / (2*pi) * log(2*h / r)
# l_pp = mu0 / (2*pi) * log(2*h[0] / r)

z_c1_t = sqrt(l1 / c1)
z_c0_t = sqrt(l0 / c0)

v_c1_t = sqrt(1 / (l1 * c1))
v_c0_t = sqrt(1 / (l0 * c0))

# l_p = l1
# l_pp = l1 - l_p / 3  # ошибка ?
l_p = l0
l_pp = abs(l1 - l_p) / 3


# print(l_p.mean())
print(D_av)
print(l_p)
print(l_pp)
# print(l_p*10**3)
print(v_c0_t)
print(v_c1_t)

# print(D_av)
