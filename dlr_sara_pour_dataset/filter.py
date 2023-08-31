import copy
import os

import numpy as np
from scipy.spatial.transform import Rotation

if __name__ == "__main__":
    data_dir = "data_bak_bak/train/"
    save_dir = "data_filtered/train/"
    file_list = os.listdir(data_dir)

    number_of_episodes = 0

    for f in file_list:
        data = np.load(os.path.join(data_dir, f), allow_pickle=True)  # this is a list of dicts in our case
        n_steps = len(data)
        number_of_episodes += 1
        print(f"Episode: {f}")
        for i in range(n_steps):
            step_t = data[i]
            if i < n_steps - 1:
                step_t_1 = data[i + 1]
                h_msr = Rotation.from_euler("zxy", step_t["state"][3:6])
                # print(step['state'][0:3][np.newaxis].T)
                h_msr = np.hstack((h_msr.as_matrix(), step_t["state"][0:3][np.newaxis].T))
                h_msr = np.vstack((h_msr, np.array([0, 0, 0, 1])))
                # print(f"step_t[state]: {step_t['state']}")

                h_des = Rotation.from_euler("zxy", step_t_1["state"][3:6])
                h_des = np.hstack((h_des.as_matrix(), step_t_1["state"][0:3][np.newaxis].T))
                h_des = np.vstack((h_des, np.array([0, 0, 0, 1])))
                # print(f"step_t_1[state]: {step_t_1['state']}")
                # For delta in Robot EEF frame

                delta = np.linalg.inv(h_msr).dot(h_des)
                # For delta in Robot base frame
                # delta = h_des.dot(np.linalg.inv(h_msr))
                delta = np.hstack((delta[:3, 3], Rotation.from_matrix(delta[:3, :3]).as_euler("zxy")))
                # print(f"step_t[action]: {delta}")

            else:
                delta = np.zeros(6)
            step_t["action"] = delta.astype(np.float32)
            data[i] = copy.deepcopy(step_t)
            # print(i, len(data))
        np.save(os.path.join(save_dir, f), data)
        # if number_of_episodes > 20:
        #     break
