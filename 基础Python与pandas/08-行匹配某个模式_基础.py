import re
import csv
#导入正则表达式模块(re)
input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"

#使用re模块的comile函数创建一个名为pattern正则表达式变量
#(1)r表示将单引号之间的模式当做原始符号字符串来处理
#(2)P<my_pattern_group>捕获了名为<my_pattern_group>的组中匹配的子字符串
#(3)搜索的实际模式是^001-.*
#(4)插入^符号表示只在字符串开头搜索模式，所以这里字符串以001-开头
#(5).*组合一起用来表示除换行符以外的任意字符可以在001-后面出现任意多次
#(6)re.I告诉正则表达式进行大小写敏感的匹配
pattern=re.compile(r'(?P<my_pattern_group>^001-.*)',re.I)
#打开读写对象
with open(input_file,'r',newline='') as csv_in_file:
    with open(output_file,'w',newline='') as csv_out_file:
        #创建读写对象
        filereader=csv.reader(csv_in_file)
        filewriter=csv.writer(csv_out_file)
        #读写第一行属性
        header=next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            invoice_number=row_list[1]
            if pattern.search(invoice_number):
                filewriter.writerow(row_list)
