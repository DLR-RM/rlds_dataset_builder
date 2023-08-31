import os

import numpy as np
from scipy.spatial.transform import Rotation

if __name__ == "__main__":
    data_dir = "data_filtered/train/"
    backup_dir = "data/train/"
    file_list = os.listdir(data_dir)
    number_of_episodes = 0
    for f in file_list:
        data = np.load(os.path.join(data_dir, f), allow_pickle=True)  # this is a list of dicts in our case
        data_orig = np.load(os.path.join(backup_dir, f), allow_pickle=True)
        l = len(data)
        number_of_episodes += 1
        print(f"Episode: {f}")
        for i in range(l):
            if i < l - 1:
                step_t = data[i]
                h_msr = Rotation.from_euler("zxy", step_t["state"][3:6])
                h_msr = np.hstack((h_msr.as_matrix(), step_t["state"][0:3][np.newaxis].T))
                h_msr = np.vstack((h_msr, np.array([0, 0, 0, 1])))
                # print(f"step_t[state]: {step_t['state']}")

                delta = Rotation.from_euler("zxy", step_t["action"][3:6])
                delta = np.hstack((delta.as_matrix(), step_t["action"][0:3][np.newaxis].T))
                delta = np.vstack((delta, np.array([0, 0, 0, 1])))

                h_msr_t_1 = h_msr.dot(delta)
                h_msr_t_1 = np.hstack((h_msr_t_1[:3, 3], Rotation.from_matrix(h_msr_t_1[:3, :3]).as_euler("zxy")))
                # print(f"step_t_1_estimated: {h_msr_t_1}")

                step_t_1_orig = data_orig[i + 1]
                # print(f"step_t_1[state]: {step_t_1_orig['state']}")
                if np.linalg.norm(h_msr_t_1 - step_t_1_orig["state"][0:6]) > 5e-16:
                    print(np.linalg.norm(h_msr_t_1 - step_t_1_orig["state"][0:6]))
                    print()
        # if number_of_episodes > 2:
        #     break
