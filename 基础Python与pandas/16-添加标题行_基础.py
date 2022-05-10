import csv
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"
#打开读写对象
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        #创建读写对象
        filereader=csv.reader(csv_in_file)
        filewriter=csv.writer(csv_out_file)
        #标题行
        header_list=['Supplier Name','Invoice Number',\
                     'Part Number','Cost','Purchase Date']
        filewriter.writerow(header_list)
        for row in filereader:
            filewriter.writerow(row)