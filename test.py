
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.cbook import get_sample_data
# from matplotlib._png import read_png
# import numpy as np
#
# fn = get_sample_data("/Users/tylerkorte/PycharmProjects/Monopoly/monopoly-board.png", asfileobj=True)
# img = read_png(fn)
#
# x, y = np.mgrid[0:img.shape[0], 0:img.shape[1]]
#
# ax = plt.gca(projection='3d')
# ax.plot_surface(x, y, np.sin(0.02*x)*np.sin(0.02*y), rstride=2, cstride=2,
#                 facecolors=img)
# plt.show()

# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator, FormatStrFormatter
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib._png import read_png
# from matplotlib.cbook import get_sample_data
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X = np.arange(-5, 5, .25)
# Y = np.arange(-5, 5, .25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.winter,
#                        linewidth=0, antialiased=True)
#
# ax.set_zlim(-2.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
# fn = get_sample_data("/Users/tylerkorte/PycharmProjects/Monopoly/monopoly-board.png", asfileobj=True)
# arr = read_png(fn)
# # 10 is equal length of x and y axises of your surface
# stepX, stepY = 10. / arr.shape[0], 10. / arr.shape[1]
#
# X1 = np.arange(-5, 5, stepX)
# Y1 = np.arange(-5, 5, stepY)
# X1, Y1 = np.meshgrid(X1, Y1)
# # stride args allows to determine image quality
# # stride = 1 work slow
# ax.plot_surface(X1, Y1, -2.01, rstride=1, cstride=1, facecolors=arr)
#
# plt.show()


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib._png import read_png
from matplotlib.cbook import get_sample_data

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, .25)
Y = np.arange(-5, 5, .25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.winter,
                       linewidth=0, antialiased=True)

ax.set_zlim(-2.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fn = get_sample_data("/Users/tylerkorte/PycharmProjects/Monopoly/monopoly-board.png", asfileobj=True)
arr = read_png(fn)
# 10 is equal length of x and y axises of your surface
stepX, stepY = 10. / arr.shape[0], 10. / arr.shape[1]

X1 = np.arange(-5, 5, stepX)
Y1 = np.arange(-5, 5, stepY)
X1, Y1 = np.meshgrid(X1, Y1)
# stride args allows to determine image quality
# stride = 1 work slow
ax.plot_surface(X1, Y1, np.atleast_2d(-2.0), rstride=1, cstride=1, facecolors=arr)

plt.show()