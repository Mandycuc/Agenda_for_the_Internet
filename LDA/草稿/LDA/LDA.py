from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from scipy import sparse

# 读取分词处理后的文本数据
def read_tokenized_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.readlines()
    return text

# 假设分词处理后的文本存储在名为tokenized_data.txt的文本文件中
file_path = 'union.txt'
tokenized_text = read_tokenized_text_file(file_path)

# 创建TF-IDF向量化器
tfidf_vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split())

# 向量化文本数据
tfidf_matrix = tfidf_vectorizer.fit_transform(tokenized_text)

# 将稀疏矩阵保存到文件
sparse.save_npz("tf_union.npz", tfidf_matrix)

# 加载TF-IDF特征向量数据
tfidf_features_sparse = sparse.load_npz("tf_union.npz")

# 设置LDA模型参数
num_topics = 5
lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)

# 拟合LDA模型
lda.fit(tfidf_features_sparse)

# 获取主题-单词分布矩阵
topic_word_distributions = lda.components_

# 获取单词列表
words = tfidf_vectorizer.get_feature_names_out()

# 打印每个主题的前n个单词
for i, topic in enumerate(topic_word_distributions):
    top_words_indices = topic.argsort()[:-5-1:-1]  # 取前5个单词
    top_words = [words[idx] for idx in top_words_indices]
    print(f"Topic {i+1}: {' '.join(top_words)}")
