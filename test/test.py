import numpy as np
import matplotlib.pyplot as plt

def st_line(x1, x2, x):
    y=(30/(x2-x1))*(x-x1)-15
    return y

xu_list=[]
xd_list=[]

f=open('value.dat', 'rt')
for line in f:
    data=line[:-1].split(',')
    xu_list.append(float(data[0]))
    xd_list.append(float(data[1]))

print(xu_list)
xu_list=np.array(xu_list)
xd_list=np.array(xd_list)
print(xu_list, xd_list)

plt.ion()

# 6×4サイズのFigureを作成
fig = plt.figure(figsize = (8, 6))

# FigureにAxesを１つ追加
ax = fig.add_subplot(111)


# 0～5を10分割したデータを作成
x = np.linspace(-15, 15, 10)


for i in range(1, 5):
    # 軸ラベルを設定
    ax.set_xlabel("x", fontsize = 14)
    ax.set_ylabel("y", fontsize = 14)
    print(i)
    # 軸範囲を設定
    ax.set_xlim([-18, 18])
    ax.set_ylim([-18, 18])
    ax.axhline(10,  ls = "-.", color = "b")
    ax.axhline(-10, ls = "-.", color = "b")
    ax.plot(x, st_line(xd_list[i], xu_list[i], x), color="red")
    plt.draw()
    plt.pause(0.3)
    if input()=='q':
        break
    elif i==9 and input()=='q':
        plt.close()



# 直線をプロット
#ax.plot(x, st_line(-3, 3, x), color = "red")


plt.show()
plt.close()
