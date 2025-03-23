from reportlab.lib.units import cm

def addPageNumber(canvas, doc):
    """
    Add the page number
    """
    page_num = canvas.getPageNumber()
    text = str(page_num - 1)
    # canvas.drawRightString(20*cm, 2*cm, text)
    # canvas.textsize = 12
    # canvas.fonts = 'Times-Roman'
    canvas.drawString(12*cm, 1*cm, text)
    # canvas.Paragraph(text, alignment=TA_CENTER)
