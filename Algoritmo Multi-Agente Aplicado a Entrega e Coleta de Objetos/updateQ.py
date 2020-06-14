import numpy as np

def updateQ(R_, Q, state_x, state_y, n_repositories, dim, gamma, alpha):
    next_index = np.where(Q[state_y] >= alpha*np.max(Q[state_y]))[0]
    if next_index[0] == 0:
        next_index = 0
    elif next_index.shape[0] > 1:
        next_index = int(np.random.choice(next_index, 1))
    else:
        next_index = int(next_index)

    future_reward = Q[state_y, next_index]

    Q[state_x, state_y] = R_[state_x, state_y] + gamma*future_reward

    if state_y >= (dim-n_repositories):
        R_[state_x, state_y] = -1
    else:
        R_[:,state_y] = -1

    return R_, Q
