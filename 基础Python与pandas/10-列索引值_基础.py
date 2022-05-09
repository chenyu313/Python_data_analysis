import csv
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"
#想要保留的两列索引值
my_columns=[0,3]
#打开读写对象
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        #创建读写对象
        filereader=csv.reader(csv_in_file)
        filewriter=csv.writer(csv_out_file)
        for row_list in filereader:
            #创建变量用于存列
            row_list_output=[]
            for index_value in my_columns:
                #index_value=0或3
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)
