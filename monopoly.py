import random as rando
import numpy as np
import matplotlib.pyplot as plt

from matplotlib._png import read_png
from matplotlib.cbook import get_sample_data


def main():
    # create list of 1000 rolls
    rolls = list()
    for _ in range(39):
        rolls.append(rando.randint(1, 6) + rando.randint(1, 6))

    print(rolls)

    # populate a dict with the locations
    boardFile = open('board.txt', 'r')
    board = dict()
    for i, line in enumerate(boardFile.readlines()):
        board[i] = line.strip()

    # for roll in rolls we want to tally the position
    # position is 0 for go to 39 for boardwalk
    position = 0
    tallys = dict()
    for roll in rolls:
        position = np.mod(position + roll, 40)
        if position in tallys.keys():
            tallys[position] += 1
        else:
            tallys[position] = 1
        # print(f'roll: {roll} new position: {position}')
        #         # print(tallys)

    # plot the results
    fig = plt.figure()
    # ax = plt.axes(projection="3d")
    ax = fig.add_subplot(111, projection='3d')

    num_bars = 40  # 36
    x_pos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    y_pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    z_pos = [0] * num_bars
    x_size = [0.5] * num_bars
    y_size = [0.5] * num_bars
    z_size = [0] * num_bars
    for x in range(num_bars):
        if x in tallys.keys():
            z_size[x] = tallys[x]
    # for key in sorted(tallys.keys()):
    #     z_size.append(tallys[key])

    # ax.set_xlabel('X axis')
    # ax.set_ylabel('Y axis')
    # ax.set_zlabel('Z axis')

    # Image Stuff
    fn = get_sample_data("/Users/tylerkorte/PycharmProjects/Monopoly/classic-monopoly.png", asfileobj=True)
    arr = read_png(fn)
    # End Image Stuff

    # 3D labels
    # for prop, x, y, z in zip(board.values(), x_pos, y_pos, z_pos):
    #     label = prop  # '(%d, %d, %d)' % (x, y, z)
    #     ax.text(x, y, z, label)

    x0 = -1.5  # -2.1
    xf = 12  # 12.35
    dx = (xf - x0)/550
    x = np.arange(x0, xf, dx)
    y = np.arange(x0, xf, dx)
    xx, yy = np.meshgrid(x, y)
    ax.set_zlim(0, 10)
    ax.view_init(60, 30)

    ax.plot_surface(xx, yy, np.atleast_2d(0), rstride=1, cstride=1, facecolors=arr)
    ax.bar3d(x_pos, y_pos, z_pos, x_size, y_size, z_size, color='aqua')

    plt.show()

    # print(tallys.keys())
    # print(tallys.values())


if __name__ == '__main__':
    main()
