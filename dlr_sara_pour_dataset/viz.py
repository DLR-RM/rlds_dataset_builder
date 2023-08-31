import os
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
        print(f"Episode: {f}, Is terminal : ", data[n_steps - 1]["is_terminal"])
        if data[n_steps - 1]["is_terminal"]:
            number_of_successes += 1

        for step in range(n_steps):
            cv2.imshow("image", data[step]["image"])
            cv2.waitKey(1)

        #     # print(f"Terminal : {data[i]['is_terminal']}, Success: {data[i]['is_success']}, Reward : {data[i]['reward']}")

        # time.sleep(5)
        # if number_of_episodes > 2:
        #     break
    print(f"Number of successes : {number_of_successes}")
