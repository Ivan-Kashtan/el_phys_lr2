import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from pandas import DataFrame, ExcelWriter

# Defining a data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['Rajkot', 'Ahmedabad', 'Surat', 'Jamnanagar'],
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Converting DataFrame to list of lists
data_list = [df.columns.values.tolist()] + df.values.tolist()

# Creating a PDF document
pdf_path = r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР2\export_df.pdf'
pdf = SimpleDocTemplate(pdf_path, pagesize=A4)

# Creating a table with the data
table = Table(data_list)

# Adding style to the table
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
])
table.setStyle(style)

# Creating the PDF
elements = [table]
pdf.build(elements)

# with ExcelWriter(r'C:\Users\kasht\Documents\Учёба\Машины\Лабы\6\Машины ЛР 6.xlsx',
#                  mode="a", engine="openpyxl", if_sheet_exists='replace') as writer:
#     p0.to_excel(writer, sheet_name='Двигатель', index=False)
# with ExcelWriter(r'C:\Users\kasht\Documents\Учёба\Машины\Лабы\6\Машины ЛР 6 2.xlsx',
#                  mode="a", engine="openpyxl", if_sheet_exists='replace') as writer:
#     p0.to_excel(writer, sheet_name='p = 0')
#     p15.to_excel(writer, sheet_name='p = 15')
#     p30.to_excel(writer, sheet_name='p = 30')

# p0.to_excel(r'C:\Users\kasht\Documents\Учёба\6 семестр\Электрофизика\ЛР2\test.xlsx', sheet_name="p = 0", index=False)
# p15.to_excel(r'C:\Users\kasht\Documents\Учёба\Машины\Лабы\6\Машины ЛР 6 2.xlsx', sheet_name="p = 15", index=False)
# p30.to_excel(r'C:\Users\kasht\Documents\Учёба\Машины\Лабы\6\Машины ЛР 6 2.xlsx', sheet_name="p = 30", index=False)
