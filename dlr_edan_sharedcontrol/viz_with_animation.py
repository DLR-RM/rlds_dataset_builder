import copy
import time

import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.spatial.transform import Rotation
import cv2

if __name__ == "__main__":
    data_dir = "data/train/"
    backup_dir = "data/train/"
    # backup_dir = "data_bak_bak/train/"
    file_list = os.listdir(backup_dir)
    #f = file_list[number]
    files = ["s3r30.npy"]
    x = [] 
    y = []
    z = [] 
    g = []
    img = []

    for run in files:
        data = np.load(os.path.join(backup_dir, run), allow_pickle=True)  # this is a list of dicts in our case


        for i in range(len(data)):
            action = data[i]['action']
            state = data[i]["observation"]["state"]
            x.append(state[0])
            y.append(state[1])
            z.append(state[2])
            g.append(state[6])
            img.append( data[i]["observation"]["image"])
    plt.ion() # Interactive mode on

    fig, ax_list = plt.subplots(nrows=2)

    for j in range(len(x)):
        ax_list[0].cla()
        ax_list[0].set_ylim([-1, 1])
        ax_list[0].plot(y[:j], c='red')
        ax_list[0].set_xlim([-0.1, 150])
        ax_list[1].cla()
        ax_list[1].imshow(img[j], cmap='seismic', vmin=-1, vmax=1)

        plt.pause(0.01) # Wait for half second before updating the plot again
        plt.draw()

