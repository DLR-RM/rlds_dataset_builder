import copy

import numpy as np
import os
from scipy.spatial.transform import Rotation

if __name__ == "__main__":
    data_dir = "data/train/"
    # save_dir = "data_filtered/train/"
    file_list = os.listdir(data_dir)

    for f in file_list:
        data = np.load(os.path.join(data_dir, f), allow_pickle=True)  # this is a list of dicts in our case
        l = len(data)
        for i in range(l):
            if i < l - 1:
                step_t = data[i]
                step_t_1 = data[i+1]
                h_msr = Rotation.from_euler('zxy', step_t['state'][3:6])
                # print(step['state'][0:3][np.newaxis].T)
                h_msr = np.hstack((h_msr.as_matrix(), step_t['state'][0:3][np.newaxis].T))
                h_msr = np.vstack((h_msr, np.array([0, 0, 0, 1])))
                # print(h_msr)
                h_des = Rotation.from_euler('zxy', step_t_1['state'][3:6])
                h_des = np.hstack((h_des.as_matrix(), step_t_1['state'][0:3][np.newaxis].T))
                h_des = np.vstack((h_des, np.array([0, 0, 0, 1])))

                # For delta in Robot EEF frame
                delta = np.linalg.inv(h_msr).dot(h_des)
                # For delta in Robot base frame
                # delta = h_des.dot(np.linalg.inv(h_msr))

                delta = np.hstack((Rotation.from_matrix(delta[:3, :3]).as_euler('zxy'), delta[:3, 3]))
            else:
                delta = np.zeros(6)
            step_t['action'] = delta
            data[i] = copy.deepcopy(step_t)
        np.save(data, os.path.join(data_dir, f))

