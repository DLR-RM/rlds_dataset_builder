import copy
import time

import numpy as np
import os
from scipy.spatial.transform import Rotation
import cv2

if __name__ == "__main__":
    data_dir = "data_filtered/train/"
    backup_dir = "../dlr_sara_grid_clamp_dataset/data/train/"
    # backup_dir = "data_bak_bak/train/"
    file_list = os.listdir(backup_dir)
    number_of_episodes = 0
    number_of_successes = 0
    for i in range(len(file_list)):
        f = file_list[i]
        data = np.load(os.path.join(backup_dir, f), allow_pickle=True)  # this is a list of dicts in our case
        # data_orig = np.load(os.path.join(backup_dir, f), allow_pickle=True)
        l = len(data)
        number_of_episodes += 1
        print(f"Episode: {f}, Is terminal : ", data[len(data)-1]["is_terminal"])
        if data[len(data)-1]["is_terminal"]:
            number_of_successes += 1

        for i in range(l):
            cv2.imshow("image", data[i]["image"])
            cv2.waitKey(1)

        #     # print(f"Terminal : {data[i]['is_terminal']}, Success: {data[i]['is_success']}, Reward : {data[i]['reward']}")

        # time.sleep(5)
        # if number_of_episodes > 2:
        #     break
    print(f"NUmber of successes : {number_of_successes}")