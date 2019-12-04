import matplotlib.pyplot as plt
import numpy as np

# データ生成
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# プロット領域(Figure, Axes)の初期化
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# 棒グラフの作成
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax3.scatter(y1, y2)

# 水平線、垂直線を入れる
ax3.axhline(0.45)
ax3.axvline(0.65)

plt.show()
