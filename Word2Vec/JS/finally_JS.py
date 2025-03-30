# from gensim.models import Word2Vec
# import numpy as np

# # 加载Word2Vec模型
# def load_word2vec_model(model_path):
#     return Word2Vec.load(model_path)

# # 计算两个向量之间的余弦相似度
# def cosine_similarity(vector1, vector2):
#     return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))

# # 读取关键词文件，并跳过不存在的关键词
# def read_keywords(file_path, model):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return {line.strip() for line in file if line.strip() in model.wv.key_to_index}

# # 构建议程矩阵，只包含存在于模型中的关键词
# def construct_agenda_matrix(model, keywords):
#     word_vectors = [model.wv[word] for word in keywords if word in model.wv.key_to_index]
#     return np.array(word_vectors)

# # 计算两个议程矩阵之间的Jensen-Shannon距离
# def jensen_shannon_distance(matrix1, matrix2):
#     # 计算两个矩阵的交集和并集的索引
#     intersection_indices = np.intersect1d(np.where(matrix1 != 0)[0], np.where(matrix2 != 0)[0])
#     union_indices = np.union1d(np.where(matrix1 != 0)[0], np.where(matrix2 != 0)[0])
    
#     # 过滤掉超出范围的索引
#     valid_indices = np.arange(matrix1.shape[0])
#     union_indices = np.intersect1d(union_indices, valid_indices)
    
#     # 计算交集部分的相似度
#     intersection_similarity = 0.0
#     if intersection_indices.size > 0:
#         intersection_vectors1 = matrix1[intersection_indices]
#         intersection_vectors2 = matrix2[intersection_indices]
#         intersection_similarity = np.mean([cosine_similarity(v1, v2) for v1, v2 in zip(intersection_vectors1, intersection_vectors2)])
    
#     # 计算并集部分的相似度
#     unique_vectors1 = np.unique(matrix1[union_indices], axis=0, return_index=True)[1]
#     unique_vectors2 = np.unique(matrix2[union_indices], axis=0, return_index=True)[1]
#     # 创建一个映射，将索引映射到对应的唯一向量
#     unique_map1 = {index: vector for index, vector in zip(unique_vectors1, matrix1[union_indices][unique_vectors1])}
#     unique_map2 = {index: vector for index, vector in zip(unique_vectors2, matrix2[union_indices][unique_vectors2])}
    
#     # 计算每个唯一向量之间的平均相似度
#     unique_similarity = 0.0
#     for index1 in unique_map1:
#         for index2 in unique_map2:
#             unique_similarity += cosine_similarity(unique_map1[index1], unique_map2[index2])
#     unique_similarity /= (len(unique_map1) * len(unique_map2))
    
#     # 计算最终的JS距离
#     jsd = (intersection_similarity + unique_similarity) / 2
#     return 1 - jsd

# # 计算两个议程之间的相似度
# def calculate_agenda_similarity(agenda1, agenda2):
#     return jensen_shannon_distance(agenda1, agenda2)

# # 主函数
# def main():
#     # 加载Word2Vec模型
#     model_path = 'word2vec_model_all.bin'
#     model = load_word2vec_model(model_path)
    
#     # 读取关键词文件
#     tf_union_path = 'tf_union.txt'
#     tf_myself_path = 'tf_myself.txt'
#     tf_false_path = 'tf_false.txt'
    
#     # 读取关键词，并跳过不存在的关键词
#     tf_union = read_keywords(tf_union_path, model)
#     tf_myself = read_keywords(tf_myself_path, model)
#     tf_false = read_keywords(tf_false_path, model)
    
#     # 构建议程矩阵
#     agenda_matrix_union = construct_agenda_matrix(model, tf_union)
#     agenda_matrix_myself = construct_agenda_matrix(model, tf_myself)
#     agenda_matrix_false = construct_agenda_matrix(model, tf_false)
    
#     # 计算相似度
#     similarity_union_myself = calculate_agenda_similarity(agenda_matrix_union, agenda_matrix_myself)
#     similarity_union_false = calculate_agenda_similarity(agenda_matrix_union, agenda_matrix_false)
#     similarity_myself_false = calculate_agenda_similarity(agenda_matrix_myself, agenda_matrix_false)
    
#     print(f"Similarity between tf_union and tf_myself: {similarity_union_myself}")
#     print(f"Similarity between tf_union and tf_false: {similarity_union_false}")
#     print(f"Similarity between tf_myself and tf_false: {similarity_myself_false}")

# if __name__ == "__main__":
#     main()

from gensim.models import Word2Vec
import numpy as np

# 加载Word2Vec模型
def load_word2vec_model(model_path):
    return Word2Vec.load(model_path)

# 计算两个向量之间的余弦相似度
def cosine_similarity(vector1, vector2):
    return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))

# 读取关键词文件，并跳过不存在的关键词
def read_keywords(file_path, model):
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.strip() for line in file if line.strip() in model.wv.key_to_index}

# 构建议程矩阵，只包含存在于模型中的关键词
def construct_agenda_matrix(model, keywords):
    word_vectors = [model.wv[word] for word in keywords if word in model.wv.key_to_index]
    return np.array(word_vectors)

# 计算两个议程矩阵之间的Jensen-Shannon距离
def jensen_shannon_distance(matrix1, matrix2):
    # 计算两个矩阵的交集和并集的索引
    intersection_indices = np.intersect1d(np.where(matrix1 != 0)[0], np.where(matrix2 != 0)[0])
    union_indices = np.union1d(np.where(matrix1 != 0)[0], np.where(matrix2 != 0)[0])
    
    # 过滤掉超出范围的索引
    valid_indices = np.arange(matrix1.shape[0])
    union_indices = np.intersect1d(union_indices, valid_indices)
    
    # 计算交集部分的相似度
    intersection_similarity = 0.0
    if intersection_indices.size > 0:
        intersection_vectors1 = matrix1[intersection_indices]
        intersection_vectors2 = matrix2[intersection_indices]
        intersection_similarity = np.mean([cosine_similarity(v1, v2) for v1, v2 in zip(intersection_vectors1, intersection_vectors2)])
    
    # 计算并集部分的相似度
    unique_vectors1 = np.unique(matrix1[union_indices], axis=0, return_index=True)[1]
    unique_vectors2 = np.unique(matrix2[union_indices], axis=0, return_index=True)[1]
    # 创建一个映射，将索引映射到对应的唯一向量
    unique_map1 = {index: vector for index, vector in zip(unique_vectors1, matrix1[union_indices][unique_vectors1])}
    unique_map2 = {index: vector for index, vector in zip(unique_vectors2, matrix2[union_indices][unique_vectors2])}
    
    # 计算每个唯一向量之间的平均相似度
    unique_similarity = 0.0
    for index1 in unique_map1:
        for index2 in unique_map2:
            unique_similarity += cosine_similarity(unique_map1[index1], unique_map2[index2])
    unique_similarity /= (len(unique_map1) * len(unique_map2))
    
    # 计算最终的JS距离
    jsd = (intersection_similarity + unique_similarity) / 2
    return jsd

# 将Jensen-Shannon距离转换为相似度分数
def jsd_to_similarity(jsd):
    return 1 - jsd

# 计算两个议程之间的相似度
def calculate_agenda_similarity(agenda1, agenda2):
    jsd = jensen_shannon_distance(agenda1, agenda2)
    similarity = jsd_to_similarity(jsd)
    return similarity

# 主函数
def main():
    # 加载Word2Vec模型
    model_path = 'word2vec_model_all.bin'
    model = load_word2vec_model(model_path)
    
    # 读取关键词文件
    tf_union_path = 'tf_union.txt'
    tf_myself_path = 'tf_myself.txt'
    tf_false_path = 'tf_false.txt'
    
    # 读取关键词，并跳过不存在的关键词
    tf_union = read_keywords(tf_union_path, model)
    tf_myself = read_keywords(tf_myself_path, model)
    tf_false = read_keywords(tf_false_path, model)
    
    # 构建议程矩阵
    agenda_matrix_union = construct_agenda_matrix(model, tf_union)
    agenda_matrix_myself = construct_agenda_matrix(model, tf_myself)
    agenda_matrix_false = construct_agenda_matrix(model, tf_false)
    
    # 计算相似度
    similarity_union_myself = calculate_agenda_similarity(agenda_matrix_union, agenda_matrix_myself)
    similarity_union_false = calculate_agenda_similarity(agenda_matrix_union, agenda_matrix_false)
    similarity_myself_false = calculate_agenda_similarity(agenda_matrix_myself, agenda_matrix_false)
    
    print(f"Similarity between tf_union and tf_myself: {similarity_union_myself:.4f}")
    print(f"Similarity between tf_union and tf_false: {similarity_union_false:.4f}")
    print(f"Similarity between tf_myself and tf_false: {similarity_myself_false:.4f}")

if __name__ == "__main__":
    main()