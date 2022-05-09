import pandas as pd

input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"
#购买日期集合
important_dates=['1/20/14','1/30/14']
#读取文件对象
data_frame=pd.read_csv(input_file)
#pandas 提供了一个 loc 函数，可以同时选择特定的行与列。你需要在逗号前面设定行筛选
#条件，在逗号后面设定列筛选条件。
data_frame_value_in_set=data_frame.loc[data_frame['Purchase Date'].\
    isin(important_dates),:]  #isin命令
data_frame_value_in_set.to_csv(output_file,index=False)
