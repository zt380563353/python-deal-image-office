# coding=utf-8

import matplotlib.pyplot as plt  # 导入模块
import numpy as np

#生成数据柱状图
def write_histogram_jpg(data: dict, fileAllPath):
    # 1）创建画布(容器层)
    plt.figure("不同源ip的日志个数", figsize=(12, 9))  # 10为绘图对象长度，5为宽度
    #plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    # 设置x轴的信息
    new_x = np.linspace(0, 11, 12)
    plt.xticks(new_x)

    # 设置y轴取值范围, data的values的最大值为y轴最大值
    plt.ylim(0, max(data.values()))

    """将x轴对应的参数显示为ip"""
    plt.xticks(range(0, len(data)),
               data.keys(),
               )

    # 调整字体角度
    plt.xticks(rotation=45)

    # 包含每个柱子下标的序列
    index = np.arange(len(data))
    #x轴为ip，y轴该ip对应的值
    plt.bar(index, data.values(), 0.5, color=["red", "g", "b"], align="center")

    #给柱状图加数据标注
    for x, y in enumerate(data.values()):
        plt.text(x - 0.1, y + 1, "%s" % y)

    # 3）显示图像
    #plt.show()

    plt.savefig(fileAllPath)

    #关闭图片
    plt.close()

#生成饼图
#data ： {key1: num, key2: num}
def write_pieChart_jpg(data: dict, fileAllPath):

    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            # 同时显示数值和占比的饼图
            return '{v:d} ({p:.2f}% )'.format(p=pct, v=val)

        return my_autopct

    #创建饼图
    plt.pie(data.values(), explode=None, labels=data.keys(), autopct=make_autopct(data.values()), shadow=False, startangle=150)

    #显示图像
    #plt.show()

    #保存图像
    plt.savefig(fileAllPath)

    #关闭图片
    plt.close()