import pandas as pd

# 读取 CSV 文件
data = pd.read_csv('互联网认证新闻单位.csv',low_memory=False)

# 获取第三列数据并将其转换为字符串
text_data = data.iloc[:, 2].astype(str)

# 将数据保存到文本文件
with open('互联网认证新闻单位.txt', 'w', encoding='utf-8') as f:
    for text in text_data:
        f.write(text + '\n')
