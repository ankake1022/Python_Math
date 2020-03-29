#図形の線対称移動
import numpy as np
import matplotlib.pyplot as plt

#三角形を描画する場合・・・
#matplotlibで A⇒B⇒C⇒A の順に頂点を結んで行って描画していく
#そのため移動前の座標は「2*4の行列」
#(1 3 3 1) ← x座標
#(1 1 2 1) ← y座標
# ↑ ↑ ↑ ↑
#(A B C A)
#これを踏まえてコードを書いていく

#三角形ABCの頂点
p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1]])

#変換行列(X軸に線対称)
q = np.matrix([[1, 0], [0, -1]])

#変換
p2 = q*p
print(p2)

#描画処理
p = np.array(p)  #行列を二次元配列に変換
p2 = np.array(p2)#行列を二次元配列に変換

plt.plot(p[0, :], p[1, :]) #「:」で指定した行の値すべて
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()

#y軸対称やy = x線対称などは変換行列の値が変わるだけなので省略