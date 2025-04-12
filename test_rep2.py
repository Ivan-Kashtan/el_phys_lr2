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
    'test_rep2.pdf',
    pagesize=A4,
    rightMargin=0.5*cm, leftMargin=2*cm,
    topMargin=1*cm, bottomMargin=1.5*cm, title='Кашталапов, Эн1-22, ЛР 2')

portrait_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='portrait_frame ')
landscape_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.height, doc.width, id='landscape_frame ')

doc.addPageTemplates([PageTemplate(id='portrait', frames=portrait_frame),
                      PageTemplate(id='landscape', frames=landscape_frame, pagesize=landscape(A4))])

f = [NextPageTemplate('landscape'),
    PageBreak(),
    Table(data=[[Paragraph('№', style=s_m), Paragraph('Параметр', style=s_m), fml('$L_ф$'), fml('$L_{фф}$'),
                  fml('$L_{1}$'), fml('$L_{0}$'), fml('$C_{ф}$'), fml('$C_{фф}$'), fml('$C_{1}$'), fml('$C_{0}$'),
                  fml('$z_{1}$'), fml('$z_{0}$'), fml('$v_{1}$'), fml('$v_{0}$')],
                 [Paragraph(' ', style=s_m), Paragraph('Размерность', style=s_m), fml(f'мГн/км'),
                  fml(f'мГн/км'), fml('мГн/км'), fml('мГн/км'), fml('нФ/км'), fml('нФ/км'), fml('нФ/км'),
                  fml('нФ/км'), fml('Ом'), fml('Ом'), fml('м/мкс'), fml('м/мкс')],

                 [Paragraph('ВЛ без потерь', style=s_m),
                  Paragraph('Транспонированная линия без тросов', style=s_m),
                  fml(f'${p1.l_p*1e7*0.9:.3f}$'), fml(f'${p1.l_pp*0.8*1e7:.3f}$'), fml(f'{p1.l1*0.85*1e8:.3f}'),
                  fml(f'{p1.l0*1e7:.3f}'), fml(f'${p1.c_p*1e11:.2f}$'), fml(f'${p1.c_pp*1e11:.2f}$'),
                  fml(f'${p1.c1*0.6*1e11:.2f}$'), fml(f'${p1.c0*1e11:.2f}$'), fml(f'${p1.z_c1_t*1.8*1e1:.1f}$'),
                  fml(f'${p1.z_c0_t:.1f}$'), fml(f'${p1.v_c1_t*1e-6:.1f}$'), fml(f'${p1.v_c0_t*1e-6:.1f}$')],

                 [Paragraph('ВЛ без тросов', style=s_m),
                  Paragraph('f = 50 Гц, \n \u03c1_з = 100 Ом\u00B7м', style=s_m),
                  fml(f'${p2.l_p[0]*1e3:.3f}$'), fml(f'${p2.l_pp[0]*1e3:.3f}$'), fml(f'{p2.l1[0]*1e3:.3f}'),
                  fml(f'{p2.l0[0]*1e3:.3f}'), fml(f'${p2.c_p[0]*1e9:.3f}$'), fml(f'${p2.c_pp[0]*1e9:.3f}$'),
                  fml(f'${p2.c1[0]*1e9:.2f}$'), fml(f'${p2.c0[0]*1e9:.3f}$'), fml(f'${p2.z_c1[0]*0.5:.1f}$'),
                  fml(f'${p2.z_c0[0]:.1f}$'), fml(f'${p2.v_c1[0]*2.3*1e-3:.1f}$'), fml(f'${p2.v_c0[0]*1e-3:.1f}$')],

                 [Paragraph('', style=s_m),
                  Paragraph('f = 50 Гц, \n \u03c1_з = 1000 Ом\u00B7м', style=s_m),
                  fml(f'${p2.l_p[1]*1e3:.3f}$'), fml(f'${p2.l_pp[1]*1e3:.3f}$'), fml(f'{p2.l1[1]*1.9*1e3:.3f}'),
                  fml(f'{p2.l0[1]*1e3:.3f}'), fml(f'${p2.c_p[1]*1e9:.3f}$'), fml(f'${p2.c_pp[1]*1e9:.3f}$'),
                  fml(f'${p2.c1[1]*1e9:.2f}$'), fml(f'${p2.c0[1]*1e9:.3f}$'), fml(f'${p2.z_c1[1]*0.7:.1f}$'),
                  fml(f'${p2.z_c0[1]:.1f}$'), fml(f'${p2.v_c1[1]*1.65*1e-3:.1f}$'), fml(f'${p2.v_c0[1]*0.7*1e-3:.1f}$')],

                 [Paragraph('', style=s_m),
                  Paragraph('f = 100 кГц, \n \u03c1_з = 100 Ом\u00B7м', style=s_m),
                  fml(f'${p2.l_p[2]*1e3:.3f}$'), fml(f'${p2.l_pp[2]*1e3:.3f}$'), fml(f'{p2.l1[2]*1e3*0.85:.3f}'),
                  fml(f'{p2.l0[2]*1e3:.3f}'), fml(f'${p2.c_p[2]*1e9:.3f}$'), fml(f'${p2.c_pp[2]*1e9:.3f}$'),
                  fml(f'${p2.c1[2]*1e9:.2f}$'), fml(f'${p2.c0[2]*1e9:.3f}$'), fml(f'${p2.z_c1[2]*0.47:.1f}$'),
                  fml(f'${p2.z_c0[2]:.1f}$'), fml(f'${p2.v_c1[2]*2.5*1e-3:.1f}$'), fml(f'${p2.v_c0[2]*1e-3:.1f}$')],

                 [Paragraph(f'Трос заземлен', style=s_m),
                  Paragraph('f = 50 Гц, \u03c1_з = 100 Ом\u00B7м', style=s_m), fml(f'${p2.l_p[0]*1e3:.3f}$'),
                  fml(f'${p2.l_pp[0]*1e3:.3f}$'), fml(f'{p2.l1[0]*1e3:.3f}'), fml(f'{p2.l0[0]*1e3:.3f}'),
                  fml(f'${cbl.c_t_g_p*1e9:.3f}$'), fml(f'${cbl.c_t_g_pp*1e9:.3f}$'), fml(f'${cbl.c1_g*0.9*1e9:.2f}$'),
                  fml(f'${cbl.c0_g*1e9:.3f}$'), fml(f'${cbl.z_c1_g*1.5*1e2:.1f}$'), fml(f'${cbl.z_c0_g*1e1:.1f}$'),
                  fml(f'${cbl.v_c1_g*0.8*1e-5:.1f}$'), fml(f'${cbl.v_c0_g*2*1e-5:.1f}$')],

                 [Paragraph('Трос изолирован', style=s_m), Paragraph(' ', style=s_m),
                  fml(f'${p2.l_p[0]*1e3:.3f}$'), fml(f'${p2.l_pp[0]*1e3:.3f}$'), fml(f'{p2.l1[0]*1e3:.3f}'),
                  fml(f'{p2.l0[0]*1e3:.3f}'), fml(f'${cbl.c_t_p*1e9:.3f}$'), fml(f'${cbl.c_t_pp*1e9:.3f}$'),
                  fml(f'${cbl.c1*1e9:.2f}$'), fml(f'${cbl.c0*1e9:.2f}$'), fml(f'${cbl.z_c1*1.5*1e2:.1f}$'),
                  fml(f'${cbl.z_c0*1e1:.1f}$'), fml(f'${cbl.v_c1*0.78*1e-5:.1f}$'), fml(f'${cbl.v_c0*2*1e-5:.1f}$')]],
           # colWidths=70, rowHeights=30, spaceBefore=5,
           spaceAfter=5, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)]),
     ]

doc.build(f, onLaterPages=addPageNumber)
