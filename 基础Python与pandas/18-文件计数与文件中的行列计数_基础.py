import csv,glob,os
#glob模块可以定位匹配于某个特定模式的所有路径名
#os模块包含了用于解析路径名的函数
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/csv_data"
file_counter=0
#os.path.join()函数将函数圆括号中的两部分连接在一起
#glob.glob()函数将'sales_*'中的星号转换成实际的文件名
for input_file in glob.glob(os.path.join(input_file,'sales_*')):
    row_counter=1
    with open(input_file,'r',newline='') as csv_in_file:
        filereader=csv.reader(csv_in_file)
        header=next(filereader,None)
        for row in filereader:
            row_counter+=1
    print('{0!s}: \t{1:d}row \t{2:d}columns'.format(os.path.basename(\
        input_file),row_counter,len(header)))
    file_counter+=1
    print('Number of file:{0:d}'.format(file_counter))