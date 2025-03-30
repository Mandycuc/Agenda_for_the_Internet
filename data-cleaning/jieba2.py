import csv
import jieba

# 读取停用词文件
stopwords = set()
with open('dict.txt', 'r', encoding='utf-8') as file:
    for line in file:
        stopwords.add(line.strip())

# 读取CSV文件，对第三列中文文本进行分词处理，并将处理后的数据与其他列重新组合生成新的文件
with open('2022_24.csv', 'r', newline='', encoding='utf-8') as input_file, \
     open('2022_34.csv', 'w', newline='', encoding='utf-8') as output_file:

    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    for row in csv_reader:
        # 假设第三列至第十七列是中文文本数据，使用切片操作取出这些列的数据
        chinese_texts = row[2:17]
        
        # 对每一列中的中文文本进行分词处理，并过滤停用词
        segmented_texts = [' '.join(word for word in jieba.cut(text) if word not in stopwords) for text in chinese_texts]

        # 将处理后的数据与原文件的其他列重新组合
        new_row = row[:2] + segmented_texts + row[17:]  # 假设其他列的索引为0、1、从第三列开始到第十七列、第十七列之后的列

        # 将结果写入新的CSV文件
        csv_writer.writerow(new_row)

print("处理完成，结果已保存至2022_34.csv")
