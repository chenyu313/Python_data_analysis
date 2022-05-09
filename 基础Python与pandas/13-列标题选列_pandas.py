import pandas as pd

input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"
data_frame=pd.read_csv(input_file)
#loc函数，逗号左边是行，逗号右边是列
data_frame_column_by_name=data_frame.loc[:,['Invoice Number','Purchase Date']]
data_frame_column_by_name.to_csv(output_file,index=False)