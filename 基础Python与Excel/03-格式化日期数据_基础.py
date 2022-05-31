#可以将数值转化为日期并对日期进行格式化
from datetime import date
#第一个函数打开Excel工作薄，第二个函数将日期的数值转化为元组
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与Excel/sales_2013.xls"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与Excel/output_file.xls"
#实例化一个Excel文件对象
output_workbook=Workbook()
#为该对象添加一个表格，名字为‘jan_2013_output’
output_worksheet = output_workbook.add_sheet('jan_2013_output')
#打开输入工作簿
with open_workbook(input_file) as workbook:
    worksheet=workbook.sheet_by_name('january_2013')
    for row_index in range(worksheet.nrows):
        row_list_output=[]
        for col_index in range(worksheet.ncols):
            #单元格类型为 3 表示这个单元格中包含日期数据
            #如果含有日期数据，那么 if 代码块就对单元格进行处理;如果不含有日期数据，那么就使用 else 代码块对单元格进行处理。
            if worksheet.cell_type(row_index,col_index)==3:
                #cell_value 函数和行列索引来引用单元格中的值
                #参数 workbook.datemode 是必需的，它可以使函数确定日期是基于 1900 年还是基于 1904年，并据此将数值转换成正确的元组
                date_cell=xldate_as_tuple(worksheet.cell_value(row_index,col_index),workbook.datemode)
                #使用元组索引来引用元组 date_cell 中的前 3 个元素（也就是年、月、日）并将它们作为参数传给 date 函数
                #strftime 函数将 date 对象转换为一个具有特定格式的字符串
                data_cell=date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list_output.append(date_cell)
                output_worksheet.write(row_index,col_index,data_cell)
            else:
                #行列索引引用单元格中的值，并将其赋给变量 non_date_cell
                non_date_cell=worksheet.cell_value(row_index,col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index, col_index,non_date_cell)
#记得最后要保存在输出文件中
output_workbook.save(output_file)
