#図形の拡大と縮小(変換行列を変えるだけだが見た目の変化が大きいので記しておく)
import numpy as np
import matplotlib.pyplot as plt

p = np.matrix([[1, 1, 2, 1], [3, 1, 1, 3]])
A = int(input("拡大倍率を入力 >>"))
q = np.matrix([[A, 0], [0, A]])

p2 = q * p

#描画
p = np.array(p)
p2 = np.array(p2)
plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()