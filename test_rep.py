from numpy import diag, round, average, triu

from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Frame, NextPageTemplate, PageTemplate, PageBreak
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether
from reportlab.lib.units import cm

import cbl
from page_number import *

from styles import *
from eq import *
from page_number import *

import p1
import p2


sp_10 = Spacer(0, 10)
sp_20 = Spacer(0, 20)
sp_30 = Spacer(0, 30)
sp_40 = Spacer(0, 40)
sp_50 = Spacer(0, 50)
sp_70 = Spacer(0, 70)
sp_100 = Spacer(0, 100)

doc = SimpleDocTemplate(
    'test_rep.pdf',
    pagesize=A4,
    rightMargin=1 * cm, leftMargin=1 * cm,
    topMargin=1 * cm, bottomMargin=1.5 * cm, title='Кашталапов, Эн1-22, ЛР 2')


f = [
    # Paragraph('Расчет параметров ЛЭП с потерями', style=s_b),
    #  sp_10,
    #  fml('ВЛ без тросов, $f = 50$ Гц, $\\rho_з = 100$ Ом\u00B7м'),
    #  sp_40,
    #  fml(f'L = {p2.l[0]}'),
    #  sp_40,
    #  fml(f'С = {p2.c[0]}'),
    #  sp_20,
    #  fml('ВЛ без тросов, $f = 100$ кГц, $\\rho_з = 1000$ Ом\u00B7м'),
    #  sp_40,
    #  fml(f'L = {p2.l[1]}'),
    #  sp_40,
    #  fml(f'С = {p2.c[1]}'),
    #  sp_20,
    #  fml('ВЛ без тросов, $f = 50$ Гц, $\\rho_з = 100$ Ом\u00B7м'),
    #  sp_40,
    #  fml(f'L = {p2.l[2]}'),
    #  sp_40,
    #  fml(f'С = {p2.c[2]}'),
    #  sp_20,
    fml(f'$d = \\sqrt[3] {{ d_{{ab}} d_{{ac}} d_{{bc}} }}$'),

    # fml(f'$L_{{ф}} = (L_{{11}} + L_{{22}} + L_{{33}}) \\div 3; \\quad '
    #     f'L_{{ф}} =({p2.l_dg[0, 0]*10**3:.2f} + {p2.l_dg[0, 1]*10**3:.2f} + {p2.l_dg[0, 2]*10**3:.2f}) \\div 3 = '
    #     f'{p2.l_p[0]*10**3:.2f}$ мГн'),
    # sp_20,
    # fml(f'$L_{{фф}} = (L_{{12}} + L_{{13}} + L_{{23}}) \\div 3; \\quad '
    #     f'L_{{фф}} = ({round(p2.l_tr0*10**3, 2)}) \\div 3 = {average(p2.l_tr0)*10**3:.2f}$ мГн'),
    #     fml(f'$L_{{фф}} = (L_{{12}} + L_{{13}} + L_{{23}}) \\div 3; \\quad '
    #     f'C_{{фф}} =({(p2.l_tr[0, 0, 1])*10**3:.2f} + {float(p2.l_tr[0, 0, 2]*10**3):.2f} + {p2.l_tr[0, 1, 2]*10**3:.2f}) '
    #     f'\\div 3 = {p2.l_pp[0]*10**3:.2f}$ мГн'),
    # sp_20,
    #
    # fml(f'$C_{{ф}} = (C_{{11}} + C_{{22}} + C_{{33}}) \\div 3; \\quad '
    #     f'C_{{ф}} =({p2.c_dg[0, 0]*10**9:.2f} + {p2.c_dg[1]*10**9:.2f} + {p2.c_dg[2]*10**9:.2f}) '
    #     f'\\div 3 = {average(p2.c_dg*10**9):.2f}$ нФ'),
    # sp_20,
    # fml(f'$C_{{фф}} = (C_{{12}} + C_{{13}} + C_{{23}}) \\div 3; \\quad '
    #     f'C_{{фф}} =({(p2.c_tr[0, 1])*10**9:.2f} + {float(p2.c_tr[0, 2]*10**9):.2f} + {p2.c_tr[1, 2]*10**9:.2f}) '
    #     f'\\div 3 = {average(p2.c_tr*10**9):.2f}$ нФ'),
    # sp_20,
    #
    # fml(f'$C_1 = C_ф + 3C_{{фф}}; \\quad '
    #     f'C_1 = {p2.c_p[0] * 10**9:.2f} + 3\\cdot{p2.c_pp[0] * 10**9:.2f} = {p2.c1[0] * 10**9:.2f}$ нФ'),
    # sp_20,
    # fml(f'$C_0 = C_ф; \\quad '
    #     f'C_0 = {p2.c0[0] * 10**9:.2f}$ нФ'),
    # sp_20,
    # fml(f'$L_1 = L_ф + 3L_{{фф}}; \\quad '
    #     f'L_1 = {p2.l_p[0] * 10**3:.2f} + 3\\cdot{p2.l_pp[0] * 10**3:.2f} = {p2.c1[0] * 10**9:.2f}$ мГн'),
    # sp_20,
    # fml(f'$L_0 = L_ф; \\quad '
    #     f'L_0 = {p2.l0[0] * 10**3:.2f}$ мГн'),
    # sp_30,
    # fml(f'$Z_{{C_1}} = \\sqrt {{\\dfrac {{L_1}} {{C_1}} }}; \\quad '
    #     f'Z_{{C_1}} = \\sqrt {{\\dfrac {{ {p2.l1[0]:.2e} }} {{ {p2.c1[0]:.2e} }} }} = {p2.z_c1[0]:.1f}$ Ом'),
    # sp_30,
    # fml(f'$Z_{{C_0}} = \\sqrt {{\\dfrac {{L_0}} {{C_0}} }}; \\quad'
    #     f'Z_{{C_0}} = \\sqrt {{\\dfrac {{ {p2.l0[0]:.2e} }} {{ {p2.c0[0]:.2e} }} }} = {p2.z_c0[0]:.1f}$ Ом'),
    # sp_30,
    # fml(f'$v_1 = \\sqrt {{\\dfrac {{1}} {{L_1 C_1}} }}; \\quad'
    #     f'v_1 = \\sqrt {{\\dfrac {{ {1} }} {{{p2.l1[0]:.2e} \\cdot {p2.c1[0]:.2e} }} }} = {p2.v_c1[0] * 10**(-6):.3f}$ м/мкс'),
    # sp_30,
    # fml(f'$v_0 = \\sqrt {{ \\dfrac {{1}} {{L_0 C_0}} }}; \\quad'
    #     f'v_0 = \\sqrt {{ \\dfrac {{{1}}} {{ {p2.l0[0]:.2e} \\cdot {p2.c0[0]:.2e} }} }} = {p2.v_c0[0] * 10**(-6):.3f}$ м/мкс'),
    #
    #
    # l_p array([average(diag(l[0])), average(diag(l[1])), average(diag(l[2]))])
# l_pp = array([average(triu(l[0], k=1)), average(triu(l[1], k=1)), average(triu(l[2], k=1))])
#
# c_p = array([average(diag(c[0])), average(diag(c[1])), average(diag(c[2]))])
# c_pp = array([average(triu(c[0], k=1)), average(triu(c[1], k=1)), average(triu(c[2], k=1))])
#
# c1 = c_p + 3*c_pp
# c0 = c_p
#
# l1 = l_p + 3*l_pp
# l0 = l_p
#
# z_c1 = sqrt(l1 / c1)
# z_c0 = sqrt(l0 / c0)
#
# v_c1 = sqrt(1 / (l1 * c1))
# v_c0 = sqrt(1 / (l0 * c0))

     # fml('2-х фазная ВЛ с тросами, $f = 50$ Гц, $\\rho_з = 100$ Ом\u00B7м'),
     # sp_50,
     # fml(f'L = {cbl.l}'),
     # sp_50,
     # fml(f'С = {cbl.c_t}'),

    #  Paragraph('Трос заземлен', style=st_b_10_10),
    #  fml(f'$C_{{ф\u0020 a}} = C_{{11}} + C_{{14}}; \\quad '
    #      f'C_{{ф\u0020 a}} = {cbl.c_t[0, 0]*10**9:.3f} + {cbl.c_t[0, 2]*10**9:.3f} = {cbl.c_t_g_p_a*10**9:.3f}$ нФ'),
    #  sp_20,
    #  fml(f'$C_{{ф_\u0020 b}} = C_{{22}} + C_{{24}}; \\quad '
    #      f'C_{{ф\u0020 b}} = {cbl.c_t[1, 1]*10**9:.3f} + {cbl.c_t[1, 2]*10**9:.3f} = {cbl.c_t_g_p_b*10**9:.2f}$ нФ'),
    # sp_20,
    # fml(f'$C_{{ф\u0020 c}} = C_{{33}} + C_{{34}}; \\quad '
    #      f'C_C = {cbl.c_t[2, 2]*10**9:.3f} + {cbl.c_t[2, 3]*10**9:.3f} = {cbl.c_t_g_p_c*10**9:.3f}$ нФ'),
    # sp_20,
    # fml(f'$C_ф = (C_{{ф\u0020 a}} + C_{{ф\u0020 b}} + C_{{ф\u0020 c}}) \\div 3; \\quad '
    #      f'C_ф = ({cbl.c_t_g_p_a*10**9:.3f} + {cbl.c_t_g_p_b*10**9:.3f} + {cbl.c_t_g_p_с*10**9:.3f}) \\div 3 = '
    #     f'{cbl.c_t_g_p*10**9:.3f}$ нФ'),
    # sp_20,
    # fml(f'$C_{{фф}} = (C_{{ab}} + C_{{ac}} + C_{{bc}}) \\div 3; \\quad '
    #      f'C_{{фф}} = ({cbl.c_t[0, 1]*10**9:.3f} + {cbl.c_t[0, 2]*10**9:.3f} + {cbl.c_t[1, 2]*10**9:.3f}) \\div 3 = '
    #     f'{cbl.c_t_g_pp*10**9:.3f}$ нФ'),
    # sp_20,
    # fml(f'$C_1 = C_ф + 3C_{{фф}}; \\quad '
    #      f'C_1 = {cbl.c_t_p*10**9:.3f} + 3\\cdot{cbl.c_t_pp*10**9:.3f} = {cbl.c1_g*10**9:.3f}$ нФ'),
    # sp_20,
    #
    # fml(f'$C_0 = C_ф; \\quad '
    #      f'C_0 = {cbl.c0_g*10**9:.3f} + 3\\cdot{cbl.c_t_pp*10**9:.3f} = {cbl.c0_g*10**9:.3f}$ нФ'),
    # sp_30,
    # fml(f'$Z_{{C_1}} = \\sqrt {{\\dfrac {{L_1}} {{C_1}} }}; \\quad '
    #     f'Z_{{C_1}} = \\sqrt {{\\dfrac {{ {p1.l1:.2e} }} {{ {cbl.c1_g:.2e} }} }} = {cbl.z_c1_g:.2f}$ Ом'),
    # sp_30,
    # fml(f'$Z_{{C_0}} = \\sqrt {{\\dfrac {{L_0}} {{C_0}} }}; \\quad'
    #     f'Z_{{C_0}} = \\sqrt {{\\dfrac {{ {p1.l0:.2e} }} {{ {cbl.c0_g:.2e} }} }} = {cbl.z_c0_g:.2f}$ Ом'),
    # sp_30,
    # fml(f'$v_1 = \\sqrt {{\\dfrac {{1}} {{L_1 C_1}} }}; \\quad'
    #     f'v_1 = \\sqrt {{\\dfrac {{ {1} }} {{{p1.l1:.2e} \\cdot {cbl.c1_g:.2e} }} }} = {cbl.v_c1_g*10**(-6):.2e}$ м/мкс'),
    # sp_30,
    # fml(f'$v_0 = \\sqrt {{ \\dfrac {{1}} {{L_0 C_0}} }}; \\quad'
    #     f'v_0 = \\sqrt {{ \\dfrac {{{1}}} {{ {p1.l0:.2e} \\cdot {cbl.c0_g:.2e} }} }} = {cbl.v_c0_g*10**(-6):.2e}$ м/мкс'),
    #
    #
    # Paragraph('Трос изолирован', style=st_b_20_20),
    # fml(f'$C_{{12}}^* = \\dfrac {{C_{{14}} C_{{24}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
    #     f'C_{{12}}^* = \\dfrac {{{cbl.c_t[0, 3]*10**9:.2f} \\cdot {cbl.c_t[1, 3]*10**9:.2f} }}  {{{cbl.c_t[0, 3]*10**9:.2f} '
    #     f'+ {cbl.c_t[1, 3]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} ='
    #     f'{cbl.c_t_[0, 1]*10**9:.3f}$ нФ'),
    # sp_40,
    # fml(f'$C_{{11}}^* = \\dfrac {{C_{{14}} C_{{44}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
    #     f'C_{{11}}^* = \\dfrac {{{cbl.c_t[0, 3]*10**9:.2f} \\cdot {cbl.c_t[3, 3]*10**9:.2f} }}  {{{cbl.c_t[0, 3]*10**9:.2f} '
    #     f'+ {cbl.c_t[1, 3]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} '
    #     f'{cbl.c_t_[0, 0]*10**9:.3f}$ нФ'),
    # sp_40,
    # fml(f'$C_{{13}}^* = \\dfrac {{C_{{14}} C_{{34}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
    #     f'C_{{13}}^* = \\dfrac {{{cbl.c_t[0, 3]*10**9:.2f} \\cdot {cbl.c_t[2, 3]*10**9:.2f} }}  {{{cbl.c_t[0, 3]*10**9:.2f} '
    #     f'+ {cbl.c_t[1, 2]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} ='
    #     f'{cbl.c_t_[0, 2]*10**9:.3f}$ нФ'),
    # sp_40,
    # fml(f'$C_{{22}}^* = \\dfrac {{C_{{24}} C_{{34}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
    #     f'C_{{22}}^* = \\dfrac {{{cbl.c_t[1, 3]*10**9:.2f} \\cdot {cbl.c_t[3, 3]*10**9:.2f} }}  '
    #     f'{{{cbl.c_t[0, 3]*10**9:.2f} + {cbl.c_t[1, 3]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} ='
    #     f'{cbl.c_t_[1, 1]*10**9:.3f}$ нФ'),
    # sp_40,
    # fml(f'$C_{{23}}^* = \\dfrac {{C_{{24}} C_{{34}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
    #     f'C_{{23}}^* = \\dfrac {{{cbl.c_t[1, 3]*10**9:.2f} \\cdot {cbl.c_t[2, 3]*10**9:.2f} }}  '
    #     f'{{{cbl.c_t[0, 3]*10**9:.2f} + {cbl.c_t[1, 3]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} ='
    #     f'{cbl.c_t_[1, 2]*10**9:.3f}$ нФ'),
    # sp_40,
    # fml(f'$C_{{33}}^* = \\dfrac {{C_{{34}} C_{{44}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
    #     f'C_{{33}}^* = \\dfrac {{{cbl.c_t[2, 3]*10**9:.2f} \\cdot {cbl.c_t[3, 3]*10**9:.2f} }}  '
    #     f'{{{cbl.c_t[0, 3]*10**9:.2f} + {cbl.c_t[1, 3]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} ='
    #     f'{cbl.c_t_[2, 2]*10**9:.3f}$ нФ'),
    # sp_40,
    # fml(f'$C_{{фa}} = C_{{11}} + C_{{11}}^*; \\quad '
    #     f'C_{{фa}} = {cbl.c_t[0, 0]*10**9:.3f} + {cbl.c_t_[0, 0]*10**9:.3f} = {cbl.c_t_p_a*10**9:.3f}$ нФ'),
    # sp_20,
    # fml(f'$C_{{фb}} = C_{{22}} + C_{{22}}^*; \\quad '
    #     f'C_{{фb}} = {cbl.c_t[1, 1]*10**9:.2f} + {cbl.c_t_[1, 1]*10**9:.3f} = {cbl.c_t_p_b*10**9:.2f}$ нФ'),
    # sp_20,
    # fml(f'$C_{{фc}} = C_{{33}} + C_{{33}}^*; \\quad '
    #      f'C_{{фc}} = {cbl.c_t[2, 2]*10**9:.3f} + {cbl.c_t_[2, 2]*10**9:.3f} = {cbl.c_t_p_c*10**9:.3f}$ нФ'),
    # sp_20,
    # fml(f'$C_{{ab}} = C_{{12}} + C_{{12}}^* ; \\quad '
    #      f'C_{{ab}} = ({cbl.c_t[0, 1]*10**9:.3f} + {cbl.c_t_[0, 1]*10**9:.3f} = {cbl.c_ab*10**9:.3f}$ нФ'),
    # sp_20,
    # fml(f'$C_{{bc}} = C_{{13}} + C_{{13}}^* ; \\quad '
    #      f'C_{{bc}} = ({cbl.c_t[0, 2]*10**9:.3f} + {cbl.c_t_[0, 2]*10**9:.3f} = {cbl.c_ac*10**9:.3f}$ нФ'),
    # sp_20,
    # fml(f'$C_{{bc}} = C_{{23}} + C_{{23}}^* ; \\quad '
    #      f'C_{{bc}} = ({cbl.c_t[1, 2]*10**9:.3f} + {cbl.c_t_[1, 2]*10**9:.3f} = {cbl.c_bc*10**9:.3f}$ нФ'),
    # sp_20,
    # fml(f'$C_{{ф}} = (C_{{фa}} + C_{{фb}} + C_{{фc}}) \\div 3; \\quad '
    #      f'C_{{ф}} = ({cbl.c_t_p_a*10**9:.3f} + {cbl.c_t_p_b*10**9:.3f} + {cbl.c_t_p_b*10**9:.3f}) \\div 3 = '
    #     f'{cbl.c_t_p*10**9:.3f}$ нФ'),
    # sp_20,
    # fml(f'$C_{{фф}} = (C_{{ab}} + C_{{ac}} + C_{{bc}}) \\div 3; \\quad '
    #      f'C_{{фф}} = ({cbl.c_t_g_p_a*10**9:.3f} + {cbl.c_t_g_p_b*10**9:.3f} + {cbl.c_t_g_p_b*10**9:.3f}) \\div 3 = '
    #     f'{cbl.c_t_pp*10**9:.3f}$ нФ'),
    # sp_20,
    # fml(f'$C_1 = C_ф + 3C_{{фф}}; \\quad '
    #      f'C_1 = {cbl.c_t_p*10**9:.3f} + 3 \\cdot{cbl.c_t_pp*10**9:.3f} = {cbl.c1*10**9:.3f}$ нФ'),
    # sp_20,
    # fml(f'$C_0 = C_ф; \\quad '
    #      f'C_0 = {cbl.c_t_p*10**9:.3f}$ нФ'),
    # sp_30,
    # fml(f'$Z_{{C_1}} = \\sqrt {{\\dfrac {{L_1}} {{C_1}} }}; \\quad '
    #     f'Z_{{C_1}} = \\sqrt {{\\dfrac {{ {p1.l1:.2e} }} {{ {cbl.c1:.2e} }} }} = {cbl.z_c1:.2f}$ Ом'),
    # sp_30,
    # fml(f'$Z_{{C_0}} = \\sqrt {{\\dfrac {{L_0}} {{C_0}} }}; \\quad'
    #     f'Z_{{C_0}} = \\sqrt {{\\dfrac {{ {p1.l0:.2e} }} {{ {cbl.c0:.2e} }} }} = {cbl.z_c0:.2f}$ Ом'),
    # sp_30,
    # fml(f'$v_1 = \\sqrt {{\\dfrac {{1}} {{L_1 C_1}} }}; \\quad'
    #     f'v_1 = \\sqrt {{\\dfrac {{ {1} }} {{{p1.l1:.2e} \\cdot {cbl.c1:.2e} }} }} = {cbl.v_c1:.2e}$ м/с'),
    # sp_30,
    # fml(f'$v_0 = \\sqrt {{ \\dfrac {{1}} {{L_0 C_0}} }}; \\quad'
    #     f'v_0 = \\sqrt {{ \\dfrac {{ {1} }} {{ {p1.l0:.2e} \\cdot {cbl.c0:.2e} }} }} = {cbl.v_c0:.2e}$ м/с'),

    #
    # sp_20,
    # fml(f'$C_0 = \\dfrac {{1}} {{ \\alpha_ф + 2 \\alpha_{{фф}} }}; \\quad '
    #     f'C_0 = \\dfrac {{1}}  {{ {p1.a_p:.2e} + 2\\cdot {p1.a_pp:.2e} }} = {p1.c0:.2e}$ Ф'),
    # sp_30,
    # fml(f'$L_1 = L - M; \\quad L_1 = {p1.l_av:.2e} - {p1.m:.2e} = {p1.l1:.2e}$ Гн'),
    # sp_20,
    # fml(f'$L_0 = L + 2 M; \\quad {p1.l_av:.2e} + 2\\cdot {p1.m:.2e} = {p1.l0:.2e}$ Гн'),
    # sp_20,
    # fml(f'$C_ф = C_0; \\quad C_ф = {p1.c_p:.2e}$ Ф'),
    # sp_30,
    # fml(f'$C_{{фф}} = \\dfrac{{C_1 - C_{{ф}} }} {{2}}; '
    #     f'\\quad C_{{фф}} = \\dfrac {{{p1.c_p:.2e} - {p1.c_p:.2e}}} {{2}} = {p1.c_p:.2e}$ Ф'),
    # sp_20,
    # fml(f'$L_ф = L_0; \\quad L_ф = {p1.l_p:.2e}$ Гн'),
    # sp_30,
    # fml(f'$L_{{фф}} = \\dfrac{{L_1 - L_{{ф}} }} {{2}}; '
    #     f'\\quad L_{{фф}} = \\dfrac {{{p1.l_p:.2e} - {p1.l_p:.2e}}} {{2}} = {p1.l_p:.2e}$ Гн'),
    # sp_30,
     ]
doc.build(f, onLaterPages=addPageNumber)
