import pandas as pd
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"
#标题行
header_list=['Supplier Name','Invoice Number',\
                     'Part Number','Cost','Purchase Date']
#read_csv函数可以直接指定输入文件不包含标题行，并可以提供一个列标题列表
data_frame=pd.read_csv(input_file,header=None,names=header_list)
data_frame.to_csv(output_file,index=False)