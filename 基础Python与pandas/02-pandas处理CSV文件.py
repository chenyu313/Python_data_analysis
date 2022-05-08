import pandas as pd
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"
data_frame=pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file,index=False)