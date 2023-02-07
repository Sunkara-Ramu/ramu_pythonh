from openpyxl import Workbook
from openpyxl.chart import LineChart,Reference
wb=Workbook()
sheet=wb.active
sales_data=[["Year","Sales"],[500,500],[2000,1000],[3000,1500],[4000,3000],[5000,2500],[6000,3000]]
for i in sales_data:
    sheet.append(i)
line=LineChart()
data=Reference(worksheet=sheet,min_row=1,max_row=5,min_col=1,max_col=2)
line.add_data(data,titles_from_data=True)
sheet.add_chart(line,"E2")
wb.save("..//data//Line_chart.xlsx")