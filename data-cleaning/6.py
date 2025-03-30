import csv
import re

#去除emoji表情

# 正则表达式匹配Emoji符号的范围
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

# 打开原始CSV文件和新的CSV文件
with open('2023.csv', 'r', newline='', encoding='utf-8') as input_file, \
     open('2023_22.csv', 'w', newline='', encoding='utf-8') as output_file:
    
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)
    
    # 对每一行数据进行处理
    for row in csv_reader:
        # 获取第三列中的中文文本
        chinese_text = row[2]
        
        # 去除标点符号和emoji符号
        cleaned_text = re.sub(r'[\W！？?.,，。、；;:：【】()（）《》<>《》“”"\'\'『』\[\]]', '', chinese_text)
        cleaned_text = emoji_pattern.sub('', cleaned_text)
        
        # 将处理后的文本内容替换原始数据的第三列
        row[2] = cleaned_text
        
        # 将处理后的行数据写入新的CSV文件
        csv_writer.writerow(row)

print("处理完成，结果已保存至2023_22.csv")
