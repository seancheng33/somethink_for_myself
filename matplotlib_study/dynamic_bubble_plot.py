'''
@Author : sean cheng
@Email  : aya234@163.com
@Time   : 18/5/28
动态气泡图
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def tracker(cur_num):
    cur_index = cur_num % num_points

    datapoints['color'][:, 3] = 1.0
    datapoints['size'] += datapoints['growth']

    datapoints['position'][cur_index] = np.random.uniform(0, 1, 2)
    datapoints['size'][cur_index] = 7
    datapoints['color'][cur_index] = (0, 0, 0, 1)
    datapoints['growth'][cur_index] = np.random.uniform(40, 150)

    scatter_plot.set_edgecolors(datapoints['color'])
    scatter_plot.set_sizes(datapoints['size'])
    scatter_plot.set_offsets(datapoints['position'])


if __name__ == '__main__':
    fig = plt.figure(figsize=(9, 7), facecolor=(0, 0.9, 0.9))
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    ax.set_xlim(0, 1)
    ax.set_xticks([])
    ax.set_ylim(0, 1)
    ax.set_yticks([])

    num_points = 20

    datapoints = np.zeros(num_points,
                          dtype=[('position', float, 2), ('size', float, 1), ('growth', float, 1), ('color', float, 4)])
    datapoints['position'] = np.random.uniform(0, 1, (num_points, 2))
    datapoints['growth'] = np.random.uniform(40, 150, num_points)

    scatter_plot = ax.scatter(datapoints['position'][:, 0], datapoints['position'][:, 1],
                              s=datapoints['size'], lw=0.7, edgecolors=datapoints['color'],
                              facecolor='none')

    animation = FuncAnimation(fig, tracker, interval=10)

    plt.show()
