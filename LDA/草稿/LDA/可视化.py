from collections import defaultdict, Counter
from scipy.sparse import csr_matrix
import numpy as np

# 读取分词后的文本文件并返回分词列表
def read_tokenized_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

# 构建词汇表
def build_vocabulary(tokens):
    words = [word for line in tokens for word in line]
    return list(set(words))

# 构建稀疏共现矩阵
def build_sparse_cooccurrence_matrix(tokens, window_size=2):
    vocab = build_vocabulary(tokens)
    vocab_size = len(vocab)
    cooccurrence_matrix = np.zeros((vocab_size, vocab_size), dtype=int)
    
    # 初始化索引映射
    index_map = {word: i for i, word in enumerate(vocab)}
    
    # 计算共现
    for i, line in enumerate(tokens):
        for j, word in enumerate(line):
            for k in range(i + 1, min(i + window_size, len(tokens))):
                if k in tokens:
                    other_line = tokens[k]
                    for other_word in other_line:
                        if other_word in index_map:
                            cooccurrence_matrix[index_map[word]][index_map[other_word]] += 1
    
    # 转换为稀疏矩阵
    rows = []
    cols = []
    data = []
    for i in range(vocab_size):
        for j in range(vocab_size):
            if cooccurrence_matrix[i][j] > 0:
                rows.append(i)
                cols.append(j)
                data.append(cooccurrence_matrix[i][j])
    
    sparse_matrix = csr_matrix((data, (rows, cols)), shape=(vocab_size, vocab_size))
    return sparse_matrix, index_map, vocab

# 将共现矩阵保存为Ucinet的.net格式
def save_cooccurrence_matrix_to_ucinet_format(matrix, index_map, vocab, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write('*NET\n')
        f.write(str(len(vocab)) + '\n')  # 节点数量
        for word in vocab:
            f.write(word + '\n')
        f.write('0\n')  # 边的数量
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] > 0:
                    f.write(str(index_map[vocab[i]]) + ' ' + str(index_map[vocab[j]]) + ' ' + str(matrix[i][j]) + '\n')

# 主程序
if __name__ == "__main__":
    filename = 'false.txt'  # 假设这是你的清洗分词后的文本文件名
    tokens = read_tokenized_text(filename)
    if not tokens:
        print("文本文件为空或所有分词列表为空，请检查文件内容。")
    else:
        matrix, index_map, vocab = build_sparse_cooccurrence_matrix(tokens)
        save_cooccurrence_matrix_to_ucinet_format(matrix, index_map, vocab, 'false.net')