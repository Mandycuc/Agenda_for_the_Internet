import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# 加载文本数据
def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    return data

# 使用LDA模型对文本数据进行主题建模
def lda_modeling(data, num_topics=5):
    # 使用词袋模型进行向量化
    vectorizer = CountVectorizer(max_df=0.8, min_df=2, max_features=1000, stop_words='english')
    X = vectorizer.fit_transform(data)

    # 使用LDA模型进行拟合
    lda_model = LatentDirichletAllocation(n_components=num_topics, learning_method='online', random_state=42)
    lda_output = lda_model.fit_transform(X)

    return lda_model, lda_output, vectorizer.get_feature_names_out()

# 构建不同主题语料的共现矩阵
def build_co_occurrence_matrix(lda_output):
    co_occurrence_matrix = np.zeros((lda_output.shape[1], lda_output.shape[1]))

    for document_topics in lda_output:
        for i in range(len(document_topics)):
            for j in range(len(document_topics)):
                if i != j:
                    co_occurrence_matrix[i][j] += document_topics[i] * document_topics[j]

    return co_occurrence_matrix

# 保存共现矩阵为Pajek格式
def save_pajek_format(co_occurrence_matrix, feature_names, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('*Vertices {}\n'.format(len(feature_names)))
        for i, word in enumerate(feature_names):
            file.write('{} "{}"\n'.format(i + 1, word))
        file.write('*Edges\n')
        for i in range(co_occurrence_matrix.shape[0]):
            for j in range(co_occurrence_matrix.shape[1]):
                if co_occurrence_matrix[i][j] > 0:
                    file.write('{} {} {}\n'.format(i + 1, j + 1, co_occurrence_matrix[i][j]))

# 主函数
def main():
    # 加载并预处理文本数据
    data = load_data('union.txt')

    # 使用LDA模型进行主题建模
    lda_model, lda_output, feature_names = lda_modeling(data)

    # 构建不同主题语料的共现矩阵
    co_occurrence_matrix = build_co_occurrence_matrix(lda_output)

    # 保存共现矩阵为Pajek格式
    save_pajek_format(co_occurrence_matrix, feature_names, 'union_network.net')

if __name__ == "__main__":
    main()

