from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 假设有三份语料 corpus1.txt, corpus2.txt, corpus3.txt

# 读取文档内容
corpus_files = ['false.txt', 'union.txt', 'myself.txt']
corpora = []

# 创建 TF-IDF 向量化器，并获取相同的词汇表
tfidf_vectorizers = []
tfidf_matrices = []
for file in corpus_files:
    with open(file, 'r', encoding='utf-8') as f:
        corpus = f.read()
        corpora.append(corpus)
        
    # 创建 TF-IDF 向量化器
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_vectorizer.fit([corpus])
    tfidf_vectorizers.append(tfidf_vectorizer)

    # 向量化当前语料
    tfidf_matrix = tfidf_vectorizer.transform([corpus])
    tfidf_matrices.append(tfidf_matrix)

# 创建 LDA 模型
num_topics = 5  # 假设有 5 个主题
ldas = []
for tfidf_matrix in tfidf_matrices:
    lda = LatentDirichletAllocation(n_components=num_topics, random_state=42)
    lda.fit(tfidf_matrix)
    ldas.append(lda)

# 获取主题-文档分布矩阵
topic_document_distributions = [lda.transform(tfidf_matrix) for lda, tfidf_matrix in zip(ldas, tfidf_matrices)]

# 计算所有可能的语料之间的主题-文档分布之间的余弦相似度
similarities = []
for i in range(len(corpus_files)):
    for j in range(i + 1, len(corpus_files)):
        similarity = cosine_similarity(topic_document_distributions[i], topic_document_distributions[j])
        similarities.append((i+1, j+1, similarity))

# 打印相似度
for i, j, similarity in similarities:
    print(f"Similarity between Corpus {i} and Corpus {j}:")
    print(similarity)



