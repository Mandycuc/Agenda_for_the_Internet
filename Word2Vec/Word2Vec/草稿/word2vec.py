# from gensim.models import Word2Vec
# from gensim.models.word2vec import LineSentence

# # 加载预处理后的中文语料
# sentences = LineSentence('all.txt')  # 预处理后的语料文件

# # 训练Word2Vec模型
# model = Word2Vec(sentences, vector_size=100, window=5, min_count=5, workers=4)

# # 保存模型（可选）
# model.save("word2vec_model_all.bin")

from gensim.models import Word2Vec

# 加载训练好的 Word2Vec 模型
model = Word2Vec.load('D:\MANDY\毕业论文\模型\word2vec_model_all.bin')

# 读取词语列表
with open('tf_true.txt', 'r', encoding='utf-8') as f:
    keywords = [line.strip() for line in f]

# 假设你有一组参考词语
reference_keywords = ['排球']

# 计算词语与参考词之间的相似度
similarities = []
for keyword in keywords:
    similarity_scores = [(ref_keyword, model.wv.similarity(keyword, ref_keyword)) for ref_keyword in reference_keywords]
    similarities.append((keyword, similarity_scores))

# 选择每个词语的最相似词语
top_similar_words = []
for keyword, similarity_scores in similarities:
    top_similar_word = max(similarity_scores, key=lambda x: x[1])[0]
    top_similar_words.append((keyword, top_similar_word))

# 输出结果
for keyword, top_similar_word in top_similar_words:
    print(f"{keyword}: {top_similar_word}")


