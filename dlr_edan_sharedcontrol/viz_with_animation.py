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
            #if i<5:
            #    continue 
            #if i>len(data)-5:
            #    continue
            print(f"run {run} -- timestamp {i}")
            print(data[i]["is_terminal"])
            if (data[i]["is_terminal"]):
                print("AAAAAAAAAAAAAAa")
            action = data[i]['action']
            print(action)
            state = data[i]["observation"]["state"]
            x.append(state[0])
            y.append(state[1])
            z.append(state[2])
            g.append(state[6])
            print(action[0], action[1], action[2])
            img.append( data[i]["observation"]["image"])
            #print(f"Terminal : {data[i]['is_terminal']}")
            #print(data[i]['reward'])
            print(f"LI : {data[i]['language_instruction']}")
            #print("normal state",all_data)
            
            #print(f"state : {state}")
            plt.ion() # Interactive mode on

    fig, ax_list = plt.subplots(nrows=2)
    print(y)
    for j in range(len(x)):
        ax_list[0].cla()
        ax_list[0].set_ylim([-1, 1])
        ax_list[0].plot(y[:j], c='red')
        ax_list[0].set_xlim([-0.1, 150])
        ax_list[1].cla()
        ax_list[1].imshow(img[j], cmap='seismic', vmin=-1, vmax=1)

        plt.pause(0.01) # Wait for half second before updating the plot again
        plt.draw()

