import gensim
from gensim import corpora
from gensim.models import LdaModel
from gensim.models import CoherenceModel
import jieba

# 从txt文件中读取文本数据
def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text_data = [line.strip() for line in file]
    return text_data

# 读取txt文件中的文本数据
file_path = 'false.txt'  # 替换为你的txt文件路径
text_data = read_txt_file(file_path)

# 对文本数据进行分词处理
text_data_tokenized = [jieba.lcut(text) for text in text_data]

# 创建词典（Dictionary），将词语映射到整数id
dictionary = corpora.Dictionary(text_data_tokenized)

# 使用词典将文本数据转换为词袋表示
corpus = [dictionary.doc2bow(text) for text in text_data_tokenized]

# 设置LDA模型参数
num_topics = 5  # 主题数量
passes = 12  # 迭代次数

# 训练LDA模型
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=passes)

# 打印每个主题中排名靠前的词语
for topic_id in range(num_topics):
    print(f"主题 {topic_id}:")
    for word, prob in lda_model.show_topic(topic_id):
        print(f"{word} (概率：{prob:.4f})")
    print()

