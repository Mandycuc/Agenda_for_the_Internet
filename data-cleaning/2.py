#去除特殊符号和标点符号
import csv
import string
import os

# 定义函数用于处理数据并生成新的CSV文件
def process_csv(input_file, output_file):
    # 打开输入CSV文件和输出CSV文件
    with open(input_file, 'r', newline='', encoding='utf-8') as csv_input, \
         open(output_file, 'w', newline='', encoding='utf-8') as csv_output:
        
        csv_reader = csv.reader(csv_input)
        csv_writer = csv.writer(csv_output)
        
        # 逐行读取输入CSV文件
        for row in csv_reader:
            # 对第三列数据进行处理（去除特殊符号和标点符号）
            processed_data = row[2].translate(str.maketrans('', '', string.punctuation))
            
            # 将处理过的数据和其他列重新组合
            new_row = [row[0], row[1], processed_data, row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16]]
            
            # 将新的行数据写入输出CSV文件
            csv_writer.writerow(new_row)

# 指定输入CSV文件和输出CSV文件路径
input_csv_path = '2023_22.csv'
output_csv_path = '2023_23.csv'

# 调用函数处理数据并生成新的CSV文件
process_csv(input_csv_path, output_csv_path)

print("处理完成，新文件已保存至:", os.path.abspath(output_csv_path))
