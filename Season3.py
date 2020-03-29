#グラフの描画 ×

import numpy as np
import matplotlib.pyplot as plt

#描画範囲の指定
# x = np.arange(x軸の最小値, x軸の最大値, 刻み)
x = np.arange(-12, 12, 0.1)

#計算式
y = np.sin(x)

#横軸の変数  縦軸の変数
plt.plot(x, y)
plt.show()
