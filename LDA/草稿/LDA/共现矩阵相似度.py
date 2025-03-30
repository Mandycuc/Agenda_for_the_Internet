import numpy as np  
from collections import defaultdict  
from scipy.sparse import csr_matrix  
from sklearn.metrics.pairwise import cosine_similarity  
  
# 读取分词后的文本文件并返回分词列表  
def read_tokenized_text(filename):  
    with open(filename, 'r', encoding='utf-8') as f:  
        return f.read().split()  
  
# 构建稀疏共现矩阵  
def build_sparse_cooccurrence_matrix(tokens, window_size=2):  
    vocab = set(tokens)  
    word_to_index = {word: i for i, word in enumerate(vocab)}  
    vocab_size = len(vocab)  
      
    # 初始化共现计数  
    cooccurrences = defaultdict(int)  
      
    # 计算共现  
    for i in range(len(tokens) - window_size + 1):  
        for j in range(i + 1, min(i + window_size, len(tokens))):  
            word1, word2 = tokens[i], tokens[j]  
            if word1 in word_to_index and word2 in word_to_index:  
                cooccurrences[(word_to_index[word1], word_to_index[word2])] += 1  
      
    # 创建稀疏矩阵的行、列和数据  
    rows, cols, data = zip(*cooccurrences.keys(), *cooccurrences.values())  
      
    # 创建稀疏矩阵  
    matrix = csr_matrix((data, (rows, cols)), shape=(vocab_size, vocab_size))  
    return matrix, word_to_index  
  
# 计算两个稀疏矩阵之间的余弦相似度  
def calculate_sparse_similarity(matrix1, matrix2):  
    return cosine_similarity(matrix1, matrix2)  
  
# 主程序  
if __name__ == "__main__":  
    filenames = ['false.txt', 'union.txt', 'myself.txt']  # 假设这是你的分词后文本文件名列表  
    cooccurrence_matrices = []  
    word_to_index_maps = []  
      
    # 为每个文件构建共现矩阵  
    for filename in filenames:  
        tokens = read_tokenized_text(filename)  
        matrix, word_to_index = build_sparse_cooccurrence_matrix(tokens)  
        cooccurrence_matrices.append(matrix)  
        word_to_index_maps.append(word_to_index)  
      
    # 比较并打印共现矩阵之间的相似度  
    for i in range(len(cooccurrence_matrices)):  
        for j in range(i + 1, len(cooccurrence_matrices)):  
            similarity = calculate_sparse_similarity(cooccurrence_matrices[i], cooccurrence_matrices[j])  
            print(f"Similarity between {filenames[i]} and {filenames[j]}: {similarity[0][0]}")