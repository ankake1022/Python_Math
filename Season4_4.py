#ベクトルの外積を求める
#cross関数で可
import numpy as np
a = np.asarray([0, 1, 2]) #←aベクトルの成分
b = np.asarray([2, 0, 0]) #←bベクトルの成分
print(np.cross(a, b))

#三角形の面積をもとめる(2つのベクトルの終点を結んでできる三角形)
a = np.asarray([2, 4])
b = np.asarray([3, 1])

#法線ベクトルの計算
cross_ab = np.cross(a, b)
norm_vab = np.linalg.norm(cross_ab)

#三角形の面積 = 法線ベクトル(a, bからなる平行四辺形の面積) / 2)
s = norm_vab / 2
print(s)