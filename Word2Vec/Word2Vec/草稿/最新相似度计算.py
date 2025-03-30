import numpy as np
from scipy.spatial.distance import cosine, jensenshannon
from gensim.models import Word2Vec
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: 提取关键词
def extract_keywords(text_file, stopwords_file, num_keywords):
    with open(stopwords_file, 'r', encoding='utf-8') as file:
        stopwords = file.read().splitlines()

    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    words = [word for word in jieba.cut(text) if word not in stopwords]

    tfidf_vectorizer = TfidfVectorizer(max_features=num_keywords)
    tfidf_matrix = tfidf_vectorizer.fit_transform([' '.join(words)])
    feature_names = tfidf_vectorizer.get_feature_names_out()
    top_keywords = [feature_names[idx] for idx in np.argsort(tfidf_matrix.toarray()[0])[-num_keywords:]]

    return top_keywords

# Step 2: 构建关键词向量
def build_keyword_vectors(top_keywords, word2vec_model_file):
    model = Word2Vec.load(word2vec_model_file)
    keyword_vectors = {}
    for word in top_keywords:
        if word in model.wv:
            keyword_vectors[word] = model.wv[word]
    return keyword_vectors

# Step 3: 构建议程矩阵
def build_agenda_matrix(top_keywords, keyword_vectors, max_length):
    model = Word2Vec.load(word2vec_model_file)
    agenda_matrix = np.zeros((max_length, model.vector_size))
    for i, keyword in enumerate(top_keywords):
        if keyword in keyword_vectors:
            agenda_matrix[i] = keyword_vectors[keyword]
    return agenda_matrix

# Step 4: 计算关键词之间的相似度
def calculate_keyword_similarity(top_keywords, keyword_vectors):
    keyword_similarities = {}
    for keyword1 in top_keywords:
        for keyword2 in top_keywords:
            if keyword1 != keyword2 and keyword1 in keyword_vectors and keyword2 in keyword_vectors:
                similarity = 1 - cosine(keyword_vectors[keyword1], keyword_vectors[keyword2])
                keyword_similarities[(keyword1, keyword2)] = similarity

    if keyword_similarities:
        average_similarity = sum(keyword_similarities.values()) / len(keyword_similarities)
    else:
        average_similarity = 0.0
    return average_similarity

# Step 5: 计算议程相似度
def evaluate_agenda_similarity(agenda_matrix_1, agenda_matrix_2):
    if agenda_matrix_1.shape != agenda_matrix_2.shape:
        return float('-inf')
    else:
        similarity = jensenshannon(np.ravel(agenda_matrix_1), np.ravel(agenda_matrix_2))
        return 1 - similarity

if __name__ == "__main__":
    stopwords_file = 'stopwords.txt'
    word2vec_model_file = 'word2vec_model_all.bin'
    num_keywords = 10

    text_files = ['tf_false.txt', 'tf_union.txt', 'tf_myself.txt']

    top_keywords = {}
    keyword_vectors = {}
    max_length = 0

    for text_file in text_files:
        keywords = extract_keywords(text_file, stopwords_file, num_keywords)
        top_keywords[text_file] = keywords
        keyword_vectors[text_file] = build_keyword_vectors(keywords, word2vec_model_file)
        max_length = max(max_length, len(keywords))

    agenda_matrices = {}
    for text_file, keywords in top_keywords.items():
        agenda_matrices[text_file] = build_agenda_matrix(keywords, keyword_vectors[text_file], max_length)

    for text_file, keywords in top_keywords.items():
        avg_keyword_similarity = calculate_keyword_similarity(keywords, keyword_vectors[text_file])
        print(f"关键词之间的平均相似度({text_file}):", avg_keyword_similarity)

    for i in range(len(text_files)):
        for j in range(i + 1, len(text_files)):
            text_file1 = text_files[i]
            text_file2 = text_files[j]
            agenda_matrix_1 = agenda_matrices[text_file1]
            agenda_matrix_2 = agenda_matrices[text_file2]
            agenda_similarity = evaluate_agenda_similarity(agenda_matrix_1, agenda_matrix_2)
            print(f"议程相似度({text_file1}, {text_file2}):", agenda_similarity)






