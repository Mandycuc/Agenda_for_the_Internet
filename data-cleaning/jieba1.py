import csv
import jieba

# 打开CSV文件
with open('2022_24.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # 逐行读取CSV文件
    for row in csvreader:
        # 取出每行的第四列数据进行分词
        text = row[2]  # 假设CSV文件中每行的第四列数据需要进行分词处理
        seg_list = jieba.cut(text, cut_all=False)
        
        # 输出分词结果
        print("/ ".join(seg_list))  
