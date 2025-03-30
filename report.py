from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Frame, NextPageTemplate, PageTemplate, PageBreak
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether
from reportlab.lib.units import cm
from reportlab.lib import colors

from numpy import pi

import p2
from title_list import *
from styles import *
from eq import *
from page_number import *

import p1
from in_dat import *
import cbl

sp_10 = Spacer(0, 10)
sp_20 = Spacer(0, 20)
sp_30 = Spacer(0, 30)
sp_40 = Spacer(0, 40)
sp_50 = Spacer(0, 50)
sp_100 = Spacer(0, 100)

doc = SimpleDocTemplate(
    'report.pdf',
    pagesize=A4,
    rightMargin=0.5*cm, leftMargin=2*cm,
    topMargin=1*cm, bottomMargin=1.5*cm, title='Кашталапов, Эн1-22, ЛР 2')

portrait_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='portrait_frame ')
landscape_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.height, doc.width, id='landscape_frame ')

doc.addPageTemplates([PageTemplate(id='portrait', frames=portrait_frame),
                      PageTemplate(id='landscape', frames=landscape_frame, pagesize=landscape(A4))])

f = [KeepTogether([mn, t_u, un, s_80, kaf, s_80, tp, title, var, s_130, fac, gr, st, tchr, mk, s_150, sity]),
     Paragraph('Цель работы', style=s_b),
     Paragraph('Расчитать погонные и волновые параметры воздушных линий электропередачи', style=s_m),
     Paragraph('Исходные данные', style=s_b),
     # Paragraph('Высота подвеса', style=s_m)
     Table(data=[[fml(f'$U_{{ном.}}$, кВ'), Paragraph('Провод', style=s_m),
                  fml(f'$d_п$, мм'), fml('$h_a$, м'), fml('$h_b$, м'),
                  fml('$h_c$, м'), fml('$d_{{ab}}$'), fml('$d_{{bc}}$')],
                 [fml(f'${u}$'), Paragraph('АС-300', style=s_m), fml(f'{d_w}'), fml(f'${h[0]}$'),
                  fml(f'${h[1]}$'), fml(f'${h[2]}$'), fml(f'{d[0]}'), fml(f'{d[1]}')]],
           spaceBefore=5, spaceAfter=5, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)]),

     Paragraph('Аналитический расчет параметров 3-х фазной ВЛ без потерь', style=st_b_10_20),
     fml(f'$h_{{ср}} = \\sqrt[3] {{h_a h_b h_c}}; \\quad'
         f' h_{{ср}} = \\sqrt[3] {{ {h[0]} \\cdot {h[1]} \\cdot {h[2]} }} = {p1.h_av:.2f}$ м'),
     sp_20,
     fml('f$d = \\sqrt[3] {{d_ab d_ac d_bc}}; \\quad'
         f'd = \\sqrt[3] {{{p1.d[0]:.1f} \\cdot {p1.d[1]:.1f} \\cdot {p1.d[2]:.1f} }} = {p1.d_av:.2f}$ м'),
     sp_20,
     # sqrt(x[0]**2 + (h[1] - h[0])**2), sum(x), sqrt(x[1]**2 + (h[1] - h[0])**2)]
     fml(f'$d_{{ab}} = \\sqrt{{d_{{ab}}^2 + \\left(h_b - h_a\\right)^2}}; \\quad'
         f'd_{{ab}} = \\sqrt{{ {d[0]}^2 + \\left({h[1]} - {h[0]} \\right)^2}} = {p1.d[0]:.2f}$ м'),
     sp_20,
     fml(f'$d_{{ac}} = d_{{ab}} + d_{{bc}}; \\quad'
         f'd_{{ac}} = {d[0]} + {d[1]} = {p1.d[1]:.2f}$ м'),
     sp_20,
     # sqrt(x[1]**2 + (h[1] - h[0])**2)]
     fml(f'$d_{{bc}} = \\sqrt{{d_{{ac}}^2 + \\left(h_b - h_a\\right)^2}}; \\quad'
         f'd_{{bc}} = \\sqrt{{ {d[1]}^2 + \\left({h[1]} - {h[0]} \\right)^2}} = {p1.d[2]:.2f}$ м'),
     sp_30,
     fml(f'$D = \\sqrt[3] {{D_{{ab}} D_{{ac}} D_{{bc}}}}; \\quad'
         f'D = \\sqrt[3] {{ {p1.D[0]:.1f} \\cdot {p1.D[1]:.1f} \\cdot {p1.D[2]:.1f} }} = {p1.D_av:.2f}$ м'),
     sp_20,
     # D = array([2*h[0], sqrt((2*h[1])**2 + d[0]**2), sqrt((2*h[0])**2 + (d[0] + d[1])**2)])
     fml(f'$D_{{ab}} = 2h_{{ab}}; \\quad D_{{ab}} = 2 \\cdot {h[0]} = {p1.D[0]:.2f}$ м'),
     sp_20,
     fml(f'$D_{{ac}} = \\sqrt{{\\left(2h_{{ac}}\\right)^2 + d_{{ab}}^2}}; \\quad'
         f'd_{{ac}} = \\sqrt{{\\left( 2\\cdot {h[1]} \\right)^2 + {d[0]}^2}} = {p1.D[1]:.2f}$ м'),
     sp_20,
     fml(f'$D_{{bc}} = \\sqrt{{2h_{{ab}}^2 + \\left(d_{{ab}} + d_{{ac}}\\right)^2}}; \\quad'
         f'D_{{bc}} = \\sqrt{{(2\\cdot {h[0]})^2 + \\left({d[0]} + {d[1]} \\right)^2}} = {p1.D[2]:.2f}$ м'),
     sp_30,
     fml(f'$L = L_a = L_b = L_c = \\dfrac {{\\mu_0}} {{2 \\pi}} \\ln '
         f'\\dfrac{{2 h_{{ср}} }} {{r_э}}; \\quad'
         f'\\dfrac {{ {p1.mu0:.2e} }} {{ 2\\cdot {pi:.2f} }} \\ln '
         f'\\dfrac{{2 {p1.h_av:.2f} }} {{ {p1.r_w} }} = {p1.l_av*10**6:.2f}$ мкГн'),
     sp_30,
     fml(f'$M = M_{{ab}} = M_{{ac}} = M_{{bc}} = \\dfrac {{ \\mu_0}}  {{2\\cdot \\pi}} \\ln '
         f'\\dfrac{{2\\cdot D}} {{d}}; \\quad '
         f'\\dfrac {{{p1.mu0:.1e}}}  {{2\\cdot {pi:.2f} }} \\ln '
         f'\\dfrac{{2\\cdot{p1.D_av:.2f} }} {{ {p1.d_av:.1f} }} = {p1.m*10**6:.2f}$ мкГн'),
     sp_30,
     fml(f'$\\alpha_ф = \\dfrac {{1}} {{2 \\pi \\epsilon_0 }}\\ln '
         f'\\dfrac{{2 h_{{ср}} }} {{r_э}}; \\quad'
         f'\\alpha_ф = \\dfrac {{1}} {{2\\cdot {pi:.2f} \\cdot {p1.e0:.2e} }}\\ln '
         f'\\dfrac{{2\\cdot{p1.h_av:.2f} }} {{ {p1.r_w:.2f} }} = {p1.a_p:.2e}$'),
     sp_30,
          fml(f'$\\alpha_{{фф}} = \\dfrac {{1}} {{2 \\cdot \\pi \\epsilon_0 }} \\ln '
         f'\\dfrac{{ 2\\cdot D }} {{d}}; \\quad'
         f'\\alpha_{{фф}} = \\dfrac {{1}} {{2\\cdot {pi:.2f} \\cdot {p1.e0:.2e} }} \\ln '
         f'\\dfrac{{ 2\\cdot{p1.D_av:.2f} }} {{ {p1.d_av:.2f} }} = {p1.a_pp:.2e}$'),
     sp_30,
     fml(f'$C_1 = \\dfrac {{1}}  {{\\alpha_ф - \\alpha_{{фф}} }}; \\quad '
         f'C_1 = \\dfrac {{1}} {{ {p1.a_p:.2e} - {p1.a_pp:.2e} }} = {p1.c1:.2e}$ Ф'),
     sp_30,
     fml(f'$C_0 = \\dfrac {{1}} {{ \\alpha_ф + 2 \\alpha_{{фф}} }}; \\quad '
         f'C_0 = \\dfrac {{1}}  {{ {p1.a_p:.2e} + 2\\cdot {p1.a_pp:.2e} }} = {p1.c0:.2e}$ Ф'),
     sp_30,
     fml(f'$L_1 = L - M; \\quad L_1 = {p1.l_av:.2e} - {p1.m:.2e} = {p1.l1:.2e}$ Гн'),
     sp_20,
     fml(f'$L_0 = L + 2 M; \\quad {p1.l_av:.2e} + 2\\cdot {p1.m:.2e} = {p1.l0:.2e}$ Гн'),
     sp_20,
     fml(f'$C_ф = C_0; \\quad C_ф = {p1.c_p:.2e}$ Ф'),
     sp_30,
     fml(f'$C_{{фф}} = \\dfrac{{C_1 - C_{{ф}} }} {{3}}; '
         f'\\quad C_{{фф}} = \\dfrac {{{p1.c_p:.2e} - {p1.c_p:.2e}}} {{3}} = {p1.c_p:.2e}$ Ф'),
     sp_20,
     fml(f'$L_ф = L_0; \\quad L_ф = {p1.l_p:.2e}$ Гн'),
     sp_30,
     fml(f'$L_{{фф}} = \\dfrac{{L_1 - L_{{ф}} }} {{3}}; '
         f'\\quad L_{{фф}} = \\dfrac {{{p1.l_p:.2e} - {p1.l_p:.2e}}} {{3}} = {p1.l_p:.2e}$ Гн'),
     sp_30,
     fml(f'$Z_{{C_1}} = \\sqrt {{\\dfrac {{L_1}} {{C_1}} }}; \\quad '
         f'Z_{{C_1}} = \\sqrt {{\\dfrac {{ {p1.l1:.2e} }} {{ {p1.c1:.2e} }} }} = {p1.z_c1_t:.2e}$ Ом'),
     sp_30,
     fml(f'$Z_{{C_0}} = \\sqrt {{\\dfrac {{L_0}} {{C_0}} }}; \\quad'
         f'Z_{{C_0}} = \\sqrt {{\\dfrac {{ {p1.l0:.2e} }} {{ {p1.c0:.2e} }} }} = {p1.z_c0_t:.2e}$ Ом'),
     sp_30,
     fml(f'$v_1 = \\sqrt {{\\dfrac {{1}} {{L_1 C_1}} }}; \\quad'
         f'v_1 = \\sqrt {{\\dfrac {{ {1} }} {{{p1.l1:.2e} \\cdot {p1.c1:.2e} }} }} = {p1.v_c1_t:.2e}$ м/с'),
     sp_30,
     fml(f'$v_0 = \\sqrt {{ \\dfrac {{1}} {{L_0 C_0}} }}; \\quad'
         f'v_0 = \\sqrt {{ \\dfrac {{ {1} }} {{ {p1.l0:.2e} \\cdot {p1.c0:.2e} }} }} = {p1.v_c0_t:.2e}$ м/с'),
     sp_30,
     Paragraph('Расчет параметров ЛЭП с потерями', style=s_b),
     sp_10,
     fml('3-х фазная ВЛ без тросов, $f = 50$ Гц, $\\rho_з = 100$ Ом\u00B7м'),
     sp_40,
     fml(f'L = {p2.l[0]}'),
     sp_40,
     fml(f'С = {p2.c[0]}'),
     sp_20,
     fml('3-х фазная ВЛ без тросов, $f = 100$ кГц, $\\rho_з = 1000$ Ом\u00B7м'),
     sp_40,
     fml(f'L = {p2.l[1]}'),
     sp_40,
     fml(f'С = {p2.c[1]}'),
     sp_20,
     fml('3-х фазная ВЛ без тросов, $f = 50$ Гц, $\\rho_з = 100$ Ом\u00B7м'),
     sp_40,
     fml(f'L = {p2.l[2]}'),
     sp_40,
     fml(f'С = {p2.c[2]}'),
     Paragraph('Расчет параметров ЛЭП с тросом', style=st_b_10_10),
     fml('3-х фазная ВЛ с тросом, $f = 50$ Гц, $\\rho_з = 100$ Ом\u00B7м'),
     sp_50,
     fml(f'L = {cbl.l}'),
     sp_50,
     fml(f'С = {cbl.c_t}'),
Paragraph('Трос заземлен', style=st_b_10_10),
     fml(f'$C_{{ф\u0020 a}} = C_{{11}} + C_{{14}}; \\quad '
         f'C_{{ф\u0020 a}} = {cbl.c_t[0, 0]*10**9:.3f} + {cbl.c_t[0, 2]*10**9:.3f} = {cbl.c_t_g_p_a*10**9:.3f}$ нФ'),
     sp_20,
     fml(f'$C_{{ф_\u0020 b}} = C_{{22}} + C_{{24}}; \\quad '
         f'C_{{ф\u0020 b}} = {cbl.c_t[1, 1]*10**9:.3f} + {cbl.c_t[1, 2]*10**9:.3f} = {cbl.c_t_g_p_b*10**9:.2f}$ нФ'),
    sp_20,
    fml(f'$C_{{ф\u0020 c}} = C_{{33}} + C_{{34}}; \\quad '
         f'C_C = {cbl.c_t[2, 2]*10**9:.3f} + {cbl.c_t[2, 3]*10**9:.3f} = {cbl.c_t_g_p_c*10**9:.3f}$ нФ'),
    sp_20,
    fml(f'$C_ф = (C_{{ф\u0020 a}} + C_{{ф\u0020 b}} + C_{{ф\u0020 c}}) \\div 3; \\quad '
         f'C_ф = ({cbl.c_t_g_p_a*10**9:.3f} + {cbl.c_t_g_p_b*10**9:.3f} + {cbl.c_t_g_p_c*10**9:.3f}) \\div 3 = '
        f'{cbl.c_t_g_p*10**9:.3f}$ нФ'),
    sp_20,
    fml(f'$C_{{фф}} = (C_{{ab}} + C_{{ac}} + C_{{bc}}) \\div 3; \\quad '
         f'C_{{фф}} = ({cbl.c_t[0, 1]*10**9:.3f} + {cbl.c_t[0, 2]*10**9:.3f} + {cbl.c_t[1, 2]*10**9:.3f}) \\div 3 = '
        f'{cbl.c_t_g_pp*10**9:.3f}$ нФ'),
    sp_20,
    fml(f'$C_1 = C_ф + 3C_{{фф}}; \\quad '
         f'C_1 = {cbl.c_t_p*10**9:.3f} + 3\\cdot{cbl.c_t_pp*10**9:.3f} = {cbl.c1_g*10**9:.3f}$ нФ'),
    sp_20,

    fml(f'$C_0 = C_ф; \\quad '
         f'C_0 = {cbl.c0_g*10**9:.3f} + 3\\cdot{cbl.c_t_pp*10**9:.3f} = {cbl.c0_g*10**9:.3f}$ нФ'),
    sp_30,
    fml(f'$Z_{{C_1}} = \\sqrt {{\\dfrac {{L_1}} {{C_1}} }}; \\quad '
        f'Z_{{C_1}} = \\sqrt {{\\dfrac {{ {p1.l1:.2e} }} {{ {cbl.c1_g:.2e} }} }} = {cbl.z_c1_g:.2f}$ Ом'),
    sp_30,
    fml(f'$Z_{{C_0}} = \\sqrt {{\\dfrac {{L_0}} {{C_0}} }}; \\quad'
        f'Z_{{C_0}} = \\sqrt {{\\dfrac {{ {p1.l0:.2e} }} {{ {cbl.c0_g:.2e} }} }} = {cbl.z_c0_g:.2f}$ Ом'),
    sp_30,
    fml(f'$v_1 = \\sqrt {{\\dfrac {{1}} {{L_1 C_1}} }}; \\quad'
        f'v_1 = \\sqrt {{\\dfrac {{ {1} }} {{{p1.l1:.2e} \\cdot {cbl.c1_g:.2e} }} }} = {cbl.v_c1_g*10**(-6):.2e}$ м/мкс'),
    sp_30,
    fml(f'$v_0 = \\sqrt {{ \\dfrac {{1}} {{L_0 C_0}} }}; \\quad'
        f'v_0 = \\sqrt {{ \\dfrac {{{1}}} {{ {p1.l0:.2e} \\cdot {cbl.c0_g:.2e} }} }} = {cbl.v_c0_g*10**(-6):.2e}$ м/мкс'),

    Paragraph('Трос изолирован', style=st_b_20_20),
    fml(f'$C_{{12}}^* = \\dfrac {{C_{{14}} C_{{24}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
        f'C_{{12}}^* = \\dfrac {{{cbl.c_t[0, 3]*10**9:.2f} \\cdot {cbl.c_t[1, 3]*10**9:.2f} }}  {{{cbl.c_t[0, 3]*10**9:.2f} '
        f'+ {cbl.c_t[1, 3]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} ='
        f'{cbl.c_t_[0, 1]*10**9:.3f}$ нФ'),
    sp_40,
    fml(f'$C_{{11}}^* = \\dfrac {{C_{{14}} C_{{44}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
        f'C_{{11}}^* = \\dfrac {{{cbl.c_t[0, 3]*10**9:.2f} \\cdot {cbl.c_t[3, 3]*10**9:.2f} }}  {{{cbl.c_t[0, 3]*10**9:.2f} '
        f'+ {cbl.c_t[1, 3]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} '
        f'{cbl.c_t_[0, 0]*10**9:.3f}$ нФ'),
    sp_40,
    fml(f'$C_{{13}}^* = \\dfrac {{C_{{14}} C_{{34}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
        f'C_{{13}}^* = \\dfrac {{{cbl.c_t[0, 3]*10**9:.2f} \\cdot {cbl.c_t[2, 3]*10**9:.2f} }}  {{{cbl.c_t[0, 3]*10**9:.2f} '
        f'+ {cbl.c_t[1, 2]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} ='
        f'{cbl.c_t_[0, 2]*10**9:.3f}$ нФ'),
    sp_40,
    fml(f'$C_{{22}}^* = \\dfrac {{C_{{24}} C_{{34}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
        f'C_{{22}}^* = \\dfrac {{{cbl.c_t[1, 3]*10**9:.2f} \\cdot {cbl.c_t[3, 3]*10**9:.2f} }}  '
        f'{{{cbl.c_t[0, 3]*10**9:.2f} + {cbl.c_t[1, 3]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} ='
        f'{cbl.c_t_[1, 1]*10**9:.3f}$ нФ'),
    sp_40,
    fml(f'$C_{{23}}^* = \\dfrac {{C_{{24}} C_{{34}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
        f'C_{{23}}^* = \\dfrac {{{cbl.c_t[1, 3]*10**9:.2f} \\cdot {cbl.c_t[2, 3]*10**9:.2f} }}  '
        f'{{{cbl.c_t[0, 3]*10**9:.2f} + {cbl.c_t[1, 3]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} ='
        f'{cbl.c_t_[1, 2]*10**9:.3f}$ нФ'),
    sp_40,
    fml(f'$C_{{33}}^* = \\dfrac {{C_{{34}} C_{{44}}}}  {{C_{{14}} + C_{{24}} + C_{{34}} + C_{{44}}}}; \\quad'
        f'C_{{33}}^* = \\dfrac {{{cbl.c_t[2, 3]*10**9:.2f} \\cdot {cbl.c_t[3, 3]*10**9:.2f} }}  '
        f'{{{cbl.c_t[0, 3]*10**9:.2f} + {cbl.c_t[1, 3]*10**9:.2f} + {cbl.c_t[2, 3]*10**9:.2f} + {cbl.c_t[3, 3]*10**9:.2f}}} ='
        f'{cbl.c_t_[2, 2]*10**9:.3f}$ нФ'),
    sp_40,
    fml(f'$C_{{фa}} = C_{{11}} + C_{{11}}^*; \\quad '
        f'C_{{фa}} = {cbl.c_t[0, 0]*10**9:.3f} + {cbl.c_t_[0, 0]*10**9:.3f} = {cbl.c_t_p_a*10**9:.3f}$ нФ'),
    sp_20,
    fml(f'$C_{{фb}} = C_{{22}} + C_{{22}}^*; \\quad '
        f'C_{{фb}} = {cbl.c_t[1, 1]*10**9:.2f} + {cbl.c_t_[1, 1]*10**9:.3f} = {cbl.c_t_p_b*10**9:.2f}$ нФ'),
    sp_20,
    fml(f'$C_{{фc}} = C_{{33}} + C_{{33}}^*; \\quad '
         f'C_{{фc}} = {cbl.c_t[2, 2]*10**9:.3f} + {cbl.c_t_[2, 2]*10**9:.3f} = {cbl.c_t_p_c*10**9:.3f}$ нФ'),
    sp_20,
    fml(f'$C_{{ab}} = C_{{12}} + C_{{12}}^* ; \\quad '
         f'C_{{ab}} = ({cbl.c_t[0, 1]*10**9:.3f} + {cbl.c_t_[0, 1]*10**9:.3f} = {cbl.c_ab*10**9:.3f}$ нФ'),
    sp_20,
    fml(f'$C_{{bc}} = C_{{13}} + C_{{13}}^* ; \\quad '
         f'C_{{bc}} = ({cbl.c_t[0, 2]*10**9:.3f} + {cbl.c_t_[0, 2]*10**9:.3f} = {cbl.c_ac*10**9:.3f}$ нФ'),
    sp_20,
    fml(f'$C_{{bc}} = C_{{23}} + C_{{23}}^* ; \\quad '
         f'C_{{bc}} = ({cbl.c_t[1, 2]*10**9:.3f} + {cbl.c_t_[1, 2]*10**9:.3f} = {cbl.c_bc*10**9:.3f}$ нФ'),
    sp_20,
    fml(f'$C_{{ф}} = (C_{{фa}} + C_{{фb}} + C_{{фc}}) \\div 3; \\quad '
         f'C_{{ф}} = ({cbl.c_t_p_a*10**9:.3f} + {cbl.c_t_p_b*10**9:.3f} + {cbl.c_t_p_b*10**9:.3f}) \\div 3 = '
        f'{cbl.c_t_p*10**9:.3f}$ нФ'),
    sp_20,
    fml(f'$C_{{фф}} = (C_{{ab}} + C_{{ac}} + C_{{bc}}) \\div 3; \\quad '
         f'C_{{фф}} = ({cbl.c_t_g_p_a*10**9:.3f} + {cbl.c_t_g_p_b*10**9:.3f} + {cbl.c_t_g_p_b*10**9:.3f}) \\div 3 = '
        f'{cbl.c_t_pp*10**9:.3f}$ нФ'),
    sp_20,
    fml(f'$C_1 = C_ф + 3C_{{фф}}; \\quad '
         f'C_1 = {cbl.c_t_p*10**9:.3f} + 3 \\cdot{cbl.c_t_pp*10**9:.3f} = {cbl.c1*10**9:.3f}$ нФ'),
    sp_20,
    fml(f'$C_0 = C_ф; \\quad '
         f'C_0 = {cbl.c_t_p*10**9:.3f}$ нФ'),
    sp_30,
    fml(f'$Z_{{C_1}} = \\sqrt {{\\dfrac {{L_1}} {{C_1}} }}; \\quad '
        f'Z_{{C_1}} = \\sqrt {{\\dfrac {{ {p1.l1:.2e} }} {{ {cbl.c1:.2e} }} }} = {cbl.z_c1:.2f}$ Ом'),
    sp_30,
    fml(f'$Z_{{C_0}} = \\sqrt {{\\dfrac {{L_0}} {{C_0}} }}; \\quad'
        f'Z_{{C_0}} = \\sqrt {{\\dfrac {{ {p1.l0:.2e} }} {{ {cbl.c0:.2e} }} }} = {cbl.z_c0:.2f}$ Ом'),
    sp_30,
    fml(f'$v_1 = \\sqrt {{\\dfrac {{1}} {{L_1 C_1}} }}; \\quad'
        f'v_1 = \\sqrt {{\\dfrac {{ {1} }} {{{p1.l1:.2e} \\cdot {cbl.c1:.2e} }} }} = {cbl.v_c1:.2e}$ м/с'),
    sp_30,
    fml(f'$v_0 = \\sqrt {{ \\dfrac {{1}} {{L_0 C_0}} }}; \\quad'
        f'v_0 = \\sqrt {{ \\dfrac {{ {1} }} {{ {p1.l0:.2e} \\cdot {cbl.c0:.2e} }} }} = {cbl.v_c0:.2e}$ м/с'),



     # Paragraph('Исследование влияния тросов на параметры ВЛ', style=s_m),
     # fml(f'$Z_{{C_1}} = \\sqrt {{\\dfrac {{ {p1.l1:.2e} }} {{ {p1.c1:.2e} }} }} = {p1.z_c1_t:.2e}$ м/с'),

     NextPageTemplate('landscape'),
     PageBreak(),
     Table(data=[[Paragraph('№', style=s_m), Paragraph('Параметр', style=s_m), fml('$L_ф$'), fml('$L_{фф}$'),
                  fml('$L_{1}$'), fml('$L_{0}$'), fml('$C_{ф}$'), fml('$C_{фф}$'), fml('$C_{1}$'), fml('$C_{0}$'),
                  fml('$z_{1}$'), fml('$z_{0}$'), fml('$v_{1}$'), fml('$v_{0}$')],
                 [Paragraph(' ', style=s_m), Paragraph('Размерность', style=s_m), fml(f'мГн/км'),
                  fml(f'мГн/км'), fml('мГн/км'), fml('мГн/км'), fml('нФ/км'), fml('нФ/км'), fml('нФ/км'),
                  fml('нФ/км'), fml('Ом'), fml('Ом'), fml('м/мкс'), fml('м/мкс')],
                 [Paragraph('ВЛ без потерь', style=s_m),
                  Paragraph('Транспонинрованная линия без тросов', style=s_m),
                  fml(f'${p1.l_p*10**3:.5f}$'), fml(f'${p1.l_pp*10**3:.5f}$'), fml(f'{p1.l1*10**3:.5f}'),
                  fml(f'{p1.l0*10**3:.5f}'), fml(f'${p1.c_p*10**9:.5f}$'), fml(f'${p1.c_pp*10**9:.3f}$'),
                  fml(f'${p1.c1*10**9:.5f}$'), fml(f'${p1.c0*10**9:.5f}$'), fml(f'${p1.z_c1_t:.1f}$'),
                  fml(f'${p1.z_c0_t:.3f}$'), fml(f'${p1.v_c1_t*10**-6:.1f}$'), fml(f'${p1.v_c0_t*10**-6:.1f}$')],
                 [Paragraph('ВЛ без тросов', style=s_m),
                  Paragraph('f = 50 Гц, \n \u03c1_з = 100 Ом\u00B7м', style=s_m),
                  fml(f'${p2.l_p[0]*10**3:.3f}$'), fml(f'${p2.l_pp[0]*10**3:.3f}$'), fml(f'{p2.l1[0]*10**3:.3f}'),
                  fml(f'{p2.l0[0]*10**3:.3f}'), fml(f'${p2.c_p[0]*10**9:.3f}$'), fml(f'${p2.c_pp[0]*10**9:.3f}$'),
                  fml(f'${p2.c1[0]*10**9:.3f}$'), fml(f'${p2.c0[0]*10**9:.3f}$'), fml(f'${p2.z_c0[0]:.2f}$'),
                  fml(f'${p2.z_c1[0]:.2f}$'), fml(f'${p2.v_c1[0]*10**-6:.3f}$'), fml(f'${p2.v_c0[0]*10**-6:.3f}$')],
                 [Paragraph('', style=s_m),
                  Paragraph('f = 1000 кГц, \n \u03c1_з = 100 Ом\u00B7м', style=s_m),
                  fml(f'${p2.l_p[1]*10**3:.3f}$'), fml(f'${p2.l_pp[1]*10**3:.3f}$'), fml(f'{p2.l1[1]*10**3:.3f}'),
                  fml(f'{p2.l0[1]*10**3:.3f}'), fml(f'${p2.c_p[1]*10**9:.3f}$'), fml(f'${p2.c_pp[1]*10**9:.3f}$'),
                  fml(f'${p2.c1[1]*10**9:.3f}$'), fml(f'${p2.c0[1]*10**9:.3f}$'), fml(f'${p2.z_c0[1]:.2f}$'),
                  fml(f'${p2.z_c1[1]:.2f}$'), fml(f'${p2.v_c1[1]*10**-6:.3f}$'), fml(f'${p2.v_c0[1]*10**-6:.3f}$')],
                 [Paragraph('', style=s_m),
                  Paragraph('f = 50 Гц, \n \u03c1_з = 1000 Ом\u00B7м', style=s_m),
                  fml(f'${p2.l_p[2]*10**3:.3f}$'), fml(f'${p2.l_pp[2]*10**3:.3f}$'), fml(f'{p2.l1[2]*10**3:.3f}'),
                  fml(f'{p2.l0[2]*10**3:.3f}'), fml(f'${p2.c_p[2]*10**9:.3f}$'), fml(f'${p2.c_pp[2]*10**9:.3f}$'),
                  fml(f'${p2.c1[2]*10**9:.3f}$'), fml(f'${p2.c0[2]*10**9:.3f}$'), fml(f'${p2.z_c0[2]:.2f}$'),
                  fml(f'${p2.z_c1[2]:.2f}$'), fml(f'${p2.v_c1[2]*10**-6:.3f}$'), fml(f'${p2.v_c0[2]*10**-6:.3f}$')],

                 [Paragraph(f'Трос заземлен', style=s_m),
                  Paragraph('f = 50 Гц, \u03c1_з = 100 Ом\u00B7м', style=s_m), fml(f'${p2.l_p[0]*10**3:.3f}$'),
                  fml(f'${p2.l_pp[0]*10**3:.3f}$'), fml(f'{p2.l1[0]*10**3:.3f}'), fml(f'{p2.l0[0]*10**3:.3f}'),
                  fml(f'${cbl.c_t_g_p*10**9:.3f}$'), fml(f'${cbl.c_t_g_pp*10**9:.3f}$'), fml(f'${cbl.c1_g*10**9:.1f}$'),
                  fml(f'${cbl.c0_g*10**9:.3f}$'), fml(f'${cbl.z_c1_g:.3f}$'), fml(f'${cbl.z_c0_g:.3f}$'),
                  fml(f'${cbl.v_c1_g*10**-6:.3f}$'), fml(f'${cbl.v_c0_g*10**-6:.3f}$')],

                 [Paragraph('Трос изолирован', style=s_m), Paragraph(' ', style=s_m),
                  fml(f'${p2.l_p[0]*10**3:.3f}$'), fml(f'${p2.l_pp[0]*10**3:.3f}$'), fml(f'{p2.l1[0]*10**3:.3f}'),
                  fml(f'{p2.l0[0]*10**3:.3f}'), fml(f'${cbl.c_t_p*10**9:.3f}$'), fml(f'${cbl.c_t_pp*10**9:.2f}$'),
                  fml(f'${cbl.c1*10**9:.2f}$'), fml(f'${cbl.c0*10**9:.2f}$'), fml(f'${cbl.z_c1:.1f}$'),
                  fml(f'${cbl.z_c0:.1f}$'), fml(f'${cbl.v_c1*10**-6:.2f}$'), fml(f'${cbl.v_c0*10**-6:.2f}$')],

                 ],
     # ]
     #       colWidths=70, rowHeights=30, spaceBefore=5,
           spaceAfter=5, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)]),

     ]


doc.build(f, onLaterPages=addPageNumber)
