from xlrd import open_workbook
from xlwt import Workbook
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与Excel/sales_2013.xls"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与Excel/output_file.xls"
#实例化一个 xlwt Workbook 对象，以使我们可以将结果写入用于输出的 Excel文件
output_workbook=Workbook()
#使用 xlwt 的 add_sheet 函数为输出工作簿添加一个工作表 jan_2013_output
output_worksheet=output_workbook.add_sheet('jan_2013_output')
#使用 xlrd 的 open_workbook 函数打开用于输入的工作簿，并将结果赋给一个workbook 对象
with open_workbook(input_file) as workbook:
    #使用这个 workbook 对象的 sheet_by_name 函数引用名称为january_2013 的工作表
    worksheet=workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            #使用 xlwt 的 write 函数和行与列的索引将每个单元格的值写入输出文件的工作表
            output_worksheet.write(row_index,column_index,\
                                   worksheet.cell_value(row_index,column_index))
output_workbook.save(output_file)