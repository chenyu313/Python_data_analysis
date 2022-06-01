from datetime import date
from xlrd import open_workbook,xldate_as_tuple
from xlwt import Workbook

input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与Excel/sales_2013.xls"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与Excel/output_file.xls"
#实例化Excel对象
output_workbook=Workbook()
#添加表格
output_worksheet=output_workbook.add_sheet('jan_2013_output')
#第三列--> Sale Amount 列
sale_amount_column_index=3
#打开输入文件
with open_workbook(input_file) as workbook:
    worksheet=workbook.sheet_by_name('january_2013')
    #将用输入文件中要写入输出文件中的那些行来填充这个列表
    data=[]
    #提取出标题行中的值
    header=worksheet.row_values(0)
    data.append(header)
    for row_index in range(1,worksheet.nrows):
        row_list=[]
        #保存行中的销售额
        sale_amount=worksheet.cell_value(row_index,sale_amount_column_index)
        #条件
        if sale_amount>1400.0:
            for column_index in range(worksheet.ncols):
                cell_value=worksheet.cell_value(row_index,column_index)
                cell_type=worksheet.cell_type(row_index,column_index)
                #判断是否为日期类型
                if cell_type ==3:
                    date_cell = xldate_as_tuple(cell_value,workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        #检验 row_list 是否为空，只将非空的 row_list 添加到 data 中
        if row_list:
            data.append(row_list)
    for list_index,output_list in enumerate(data):
        for element_index,element in enumerate(output_list):
            output_worksheet.write(list_index,element_index,element)
output_workbook.save(output_file)

