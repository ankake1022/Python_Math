#コサイン類似度
#1に近い値になった2つのベクトルが似ている
import numpy as np

a = np.asarray([2, 0, 1, 0, 1])
b = np.asarray([1, 1, 1, 0, 1])
c = np.asarray([1, 1, 1, 1, 0])

#ユークリッド距離計算
norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)
norm_c = np.linalg.norm(c)

#内積計算
dot_ab = np.dot(a, b)
dot_bc = np.dot(b, c)
dot_ca = np.dot(c, a)

#テスト出力
print(dot_ab / (norm_a * norm_b))
print(dot_bc / (norm_b * norm_c))
print(dot_ca / (norm_c * norm_a))