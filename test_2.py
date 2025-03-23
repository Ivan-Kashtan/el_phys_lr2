from reportlab.platypus import BaseDocTemplate, Paragraph, NextPageTemplate, PageBreak, PageTemplate, Frame
from reportlab.lib.pagesizes import A4, landscape

from styles import s_m

doc = BaseDocTemplate("test2.pdf", pagesize=A4, rightMargin=25, leftMargin=25, topMargin=25, bottomMargin=25)
portrait_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='portrait_frame ')
landscape_frame = Frame(doc.leftMargin, doc.bottomMargin, doc.height, doc.width, id='landscape_frame ')

story= [Paragraph('JKHkh', style=s_m),
        NextPageTemplate('landscape'),
        PageBreak(),
        Paragraph('JKHkh', style=s_m),
        NextPageTemplate('portrait'),
        PageBreak(),
        Paragraph('JKHkh', style=s_m)]

doc.addPageTemplates([PageTemplate(id = 'portrait', frames=portrait_frame),
                      PageTemplate(id = 'landscape', frames=landscape_frame, pagesize=landscape(A4)),
                      ])
doc.build(story)
