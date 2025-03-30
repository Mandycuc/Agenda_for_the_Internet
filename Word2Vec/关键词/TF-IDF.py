# from sklearn.feature_extraction.text import TfidfVectorizer
# import jieba.posseg as pseg

# # 加载分好词的文档
# with open('false.txt', 'r', encoding='utf-8') as f:
#     documents = f.readlines()

# # 筛选指定词性的词语
# filtered_documents = []
# for doc in documents:
#     words = pseg.cut(doc)
#     filtered_words = [word for word, flag in words if flag in ['n', 'nr', 'nt', 'nz', 'l', 'a', 'v', 'vd', 'vn']]
#     filtered_documents.append(' '.join(filtered_words))

# # 创建 TF-IDF 模型
# tfidf = TfidfVectorizer()

# # 计算 TF-IDF 分数
# tfidf_matrix = tfidf.fit_transform(filtered_documents)

# # 获取词汇表
# words = tfidf.get_feature_names_out()

# # 获取 TF-IDF 分数
# tfidf_scores = tfidf_matrix.toarray()[0]

# # 获取前 100 个关键词
# top_indices = tfidf_scores.argsort()[-100:][::-1]
# top_keywords = [words[i] for i in top_indices]

# # 打开新文件，保存关键词
# with open('tf_false.txt', 'w', encoding='utf-8') as f:
#     # 写入关键词
#     for keyword in top_keywords:
#         f.write(f"{keyword}\n")

# #小数据量

# 大数据量
from sklearn.feature_extraction.text import TfidfVectorizer
import jieba.posseg as pseg
import heapq

# 加载分好词的文档
with open('false.txt', 'r', encoding='utf-8') as f:
    documents = f.readlines()

# 筛选指定词性的词语并分块处理
chunk_size = 1000  # 每个分块的文档数量
num_chunks = len(documents) // chunk_size + 1  # 计算分块的数量
top_keywords = []  # 存储所有分块的关键词

# 创建 TF-IDF 模型
tfidf = TfidfVectorizer()

# 分块处理
for i in range(num_chunks):
    start_idx = i * chunk_size
    end_idx = min((i + 1) * chunk_size, len(documents))
    chunk_documents = documents[start_idx:end_idx]

    # 筛选指定词性的词语
    filtered_documents = []
    for doc in chunk_documents:
        words = pseg.cut(doc)
        filtered_words = [word for word, flag in words if flag in ['n', 'nr', 'nt', 'nz', 'l', 'a', 'v', 'vd', 'vn']]
        filtered_documents.append(' '.join(filtered_words))

    # 计算 TF-IDF 分数
    tfidf_matrix = tfidf.fit_transform(filtered_documents)

    # 获取词汇表
    words = tfidf.get_feature_names_out()

    # 获取 TF-IDF 分数
    tfidf_scores = tfidf_matrix.toarray()

    # 获取每个分块的前 100 个关键词并添加到总关键词列表中
    for tfidf_score in tfidf_scores:
        top_indices = heapq.nlargest(100, range(len(tfidf_score)), tfidf_score.__getitem__)
        top_keywords.extend([words[i] for i in top_indices])

# 获取整体的前 100 个关键词
top_keywords = heapq.nlargest(100, set(top_keywords), top_keywords.count)

# 保存关键词
with open('tf_false.txt', 'w', encoding='utf-8') as f:
    # 写入关键词
    for keyword in top_keywords:
        f.write(f"{keyword}\n")

