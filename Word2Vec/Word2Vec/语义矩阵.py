# 在获得模型后，计算所得关键词间的余弦距离，并构建各类媒体的关键词语义矩阵。
import numpy as np

# 读取关键词列表
keywords = set()
with open("union.dl", "r", encoding="utf-8") as file:
    for line in file:
        if line.startswith('"'):  # 仅处理以双引号开头的行
            # 提取每行中的关键词并添加到关键词集合中
            line = line.strip().split('"')[1::2]  # 提取引号中的关键词
            keywords.update(line)

# 初始化语义矩阵
semantic_matrix = np.zeros((len(keywords), len(keywords)))

# 加载余弦距离文件
with open("union.dl", "r", encoding="utf-8") as file:
    for line in file:
        if line.startswith('"'):  # 仅处理以双引号开头的行
            # 提取每行中的关键词和余弦距离
            line = line.strip().split()
            keyword1, keyword2 = line[:2]
            cosine_distance = float(line[2])

            # 去除额外的引号
            keyword1 = keyword1.strip('"')
            keyword2 = keyword2.strip('"')

            # 获取关键词索引
            keyword1_index = list(keywords).index(keyword1)
            keyword2_index = list(keywords).index(keyword2)

            # 填充语义矩阵
            semantic_matrix[keyword1_index][keyword2_index] = cosine_distance
            semantic_matrix[keyword2_index][keyword1_index] = cosine_distance

# 保存语义矩阵
np.save("union.npy", semantic_matrix)

# # 读取关键词列表  做输出展示用
# keywords = []
# with open("myself.dl", "r", encoding="utf-8") as file:
#     for line in file:
#         if line.startswith('"'):  # 仅处理以双引号开头的行
#             # 提取每行中的关键词并添加到关键词列表中
#             line = line.strip().split('"')[1::2]  # 提取引号中的关键词
#             keywords.extend(line)

# # 初始化语义矩阵
# semantic_matrix = []

# # 加载余弦距离文件
# with open("myself.dl", "r", encoding="utf-8") as file:
#     for line in file:
#         if line.startswith('"'):  # 仅处理以双引号开头的行
#             # 提取每行中的关键词和余弦距离
#             line = line.strip().split()
#             keyword1, keyword2 = line[:2]
#             cosine_distance = float(line[2])

#             # 去除额外的引号
#             keyword1 = keyword1.strip('"')
#             keyword2 = keyword2.strip('"')

#             # 将关键词及对应的余弦距离添加到语义矩阵中
#             semantic_matrix.append((keyword1, keyword2, cosine_distance))

# # 输出部分语义矩阵内容
# print("部分语义矩阵内容:")
# for entry in semantic_matrix[:15]:  # 输出前10条记录
#     print(entry)
