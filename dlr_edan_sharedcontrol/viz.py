import os
import time
from pathlib import Path

import cv2
import numpy as np

if __name__ == "__main__":
    backup_dir = str(Path(__file__).parent / "data/train/")
    # backup_dir = "data_bak_bak/train/"
    file_list = os.listdir(backup_dir)
    number_of_episodes = 0
    number_of_successes = 0
    for i in range(len(file_list)):
        f = file_list[i]
        data = np.load(os.path.join(backup_dir, f), allow_pickle=True)  # this is a list of dicts in our case
        # data_orig = np.load(os.path.join(backup_dir, f), allow_pickle=True)
        n_steps = len(data)
        number_of_episodes += 1
        # print(f"Episode: {f}, Is terminal : ", data[n_steps - 1]["is_terminal"])
        cv2.imshow("image", np.zeros((640, 480)))
        for step in range(n_steps):
            cv2.imshow("image", data[step]["observation"]["image"])
            print("action!", data[step]["action"])
            print(f"Step: {step}, x : {data[step]['observation']['state'][1]}, Terminal : {data[step]['is_terminal']} ")
            # time.sleep(0.5)
            cv2.waitKey(1)
            time.sleep(0.003)
        print(f"ID: {f},  TASK: {data[-1]['language_instruction']}, REWARD {data[-1]['reward']}")
        print(0.2)
        #input()