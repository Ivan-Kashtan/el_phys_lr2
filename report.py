from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Frame, NextPageTemplate, PageTemplate, PageBreak
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether
from reportlab.lib.units import cm
from reportlab.lib import colors

from numpy import pi

from title_list import *
from styles import *
from eq import *
from page_number import *

import p3
from in_dat import *
import lr_p2

doc = SimpleDocTemplate(
    'report.pdf',
    pagesize=A4,
    rightMargin=1 * cm, leftMargin=1 * cm,
    topMargin=1 * cm, bottomMargin=1.5 * cm, title='Кашталапов, Эн1-22, ЛР 2')

portrait_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='portrait_frame ')
landscape_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.height, doc.width, id='landscape_frame ')

doc.addPageTemplates([PageTemplate(id='portrait', frames=portrait_frame),
                      PageTemplate(id='landscape', frames=landscape_frame, pagesize=landscape(A4)),
                      ])

f = [KeepTogether([mn, t_u, un, s_80, kaf, s_80, tp, title, var, s_130, fac, gr, st, tchr, mk, s_130, sity]),
     Paragraph('Цель работы', style=s_b),
     Paragraph('Расчитать погонные и волновые параметры воздушных линий электропередачи', style=s_m),
     Paragraph('Исходные данные', style=s_b),
# Paragraph('Высота подвеса', style=s_m)
     Table(data=[[fml(f'$U_{{ном.}}$, кВ'), Paragraph('Провод', style=s_m),
                  Paragraph('Диаметр провода, мм', style=s_m), fml('$h_a$, м'), fml('$h_b$, м'),
                  fml('$h_c$, м'), fml('d_{{ab}}'), fml('d_{{bc}}')],
                 [fml(f'${un}$'), Paragraph('АС-300', style=s_m), fml(f'{d}'), fml(f'${h[0]}$, м'),
                  fml(f'${h[1]}$, м'), fml(f'${h[2]}$, м'), fml(f'{x[0]}'), fml(f'{x[1]}')]],
           colWidths=150, rowHeights=20, spaceBefore=5,
           spaceAfter=5, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)]),
     Paragraph('Определение параметров 3-х фазной ВЛ без потерь', style=s_b),
     fml(f'$L = L_a = L_b = L_c = \\dfrac {{{p3.mu0}}}  {{2\\cdot {p3.pi:.2f} }}$'),
     NextPageTemplate('landscape'),
     PageBreak(),
     Table(data=[[Paragraph('№', style=s_m), Paragraph('Параметр', style=s_m), fml('$L_ф$'), fml('$L_{фф}$'),
                  fml('$L_{1}$'), fml('$L_{0}$'), fml('$C_{ф}$'), fml('$C_{фф}$'), fml('$C_{1}$'), fml('$C_{0}$'),
                  fml('$z_{1}$'), fml('$z_{0}$'), fml('$v_{1}$'), fml('$v_{0}$')],
                 [Paragraph(' ', style=s_m), Paragraph('Размерность', style=s_m), fml(f'$мГн/км$'),
                  fml(f'мГн/км'), fml('мГн/км'), fml('мГн/км'), fml('нФ/км'), fml('нФ/км'), fml('нФ/км'),
                  fml('нФ/км'), fml('Ом'), fml('Ом'), fml('м/мкс'), fml('м/мкс')],
                 [Paragraph('ВЛ без потерь', style=s_m),
                  Paragraph('Транспонинрованная линия без тросов', style=s_m),
                  fml(f'${p3.l_p*10**3:.1f}$'), fml(f'${p3.l_pp*10**3:.1f}$'), fml(f'{p3.l1*10**3:.1f}'),
                  fml(f'{p3.l0*10**3:.1f}'), fml(f'${p3.c_p*10**9:.1f}$'), fml(f'${p3.c_pp*10**9:.1f}$'),
                  fml(f'${p3.c1_t*10**9:.1f}$'), fml(f'${p3.c0_t*10**9:.1f}$'), fml(f'${p3.z_c0_t:.1f}$'),
                  fml(f'${p3.z_c1_t:.1f}$'), fml(f'${p3.v_c1_t*10**-6:.1f}$'), fml(f'${p3.v_c0_t*10**-6:.1f}$')],
                 [Paragraph('ВЛ без тросов', style=s_m),
                  Paragraph('f = 50$ Гц, \u03c1_з = 100$ Ом\u00B7м', style=s_m),
                  fml(f'${p3.l_p*10**3:.1f}$'), fml(f'${p3.l_pp*10**3:.1f}$'), fml(f'{p3.l1*10**3:.1f}'),
                  fml(f'{p3.l0*10**3:.1f}'), fml(f'${p3.c_p*10**9:.1f}$'), fml(f'${p3.c_pp*10**9:.1f}$'),
                  fml(f'${p3.c1_t*10**9:.1f}$'), fml(f'${p3.c0_t*10**9:.1f}$'), fml(f'${p3.z_c0_t:.1f}$'),
                  fml(f'${p3.z_c1_t:.1f}$'), fml(f'${p3.v_c1_t*10**-6:.1f}$'), fml(f'${p3.v_c0_t*10**-6:.1f}$')],
                 [Paragraph(f'ВЛ с тросами f = 50 Гц, \u03c1_з = 100 Ом\u00B7м', style=s_m),
                  Paragraph('Трос заземлен', style=s_m), fml(f'${p3.l_p*10**3:.1f}$'), fml(f'${p3.l_pp*10**3:.1f}$'),
                  fml(f'{p3.l1*10**3:.1f}'), fml(f'{p3.l0*10**3:.1f}'), fml(f'${lr_p2.c_t_p*10**9:.1f}$'),
                  fml(f'${lr_p2.c_t_g_pp*10**9:.1f}$'), fml(f'${lr_p2.c1_g*10**9:.1f}$'),
                  fml(f'${lr_p2.c0_g*10**9:.1f}$'), fml(f'${lr_p2.z_c1_g:.1f}$'), fml(f'${lr_p2.z_c0_g:.1f}$'),
                  fml(f'${lr_p2.v_c0_g*10**-6:.1f}$'), fml(f'${lr_p2.v_c1_g*10**-6:.1f}$')],
                 [Paragraph(' ', style=s_m), Paragraph('Трос не заземлен', style=s_m),
                  fml(f'${p3.l_p*10**3:.1f}$'), fml(f'${p3.l_pp*10**3:.1f}$'), fml(f'{p3.l1*10**3:.1f}'),
                  fml(f'{p3.l0*10**3:.1f}'), fml(f'${lr_p2.c1_t*10**9:.1f}$'), fml(f'${lr_p2.c1_t*10**9:.1f}$'),
                  fml(f'${lr_p2.c0_g*10**9:.1f}$'), fml(f'${lr_p2.z_c1*10**9:.1f}$'), fml(f'${lr_p2.z_c0:.1f}$'),
                  fml(f'${lr_p2.z_c1_g:.1f}$'), fml(f'${lr_p2.v_c0*10**-6:.1f}$'), fml(f'${lr_p2.v_c1*10**-6:.1f}$')],

                 # ], )
                 ],
     # ]
     #       colWidths=70, rowHeights=30, spaceBefore=5,
           spaceAfter=5, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)]),

     ]


doc.build(f, onLaterPages=addPageNumber)
