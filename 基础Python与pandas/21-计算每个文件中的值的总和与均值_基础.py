import csv,glob,os
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/csv_data"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/csv_data/output_file.csv"
#创建了一个输出文件的列标题列表
output_header_list=['file_name','total_sales','average_sales']
#打开文件对象
csv_out_file=open(output_file,'a',newline='')
#创建写对象
filewriter=csv.writer(csv_out_file)
#将标题行写入输出文件
filewriter.writerow(output_header_list)
#循环读取文件
for input_file in glob.glob(os.path.join(input_file,'sales_*')):
    #打开文件对象
    with open(input_file,'r',newline='') as csv_in_file:
        filereader=csv.reader(csv_in_file)
        output_list=[]
        #将输入文件的文件名追加到output_list中
        output_list.append(os.path.basename(input_file))
        #除去标题行
        header=next(filereader)
        total_sales=0.0
        number_of_sales=0.0
        for row in filereader:
            #列表索引取出销售列中的值
            sale_amount=row[3]
            #将sale_amount标准化
            total_sales+=float(str(sale_amount).strip('$').replace(',',''))
            number_of_sales+=1
        #利用format函数格式化保留小数点后两位数
        average_sales='{0:.2f}'.format(total_sales/number_of_sales)
        output_list.append(total_sales)
        output_list.append(average_sales)
        filewriter.writerow(output_list)
csv_out_file.close()