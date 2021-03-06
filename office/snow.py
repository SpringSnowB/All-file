import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决中文显示为方块的问题


def rotate(p, d):
    """返回点p绕原点逆时针旋转d度的坐标"""

    a = np.radians(d)
    m = np.array([[np.cos(a), np.sin(a)], [-np.sin(a), np.cos(a)]])
    return np.dot(p, m)


def koch_curve(p, q):
    """将线段pq生成科赫曲线，返回uvw三个点"""

    p, q = np.array(p), np.array(q)
    u = p + (q - p) / 3  # 三等分点u的坐标
    v = q - (q - p) / 3  # 三等分点V的坐标
    w = rotate(v - u, 60) + u  # 线段uv绕u点逆时针旋转60°得到点w的坐标

    return u.tolist(), v.tolist(), w.tolist()


def snow(triangle, k):
    """给定三角形，生成封闭的科赫雪花"""

    for i in range(k):
        result = list()
        t_len = len(triangle)
        for j in range(t_len):
            p = triangle[j]
            q = triangle[(j + 1) % t_len]
            u, v, w = koch_curve(p, q)
            result.extend([p, u, w, v])
        triangle = result.copy()

    triangle.append(triangle[0])
    return triangle


def draw_scenery():
    """绘制雪景图"""

    im = Image.open('brage.png')
    bg = np.array(im)
    fig, ax = plt.subplots(frameon=False)
    while 1:
        ax.cla()
        for i in range(80):
            x = np.random.randint(80, im.size[0] - 80)
            y = np.random.randint(30, im.size[1] - 30)
            r = np.random.randint(5, 20)
            a = np.random.random() * 0.6 + 0.2
            v = np.array((x - r / 2, y))
            u = np.array((x + r / 2, y))
            w = rotate(v - u, 60) + u

            data = np.array(
                snow([(u[0], u[1]), (w[0], w[1]), (v[0], v[1])], 5))
            x, y = np.split(data, 2, axis=1)
            plt.plot(x, y, c='#AABBCC', lw=1, ls='-', alpha=a)
        plt.imshow(bg)  # 绘制背景图
        plt.pause(0.01)

    #  plt.axis('equal')
    #  plt.show()


def snow_dats(snn=80):
    dats = []
    for i in range(snn):
        x = np.random.randint(80, im.size[0] - 80)
        y = np.random.randint(30, im.size[1] - 30)
        r = np.random.randint(5, 20)
        a = np.random.random() * 0.6 + 0.2
        v = np.array((x - r / 2, y))
        u = np.array((x + r / 2, y))
        w = rotate(v - u, 60) + u

        data = np.array(snow([(u[0], u[1]), (w[0], w[1]), (v[0], v[1])], 5))
        x, y = np.split(data, 2, axis=1)
        tmp = x, y, a
        dats.append(tmp)
    return dats


def get_snows(nn=24, snn=40):
    """
    调用生成雪花的函数生成，指定的次数

    nn: 雪花场景的次数
    snn: 雪花的次数
    """
    import os
    snow_file = f"snows_{nn}_{snn}.npy"
    if not os.path.exists(snow_file):
        snows = [snow_dats(snn) for x in range(nn)]
        snows = np.array(snows)
        np.save(snow_file, snows)
    else:
        snows = np.load(snow_file, allow_pickle=True)
    return snows


if __name__ == "__main__":
    #  draw_scenery()
    im = Image.open('s.jpg')
    bg = np.array(im)
    fig, ax = plt.subplots(frameon=False)
    snows = get_snows()
    for sss in snows:
        ax.cla()
        for x, y, a in sss:
            ax.plot(x, y, c='#AABBCC', lw=1, ls='-', alpha=a)
        plt.imshow(bg)  # 绘制背景图
        plt.axis("off")
        plt.pause(0.1)
    plt.show()
