# 去除停用词
import pandas as pd
import thulac

# 读取原始数据
df = pd.read_csv("2023_24.csv", encoding='utf-8')

# 加载自定义词典
thu = thulac.thulac(seg_only=True, user_dict="dict.txt")

# 定义停用词列表
stop_words = set()
with open('hit_stopwords.txt', 'r', encoding='utf-8') as file:
    for line in file:
        stop_words.add(line.strip())

# 定义函数用于移除停用词
#def remove_stopwords(text):
#    words = thu.cut(text, text=True).split()
#    words = [word for word in words if word not in stop_words]
#    return " ".join(words)

def remove_stopwords(text):
    if isinstance(text, str):  # 检查是否为字符串
        words = thu.cut(text, text=True).split()
        words = [word for word in words if word not in stop_words]
        return " ".join(words)
    else:
        return ""

# 对第三列的文本进行处理
df.iloc[:, 2] = df.iloc[:, 2].apply(remove_stopwords)

# 保存处理后的数据到新的 CSV 文件
df.to_csv("2023_33.csv", index=False, encoding='utf-8')
