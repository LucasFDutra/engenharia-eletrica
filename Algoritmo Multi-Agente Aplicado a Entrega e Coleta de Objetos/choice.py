import numpy as np

def x_to_y (R, state_x):
    try:
        possible_y = np.where(R[state_x] >= 0)[0]
        state_y = int(np.random.choice(possible_y, 1))
        return state_y
    except:
        return 0
