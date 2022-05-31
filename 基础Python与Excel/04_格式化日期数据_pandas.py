import pandas as pd

input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与Excel/sales_2013.xls"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与Excel/output_file.xls"
date_frame=pd.read_excel(input_file,sheet_name='january_2013')
writer=pd.ExcelWriter(output_file)
date_frame.to_excel(writer,sheet_name='jan_2013_output',index=False)
writer.save()

# 由于xlwt软件包不再维护，xlwt引擎将在未来版本的pandas中删除。这是pandas中唯一支持xls格式写入的引擎。
# 安装openpyxl并改为写入xlsx文件。您可以设置选项io.excel.xls文件。写入“xlwt”以消除此警告。
# 虽然此选项已弃用，并且还会引发警告，但可以全局设置它并抑制警告。
