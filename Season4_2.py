#直線AB 直線CDのなす角度
import math
import numpy as np

#座標入力
a = np.asarray([2, 7])
b = np.asarray([6, 1])
c = np.asarray([2, 3])
d = np.asarray([6, 5])

#ベクトルa,ベクトルbの成分
va = b - a
vb = d - c

#ベクトルの大きさ
norm_a = np.linalg.norm(va)  #linalg.norm・・・ユークリッド距離を求める
norm_b = np.linalg.norm(vb)

#ベクトルの内積
dot_ab = np.dot(va, vb)  #dot・・・ベクトルの内積計算

#角度を求める
cos = dot_ab / (norm_a * norm_b)
rad = math.acos(cos)     #acos・・・cosの逆関数(表から求めるやつ) ※ただし、弧度法で出力
deg = math.degrees(rad)  #degrees・・・度数法に変換

print(deg)