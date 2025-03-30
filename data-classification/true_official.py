import pandas as pd

# 读取 "互联网新闻单位.csv" 文件，获取待匹配的数据
internet_media_df = pd.read_csv('互联网新闻单位.csv', encoding='utf-8', header=None)  # 根据文件实际编码进行设置

# 获取待匹配的数据
internet_media_data = set(internet_media_df[0].tolist())  # 假设待匹配的数据在文件的第一列，索引从0开始

# 读取 "true.csv" 文件
true_df = pd.read_csv('true.csv', encoding='utf-8')  # 根据文件实际编码进行设置

# 筛选出第四列内容与 "互联网新闻单位.csv" 文件中的数据匹配的行
filtered_internet_media_df = true_df[true_df.iloc[:, 3].isin(internet_media_data)]  # 假设第四列的索引为3，索引从0开始

# 将符合条件的数据保存为一个新的 CSV 文件，命名为 "互联网认证新闻单位.csv"
filtered_internet_media_df.to_csv('互联网认证新闻单位.csv', index=False, encoding='utf-8')  # 根据文件实际编码进行设置

print("已将符合条件的行保存为 '互联网认证新闻单位.csv' 文件。")

# 筛选出不属于 "互联网新闻单位.csv" 文件中的数据行
filtered_self_media_df = true_df[~true_df.iloc[:, 3].isin(internet_media_data)]

# 将不属于 "互联网新闻单位.csv" 文件中的数据行保存为一个新的 CSV 文件，命名为 "自媒体.csv"
filtered_self_media_df.to_csv('自媒体.csv', index=False, encoding='utf-8')  # 根据文件实际编码进行设置

print("已将不属于 '互联网新闻单位.csv' 文件的行保存为 '自媒体.csv' 文件。")
