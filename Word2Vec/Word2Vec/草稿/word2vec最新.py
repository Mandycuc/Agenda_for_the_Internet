from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# 指定语料文件路径
corpus_file = "all.txt"  # 你的语料文件路径

# 使用LineSentence加载语料
sentences = LineSentence(corpus_file)

# 初始化Word2Vec模型，设置参数
# 参数说明：sentences为输入的句子列表，vector_size为词向量的维度，window为上下文窗口大小，min_count为最小词频，sg为训练算法选择，workers为并行训练的线程数
model = Word2Vec(sentences, vector_size=100, window=5, min_count=5, sg=0, workers=4)

# 模型训练
model.train(sentences, total_examples=model.corpus_count, epochs=10)

# 保存训练好的模型
model.save("word2vec_model.bin")

# 如果需要加载模型
# model = Word2Vec.load("word2vec_model.bin")

# 获取词向量
vector = model.wv['亚运会']

# 获取与指定词最相似的词
similar_words = model.wv.most_similar('亚运会')

# 打印结果
print(vector)
print(similar_words)

