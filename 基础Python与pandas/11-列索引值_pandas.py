import pandas as pd
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"

data_frame=pd.read_csv(input_file)
#这里使用了iloc函数根据索引位置选取列
data_frame_colum_by_index=data_frame.iloc[:,[0,2]]
data_frame_colum_by_index.to_csv(output_file,index=False)
