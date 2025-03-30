from gensim import corpora, models
import networkx as nx

# 1. 加载预处理文本
def load_preprocessed_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        preprocessed_text_data = [line.strip().split() for line in file]
    return preprocessed_text_data

# 2. 使用LDA模型
def train_lda(preprocessed_text_data, num_topics=5):
    # 创建词袋模型
    dictionary = corpora.Dictionary(preprocessed_text_data)
    corpus = [dictionary.doc2bow(text) for text in preprocessed_text_data]
    
    # 使用LDA模型拟合数据
    lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
    
    # 打印每个主题的关键词
    for topic_id, topic_words in lda_model.print_topics():
        print(f"Topic {topic_id}: {topic_words}")
    
    return lda_model

# 3. 构建议程网络
def build_agenda_network(lda_model):
    # 创建一个空的有向图
    G = nx.DiGraph()

    # 添加节点（主题和关键词）
    for topic_id, topic_words in lda_model.print_topics():
        topic_node = f"Topic {topic_id}"
        G.add_node(topic_node)
        words = topic_words.split("+")
        for word in words:
            word_node = word.strip()
            G.add_node(word_node)
            G.add_edge(topic_node, word_node)

    # 保存网络数据为UCINET的DL格式
    nx.write_pajek(G, "myself_network.net")

# 主程序
def main():
    # 加载预处理文本数据
    preprocessed_text_data = load_preprocessed_text("myself.txt")

    # 训练LDA模型
    lda_model = train_lda(preprocessed_text_data)

    # 构建议程网络并保存为UCINET的DL格式文件
    build_agenda_network(lda_model)

if __name__ == "__main__":
    main()
