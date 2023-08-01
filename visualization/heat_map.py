# import numpy as np
# import matplotlib.pyplot as plt
#
# # Have colormaps separated into categories:
# # http://matplotlib.org/examples/color/colormaps_reference.html
#
# cmaps = [('Perceptually Uniform Sequential',
#           ['viridis', 'inferno', 'plasma', 'magma']),
#          ('Sequential', ['Blues', 'BuGn', 'BuPu',
#                          'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
#                          'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
#                          'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
#          ('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool',
#                              'copper', 'gist_heat', 'gray', 'hot',
#                              'pink', 'spring', 'summer', 'winter']),
#          ('Diverging', ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
#                         'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
#                         'seismic']),
#          ('Qualitative', ['Accent', 'Dark2', 'Paired', 'Pastel1',
#                           'Pastel2', 'Set1', 'Set2', 'Set3']),
#          ('Miscellaneous', ['gist_earth', 'terrain', 'ocean', 'gist_stern',
#                             'brg', 'CMRmap', 'cubehelix',
#                             'gnuplot', 'gnuplot2', 'gist_ncar',
#                             'nipy_spectral', 'jet', 'rainbow',
#                             'gist_rainbow', 'hsv', 'flag', 'prism'])]
#
# nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps)
# gradient = np.linspace(0, 1, 256)
# gradient = np.vstack((gradient, gradient))
#
#
# def plot_color_gradients(cmap_category, cmap_list):
#     fig, axes = plt.subplots(nrows=nrows)
#     fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
#     axes[0].set_title(cmap_category + ' colormaps', fontsize=14)
#
#     for ax, name in zip(axes, cmap_list):
#         ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
#         pos = list(ax.get_position().bounds)
#         x_text = pos[0] - 0.01
#         y_text = pos[1] + pos[3] / 2.
#         fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)
#
#     # Turn off *all* ticks & spines, not just the ones with colormaps.
#     for ax in axes:
#         ax.set_axis_off()
#
#
# for cmap_category, cmap_list in cmaps:
#     plot_color_gradients(cmap_category, cmap_list)
#
# plt.show()

# from matplotlib import cm
# import matplotlib.pyplot as plt
# import numpy as np
# import cv2
#
#
# # 将所绘制图映射到热力图
# def gray2color(gray_array, color_map):
#     '''
#
#     :param gray_array: 必须为二维numpy_narray矩阵
#     :param color_map: 保存的cmp彩色映射图
#     :return: 返回映射后的热力图(heat_map)
#     '''
#     rows, cols = gray_array.shape
#     color_array = np.zeros((rows, cols, 3), np.uint8)
#
#     for i in range(0, rows):
#         for j in range(0, cols):
#             color_array[i, j] = color_map[gray_array[i, j]]
#
#     # color_image = Image.fromarray(color_array)
#
#     return color_array
#
#
# # the path of jet_map
# jet_map = np.loadtxt('E:\\0_writePapers\\相关代码\\各算法输出结果\\jet_int.txt', dtype=np.int)
#
# # numpy narray
# picture = cv2.imread('E:\\0_writePapers\\TADT-python-master(new_1)\\out_feature_map\\score_map_vision\\image.jpg')  # cv2.imread读入的图片已经是numpy narray形式
# gray_picture = cv2.cvtColor(picture, cv2.COLOR_RGB2GRAY)  # 转换成灰度图
# print(gray_picture.shape)
# # get the heat_map
# gray_to_color = gray2color(gray_picture, jet_map)
#
# # draw picture
# plt.figure()
# plt.subplot(121)
# plt.imshow(gray_picture, cmap='gray')
#
# plt.subplot(122)
# plt.imshow(gray_to_color)
# plt.show()


import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch

delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
print(x)
X, Y = np.meshgrid(x, y)
print(X)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

fig, ax = plt.subplots()
im = ax.imshow(Z, interpolation='bilinear', cmap=cm.RdYlGn,
               origin='lower', extent=[-3, 3, -3, 3],
               vmax=abs(Z).max(), vmin=-abs(Z).max())

plt.show()
