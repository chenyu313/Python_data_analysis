import sys
#导入 xlrd 模块的 open_workbook 函数来读取和分析Excel文件
from xlrd import open_workbook
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与Excel/sales_2013.xls"
#使用 open_workbook 函数打开一个 Excel 输入文件，并赋给一个名为 workbook的对象
#可以使用这个对象从工作簿中得到单独的工作表
workbook=open_workbook(input_file)
#打印出工作簿中工作表的数量
print('Number of worksheets:',workbook.nsheets)
#循环识别工作表的数量
for worksheet in workbook.sheets():
    print("Worksheet name:",worksheet.name,"\tRows:",\
        worksheet.nrows,"\tColumns:",worksheet.ncols)