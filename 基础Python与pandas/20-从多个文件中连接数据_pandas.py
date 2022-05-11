import pandas as pd
import glob,os

input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/csv_data"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/csv_data/output_file.csv"
all_file=glob.glob(os.path.join(input_file,'sales_*'))
all_data_frames=[]
for file in all_file:
    data_fram=pd.read_csv(file,index_col=None)
    all_data_frames.append(data_fram)
data_fram_concat=pd.concat(all_data_frames,axis=0,ignore_index=True)
data_fram_concat.to_csv(output_file,index=False)