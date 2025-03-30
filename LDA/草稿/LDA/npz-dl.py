# import numpy as np
# from scipy.sparse import csr_matrix

# # 替换为你的文件路径
# file_path = 'tf_union.npz'

# # 加载稀疏矩阵
# with np.load(file_path, allow_pickle=True) as data:
#     indices = data['indices']
#     indptr = data['indptr']
#     data = data['data']
#     sparse_matrix = csr_matrix((data, indices, indptr))

# # 转换稀疏矩阵为密集矩阵并获取边列表
# dense_matrix = sparse_matrix.toarray()
# edge_list = [(i, j, dense_matrix[i, j]) for i in range(dense_matrix.shape[0]) for j in range(dense_matrix.shape[1]) if dense_matrix[i, j] > 0]

# # 保存为Ucinet支持的.dl格式文件
# output_file = 'LDA_union.dl'
# with open(output_file, 'w') as f:
#     for edge in edge_list:
#         # Ucinet期望的格式是：源节点 目标节点 权重
#         f.write(f"{edge[0]} {edge[1]} {edge[2]}\n")

# print(f"Network data has been saved to {output_file}")

import numpy as np
from scipy.sparse import csr_matrix

# 替换为你的文件路径
file_path = 'tf_union.npz'

# 加载稀疏矩阵
with np.load(file_path, allow_pickle=True) as data:
    indices = data['indices']
    indptr = data['indptr']
    data = data['data']
    sparse_matrix = csr_matrix((data, indices, indptr))

# 转换稀疏矩阵为密集矩阵
dense_matrix = sparse_matrix.toarray()

# 获取边列表，确保节点索引从1开始
edge_list = []
for i in range(dense_matrix.shape[0]):
    for j in range(dense_matrix.shape[1]):
        if dense_matrix[i, j] > 0:
            edge_list.append((i + 1, j + 1, dense_matrix[i, j]))

# 保存为Ucinet支持的.dl格式文件
output_file = 'LDA_union.dl'
with open(output_file, 'w') as f:
    for edge in edge_list:
        # 确保权重是浮点数格式
        f.write(f"{edge[0]} {edge[1]} {edge[2]:.4f}\n")  # 保留四位小数

print(f"Network data has been saved to {output_file}")