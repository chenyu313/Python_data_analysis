import csv
#你需要检验行中的值是否属于某个集合，然后筛选出具有该集合的值的行
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"
#购买日期集合
important_dates=['1/20/14','1/30/14']
#打开读写对象
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        #创建读写对象
        filereader=csv.reader(csv_in_file,delimiter=',')
        filewriter=csv.writer(csv_out_file,delimiter=',')
        #读写第一行属性
        header=next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            #取出第四列属性
            a_date=row_list[4]
            #判断是否在集合中
            if a_date in important_dates:
                filewriter.writerow(row_list)