import csv
import thulac

#使用THULAC工具对文本进行分词处理

# 创建THULAC对象
thulac_obj = thulac.thulac(seg_only=True)

# 读取CSV文件，对第三列中文文本进行分词处理，并将处理结果写入新的CSV文件
with open('2023_2.csv', 'r', newline='', encoding='utf-8') as input_file, \
     open('2023_3.csv', 'w', newline='', encoding='utf-8') as output_file:
    
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)
    
    for row in csv_reader:
        text = row[2]  # 假设第三列是中文文本数据
        segmented_text = thulac_obj.cut(text, text=True)  # 分词处理
        
        # 将处理后的数据与原始数据的其他列重新组合
        new_row = [row[0], row[1], segmented_text, row[3]]  # 假设其他列的索引为0、1、3
        
        # 将结果写入新的CSV文件
        csv_writer.writerow(new_row)

print("分词处理完成，结果已保存至2022_3.csv")
