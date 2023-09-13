import copy
import os

import numpy as np
from scipy.spatial.transform import Rotation

if __name__ == "__main__":
    data_dir = "data_filtered/train/"
    save_dir = "data_filtered_filtered/train/"
    file_list = os.listdir(data_dir)

    number_of_episodes = 0
    offset = 4
    for file_n in range(len(file_list)):
        if file_n < len(file_list) - 1:
            f = file_list[file_n]
            f_next = file_list[file_n+1]
            data = np.load(os.path.join(data_dir, f), allow_pickle=True)  # this is a list of dicts in our case
            data_next = np.load(os.path.join(data_dir, f_next), allow_pickle=True)  # this is a list of dicts in our case
            n_steps = len(data)
            number_of_episodes += 1
            print(f"Episode: {f}")
            for i in range(n_steps):
                if i < n_steps - offset:
                    data[i]["image"] = data[i + offset]["image"]
                else:
                    data[i]["image"] = data_next[offset - (n_steps - i)]["image"]
                    # print(f"Step number : {i} Is Terminal {data[i]['is_terminal']}")
        else:
            f = file_list[file_n]
            data = np.load(os.path.join(data_dir, f), allow_pickle=True)  # this is a list of dicts in our case
            n_steps = len(data)
            number_of_episodes += 1
            print(f"Episode: {f}")
            for i in range(n_steps):
                if i < n_steps - offset:
                    data[i]["image"] = data[i + offset]["image"]
                else:
                    data = np.delete(data, data.shape[0] - 1)
        np.save(os.path.join(save_dir, f), data)
