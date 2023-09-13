
Multiple tasks on the assistive robot edan, using Shared Control Templates.

- observation : 
    - image : shape=(360, 640, 3),

    - state : Robot state, consists of 
        - 3x robot EEF position, 
        - 3x robot EEF orientation yaw/pitch/roll ("zxy" format) Class in the Robot base frame
        - homogeneous transformation matrix in the raw data

- action : Robot action, consists of 
  - 3x robot EEF position "delta" in the Robot base frame,
  - 3x robot EEF orientation "delta" yaw/pitch/roll ("zxy" format) Class in the Robot base frame



