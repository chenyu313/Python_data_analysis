import pandas as pd

input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file2.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"
data_frame=pd.read_csv(input_file,header=None)
#pandas提供drp函数根据行索引或列索引丢弃行或是列
#pandas函数默认是删除行，列需要加axis=1
data_frame=data_frame.drop([0,1,2,16,17,18])
#print(data_frame)
#根据行索引选取一个单独行作为列索引
data_frame.columns=data_frame.iloc[0]
#print(data_frame.columns)
#使用reindex函数为数据框重新生成索引
data_frame=data_frame.reindex(data_frame.index.drop(3))
data_frame.to_csv(output_file,index=False)