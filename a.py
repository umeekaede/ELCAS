# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

''' define function '''
def st_line(x1, x2, x):
    y=(30/(x2-x1))*(x-x1)-15
    return y

def main():
    ''' read data file part'''
    xu_list=[]
    xd_list=[]

    f=open('value.dat', 'rt')
    for line in f:
        data=line[:-1].split(',')
        xu_list.append(float(data[0]))
        xd_list.append(float(data[1]))

    xu_list=np.array(xu_list)
    xd_list=np.array(xd_list)
    plt.ion

    # グラフ描画位置の設定
    fig=plt.figure(figsize=(8.0, 6.0))
    ax=fig.add_subplot(111)
    #plt.subplots_adjust(left=0.1, bottom=0.15)

    # グラフ描画
    plt.grid()
    x = np.arange(-15, 15)
    graph, = plt.plot(x, st_line(xd_list[0], xu_list[0], x))

#    def threshold_update(slider_val):
#        y = st_line(xd_list[2], xu_list[2], x)
#        # xとyの値を更新
#        graph.set_xdata(x)
#        graph.set_ydata(y)
#        # グラフの再描画
#        fig.canvas.draw_idle()
#
#    # スライダーの表示位置
#    slider_pos = plt.axes([0.1, 0.01, 0.8, 0.03])
#
#    # Sliderオブジェクトのインスタンス作成
#    threshold_slider = Slider(slider_pos, 'd', 0, 5, valinit=0)
#
#    # スライダーの値が変更された場合の処理を呼び出し
#    threshold_slider.on_changed(threshold_update)
#
#    # グラフ表示
#    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
