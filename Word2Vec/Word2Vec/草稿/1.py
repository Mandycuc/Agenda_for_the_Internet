from gensim.models import Word2Vec
import numpy as np

# 步骤1: 读取关键词列表
# 功能: 从TXT文档中读取每行存储的关键词，创建一个关键词列表
keywords = []
with open("tf_true.txt", "r", encoding="utf-8") as f:
    keywords = [line.strip() for line in f.readlines()]

# 步骤2: 使用Word2Vec模型计算相似度矩阵
# 功能: 加载预训练的Word2Vec模型，计算关键词列表中每对关键词之间的相似度，
#       并将这些相似度存储在一个矩阵中。
model = Word2Vec.load("D:\MANDY\毕业论文\模型\word2vec_model_all.bin")
similarity_matrix = np.zeros((len(keywords), len(keywords)))
for i, word1 in enumerate(keywords):
    for j, word2 in enumerate(keywords):
        if i != j:
            try:
                similarity_matrix[i][j] = model.wv.similarity(word1, word2)
            except KeyError:  # 如果关键词不在模型词汇表中，则相似度为0
                similarity_matrix[i][j] = 0

# 步骤3: 筛选相似度大于等于0.6的关系
# 功能: 遍历相似度矩阵，将相似度小于0.6的值设置为0，以便只保留相似度较高的关系。
similarity_matrix[similarity_matrix < 0.6] = 0

# 步骤4: 导出为UCINET可识别的DL格式
# 功能: 将筛选后的相似度矩阵导出为DL格式文件，这样文件可以被UCINET软件读取，
#       用于进一步的网络分析和可视化。
def export_matrix_to_dl(matrix, keywords, file_path):
    with open(file_path, 'w') as f:
        f.write(f'dl n={len(keywords)}\n')
        f.write('format = edgelist1\n')
        f.write('labels embedded:\n')
        f.write('data:\n')
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != 0:  # 仅导出相似度大于0的关系
                    f.write(f"{keywords[i]} {keywords[j]} {matrix[i][j]}\n")

file_path = 'D:\MANDY\毕业论文\模型\similarity_matrix.dl'
export_matrix_to_dl(similarity_matrix, keywords, file_path)
