import csv
#使用csv模块是为了更方便灵活地处理复杂的CSV文件(脏数据)
#这个模块就是被设计用于正确处理数据值中的嵌入逗号和其他复杂的模式
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"

#打开读写对象
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        #创建读写对象
        filereader=csv.reader(csv_in_file,delimiter=',')
        filewriter=csv.writer(csv_out_file,delimiter=',')
        for row_list in filereader:
            print(row_list)
            #写文件
            filewriter.writerow(row_list)
