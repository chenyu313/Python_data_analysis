import csv

input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"

#打开文件对象
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        #创建读写对象
        filereader = csv.reader(csv_in_file, delimiter=',')
        filewriter = csv.writer(csv_out_file, delimiter=',')
        #next函数读出输入文件的第一行
        header=next(filereader)
        #将标题行写入输出文件
        filewriter.writerow(header)
        for row_list in filereader:
            #取出每行供应商的名字(即第一列),并且删除两端空格
            supplier=str(row_list[0]).strip()
            #取出第4列属性，并删除美元符号，删除逗号
            cost=str(row_list[3]).strip('$').replace(',','')
            #若满足以下条件则写入
            if supplier == 'Supplier Z' or float(cost)>600.0:
                filewriter.writerow(row_list)