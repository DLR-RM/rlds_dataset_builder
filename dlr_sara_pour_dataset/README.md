# Robot learns to pour liquid from a thermos held in end-effector gripper into the mug placed on the table. 

- observation : 
    - image : shape=(480, 640, 3),

    - state : Robot state, consists of 
        - 3x robot EEF position, 
        - 3x robot EEF orientation yaw/pitch/roll calculated with scipy Rotation.as_euler(="zxy") Class

- action : Robot action, consists of 
  - 3x robot EEF position "delta" in the Robot base frame,
  - 3x robot EEF orientation "delta" yaw/pitch/roll calculated with scipy Rotation.as_euler(="zxy") Class in the Robot base frame



