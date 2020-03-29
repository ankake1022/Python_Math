#図形の回転
import numpy as np
import matplotlib.pyplot as plt

#四角形ABCDの頂点
p = np.matrix([[3, 3, 5, 5, 3], [3, 1, 1, 3, 3]])

#変換行列(反時計回りに45度回転))
th = np.radians(45)    #度数法　→  弧度法
A = np.matrix([[np.cos(th), np.sin(-th)], [np.sin(th), np.cos(th)]])

#変換
p2 = A * p

#描画
p = np.array(p)
p2 = np.array(p2)
plt.plot(p[0, :], p[1, :])
plt.plot(p2[0, :], p2[1, :])
plt.axis('equal')
plt.grid(color='0.8')
plt.show()