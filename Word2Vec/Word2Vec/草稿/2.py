from gensim.models import Word2Vec
import numpy as np

# 读取关键词列表
def read_keywords(file_path):
    """
    从TXT文件中读取关键词列表。
    每行一个关键词。
    """
    with open(file_path, "r", encoding="utf-8") as file:  # 使用utf-8编码读取，避免乱码
        keywords = [line.strip() for line in file.readlines()]
    return keywords

# 计算相似度矩阵
def calculate_similarity_matrix(model, keywords):
    """
    使用Word2Vec模型计算关键词之间的相似度矩阵。
    """
    similarity_matrix = np.zeros((len(keywords), len(keywords)))
    for i, word1 in enumerate(keywords):
        for j, word2 in enumerate(keywords):
            if i != j:
                try:
                    similarity_matrix[i][j] = model.wv.similarity(word1, word2)
                except KeyError:  # 如果关键词不在模型的词汇里，则相似度为0
                    similarity_matrix[i][j] = 0
    return similarity_matrix

# 导出为DL格式
def export_to_dl_format(similarity_matrix, keywords, file_path):
    """
    将相似度矩阵导出为DL格式的文件，用于UCINET。
    只包括相似度大于等于0.6的关系。
    """
    with open(file_path, 'w', encoding='utf-8') as file:  # 使用utf-8编码保存，避免乱码
        file.write(f'dl n={len(keywords)}\n')
        file.write('format = edgelist1\n')
        file.write('labels embedded:\n')
        file.write('data:\n')
        
        for i in range(len(similarity_matrix)):
            for j in range(len(similarity_matrix)):
                if similarity_matrix[i][j] >= 0.6:  # 只导出相似度大于等于0.6的关系
                    file.write(f'"{keywords[i]}" "{keywords[j]}" {similarity_matrix[i][j]}\n')

# 主程序
if __name__ == "__main__":
    # 加载Word2Vec模型
    model = Word2Vec.load("D:\MANDY\毕业论文\模型\word2vec_model_all.bin")
    
    # 读取关键词列表
    keywords = read_keywords("tf_false.txt")
    
    # 计算相似度矩阵
    similarity_matrix = calculate_similarity_matrix(model, keywords)
    
    # 导出为DL格式
    export_to_dl_format(similarity_matrix, keywords, "false.dl")
