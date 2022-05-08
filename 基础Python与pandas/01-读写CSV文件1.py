input_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/input_file.csv"
output_file="D:/PycharmProjects/pythonProject/CSV文件/Python-CSV/基础Python与pandas/output_file.csv"

with open(input_file,'r',newline='') as filereader:
    with open(output_file,'w',newline='') as filewriter:
        header=filereader.readline() #读取文件中第一行数据
        header=header.strip() #去除空格和制表符和换行符
        header_list=header.split(',')   #通过逗号拆分成列表
        print(header_list)
        #使用filewriter对象将header_list中的每个值写入输出文件
        #map中的str函数应用于header_list中的每个元素，确保每个元素都是字符串
        filewriter.write(','.join(map(str,header_list))+'\n')
        #循环输出
        for row in filereader:
            row=row.strip() #去除空格
            row_list=row.split(',')
            print(row_list)
            #最后写入输出文件
            filewriter.write(','.join(map(str,row_list))+'\n')
