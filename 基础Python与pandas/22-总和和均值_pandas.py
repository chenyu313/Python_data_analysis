import pandas as pd
import glob,os
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/csv_data"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/csv_data/output_file.csv"
all_files=glob.glob(os.path.join(input_file,'sales_*'))
all_data_frames=[]
for input_file in all_files:
    #循环读取文件
    data_frame=pd.read_csv(input_file,index_col=None)
    #使用列表生成式将销售这一列中带美元符号的字符串转成浮点数
    #然后使用数据框函数将这个对象再转为DataFrame
    total_cost=pd.DataFrame([float(str(value).strip('$').replace(',',''))\
                             for value in data_frame.loc[:,'Sale Amount']]).sum()
    average_cost = pd.DataFrame([float(str(value).strip('$').replace(',', '')) \
                               for value in data_frame.loc[:, 'Sale Amount']]).mean()
    data={'file_name':os.path.basename(input_file),
          'total_sales':total_cost,
          'average_sales':average_cost}

    all_data_frames.append(pd.DataFrame(data,\
                                        columns=['file_name','total_sales','average_sales']))
    #使用concat函数将这些数据框连接成为一个数据框，然后将这个数据框写入输入文件
    data_frames_concat=pd.concat(all_data_frames,axis=0,ignore_index=True)
    data_frames_concat.to_csv(output_file,index=False)