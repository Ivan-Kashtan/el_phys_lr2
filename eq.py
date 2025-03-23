from matplotlib.pyplot import figure, close
from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from reportlab.platypus.flowables import Image

def fml(t_f):
    # for i in range(len(t_f)):
    # img = []
    fig = figure(figsize=(0.01, 0.01))
    # fig.text(0, 0, '${}$'.format(t_f), fontsize=12)
    # font = {'fontname':'Arial'}
    fig.text(0, 0, t_f, fontsize=8)
    imgdata = BytesIO()
    fig.savefig(imgdata, format='svg')
    close(fig)
    imgdata.seek(0)  # rewind the data
    # drawing1=svg2rlg(imgdata)
    # d = Image(svg2rlg(imgdata), hAlign="LEFT")
    # img.append(Image(svg2rlg(imgdata), hAlign="LEFT"))
    return Image(svg2rlg(imgdata), hAlign="LEFT")
