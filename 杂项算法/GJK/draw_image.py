import matplotlib.pyplot as plt
import numpy as np


# 传入一个多边形
def draw_filled_polygon(points, title="polygon", fill_color='blue', fill_alpha=0.3,
                        show_vertices=True, show_coordinates=True):
    plt.figure(figsize=(10, 8))
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    x_coords.append(points[0][0])
    y_coords.append(points[0][1])

    # 绘制多边形边界
    plt.plot(x_coords, y_coords, 'b-', linewidth=2, label='polygon')

    # 填充多边形
    plt.fill(x_coords, y_coords, alpha=fill_alpha, color=fill_color, label='range')

    # 如果需要，显示顶点
    if show_vertices:
        plt.plot(x_coords[:-1], y_coords[:-1], 'ro', markersize=8, label='points')

    # 如果需要，显示顶点坐标
    if show_coordinates:
        for i, (x, y) in enumerate(points):
            plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points",
                         xytext=(0, 10), ha='center', fontsize=9)

    # 设置图形属性
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 替换为你的字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    plt.title(title, fontsize=14)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axis('equal')  # 保持x和y轴比例相同
    plt.legend()

    # 显示图形
    plt.tight_layout()
    plt.show()


# 示例4: 多个多边形叠加展示
def draw_multiple_polygons(polygons, colors, alphas, title="polygon"):
    """
    绘制多个多边形，展示叠加效果
    """
    plt.figure(figsize=(10, 8))

    for i, (points, color, alpha) in enumerate(zip(polygons, colors, alphas)):
        # 提取坐标
        x_coords = [point[0] for point in points]
        y_coords = [point[1] for point in points]

        # 闭合多边形
        x_coords.append(points[0][0])
        y_coords.append(points[0][1])

        # 绘制边界和填充
        plt.plot(x_coords, y_coords, linewidth=2, label=f'polygon {i + 1}')
        plt.fill(x_coords, y_coords, alpha=alpha, color=color)

    plt.title(title, fontsize=14)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axis('equal')
    plt.legend()
    plt.tight_layout()
    plt.show()

