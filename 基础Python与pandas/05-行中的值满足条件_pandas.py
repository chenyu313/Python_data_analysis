import pandas as pd
#获取文件地址
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"
#创建文件读取对象
data_frame=pd.read_csv(input_file)
#对“Cost”列进行处理
data_frame['Cost']=data_frame['Cost'].str.strip('$').astype(float)
#pandas 提供了一个 loc 函数，可以同时选择特定的行与列。你需要在逗号前面设定行筛选
#条件，在逗号后面设定列筛选条件。
data_frame_value_meets_condition=data_frame.loc[(data_frame['Supplier Name'].str.contains('Z')) \
                                                | (data_frame['Cost']<500.0),:]
data_frame_value_meets_condition.to_csv(output_file,index=False)