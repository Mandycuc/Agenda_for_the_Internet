import csv
import thulac

thulac_obj = thulac.thulac(seg_only=True, user_dict="dict.txt")


# 创建THULAC对象
#thulac_obj = thulac.thulac(seg_only=True)

# 打开原始CSV文件和新的CSV文件
with open('2023_22.csv', 'r', newline='', encoding='utf-8') as input_file, \
     open('2023_32.csv', 'w', newline='', encoding='utf-8') as output_file:
    
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)
    
    for row in csv_reader:
        text = row[2]  # 假设第三列是中文文本数据
        segmented_text = thulac_obj.cut(text, text=True)  # 分词处理
        
        # 将清洗后的数据与原文件第三列文本进行替换
        row[2] = segmented_text
        
        # 将处理后的行数据写入新的CSV文件
        csv_writer.writerow(row)

print("分词处理完成，结果已保存至2022_33.csv")
