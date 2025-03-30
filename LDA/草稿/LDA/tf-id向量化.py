from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import sparse

# 读取分词处理后的文本数据
def read_tokenized_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.readlines()
    return text

# 假设分词处理后的文本存储在名为tokenized_data.txt的文本文件中
file_path = 'false.txt'
tokenized_text = read_tokenized_text_file(file_path)

# 创建TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split())

# 向量化文本数据
tfidf_matrix = tfidf_vectorizer.fit_transform(tokenized_text)

# 将稀疏矩阵保存到文件
sparse.save_npz("tfidf_false.npz", tfidf_matrix)


