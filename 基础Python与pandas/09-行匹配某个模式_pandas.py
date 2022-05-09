import pandas as pd
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"
#用变量装读取的文件
data_frame=pd.read_csv(input_file)
#loc函数，逗号前是行，逗号后是列
#使用startwith函数来搜索数据，不用笨重的正则表达式
data_frame_value_matchs_pattern=data_frame.loc[data_frame['Invoice Number'].\
                                               str.startswith("001-"),:]
data_frame_value_matchs_pattern.to_csv(output_file,index=False)