import pandas as pd
#去除重复值和缺失值

df = pd.read_csv('2023_21.csv')

#查看有多少行数据
#print(df.shape) 

#直接查看有多少行重复的数据
#print(df.duplicated().sum())

#查看重复的数据，指的是两行数据完全相同，如果只有部分数据相同，则不是重复
#print(df.duplicated())

#查看重复的数据行
print(df[df.duplicated()]) 

#不会对数据文件进行直接修改，而是生成一个临时表
#print(df.drop_duplicates())  

# 数据去重并生成临时表
temp_df = df.drop_duplicates()

# 将临时表存为新的csv文件，同时不包括索引列
temp_df.to_csv('2023_23.csv',index=False)

#df.to_csv('2023_23.csv') #以csv文件输出#

# 显示每一列中的数据缺失值数量
#print(df.isnull().sum())

# 查看缺失值，没有缺失值标记为false，有缺失值标记为true
# print(df.isnull())

# 查看没有缺失值，没有缺失值标记为true，有缺失值标记为false
# print(df.notnull())

# 显示有缺失值的数据
# 显示'特色'列中有缺失值的数据
# print(df[df.话题内容.isnull()])


