from openpyxl import load_workbook
from openpyxl.drawing.image import Image
workbook = load_workbook(filename="..//data//dataformula.xlsx")
sheet = workbook.active
logo = Image("..//hcllogo.png")
logo.height=150
logo.width=150
sheet.add_image(logo, "D10")
workbook.save(filename="..//data//hcllogo.xlsx")