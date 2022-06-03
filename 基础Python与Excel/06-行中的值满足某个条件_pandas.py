import pandas as pd

input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与Excel/sales_2013.xls"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与Excel/output_file.xls"
#读取输入文件
data_frame=pd.read_excel(input_file,'january_2013',index_col=None)
#筛选出条件
data_frame_value_meets_condition=data_frame[data_frame['Sale Amount'].astype(float)<1400.0]
writer=pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer,sheet_name='jan_13_output',index=False)
writer.save()