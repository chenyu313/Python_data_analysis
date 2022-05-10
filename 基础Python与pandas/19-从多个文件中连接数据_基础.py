import os,glob,csv
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/csv_data"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/csv_data/output_file.csv"
#第一个文件
first_file=True
#循环读取文件
for input_file in glob.glob(os.path.join(input_file,'sales_*')):
    print(os.path.basename(input_file))
    #打开输入/输出文件
    with open(input_file,'r',newline='') as csv_in_file:
        #‘a’表示后面添加，而不是重写
        with open(output_file,'a',newline='') as csv_out_file:
            filereader=csv.reader(csv_in_file)
            filewriter=csv.writer(csv_out_file)
            #若是第一个文件，则输出标题
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file=False
            else:   #否则跳过标题行
                header=next(filereader,None)
                for row in filereader:
                    filewriter.writerow(row)