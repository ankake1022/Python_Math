#連立方程式

from sympy import Symbol, solve

#式を定義する
a = Symbol('a')
b = Symbol('b')

formula1 = a + b - 1
formula2 = 5*a + b - 3

#solve・・・連立方程式を解く
print(solve((formula1, formula2)))

#p149
ex1 = -1*a + b - 2
ex2 = 2*a + b - 4
print(solve((ex1, ex2)))


#ベクトルの方向を求める
import math

#ラジアン・・・円周上でその円の半径と等しい長さの弧=「1[rad]」(単位)を
# 　　　　　　切り取る2本の半径がなす角度

#atan2(y成分, x成分)
#・・・角度をラジアン単位(1[rad])で返す⇒弧度法(コンピュータ内部で使われる数字)
rad = math.atan2(3, 2)

#degrees(値)
#・・・度数法へ変換
th = math.degrees(rad)
print(10*math.cos(math.radians(60)))

print(rad)

#ベクトル演算
# #numpy ・・・ pythonで学術計算をするためのライブラリ
#               計算が高速になったりより楽になったりする
import numpy as np

a = np.array([2, 2])
b = np.array([4, 1])
print(a + b)