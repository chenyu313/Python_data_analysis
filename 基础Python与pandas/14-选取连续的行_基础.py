import csv
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file2.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"
#这里使用row_counter变量来跟踪行编号
row_counter=0
#打开读写对象
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        #创建读写对象
        filereader=csv.reader(csv_in_file)
        filewriter=csv.writer(csv_out_file)
        #写入的文件的行就是大于3小于15
        for row in filereader:
            if row_counter>=3 and row_counter<=15:
                filewriter.writerow([value.strip() for value in row])
            row_counter+=1
