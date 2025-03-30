import pandas as pd

# #读取两个CSV文件
# df1 = pd.read_csv('2022_36.csv')
# df2 = pd.read_csv('2023_33.csv', low_memory=False)  #设置low_memory=False参数。这样做会使Pandas在读取文件时使用更多的内存来准确地推断每列的数据类型，从而避免警告


# #将df2追加到df1的末尾
# combined_df = pd.concat([df1, df2], ignore_index=True)

# #将合并后的数据框保存到新的CSV文件
# combined_df.to_csv('all.csv', index=False)

# 读取CSV文件
df = pd.read_csv('d:/MANDY/毕业论文/数据清洗与整理/all.csv',low_memory=False)

# 筛选出第六列内容为"true"的所有行
true_df = df[df.iloc[:, 5].str.lower() == "true"]  # 使用str.lower()确保大小写不敏感

# 将筛选后的数据保存到新的CSV文件中
true_df.to_csv('d:/MANDY/毕业论文/数据清洗与整理/true.csv', index=False)

# 筛选出第六列内容为"false"的所有行
false_df = df[df.iloc[:, 5].str.lower() == "false"]  # 使用str.lower()确保大小写不敏感

# 将筛选后的数据保存到新的CSV文件中
false_df.to_csv('d:/MANDY/毕业论文/数据清洗与整理/false.csv', index=False)
