#去除emoji表情利用emoji库
import csv
import emoji
import re

# 打开原始CSV文件和新的CSV文件
with open('2023_23.csv', 'r', newline='', encoding='utf-8') as input_file, \
     open('2023_24.csv', 'w', newline='', encoding='utf-8') as output_file:
    
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)
    
    # 对每一行数据进行处理
    for row in csv_reader:
        # 获取第三列中的中文文本
        chinese_text = row[2]
        
        # 将文本中的 Emoji 表情转换为对应的字符串表示，并去除其中的特殊字符
        cleaned_text = re.sub(r'[\d！？?.,，。、；;:：|【】()（）《》<>《》“”"\'\'『』\[\]]', '', emoji.demojize(chinese_text))
        
        # 将处理后的文本内容替换原始数据的第三列
        row[2] = cleaned_text
        
        # 将处理后的行数据写入新的CSV文件
        csv_writer.writerow(row)

print("处理完成，结果已保存至output.csv")


