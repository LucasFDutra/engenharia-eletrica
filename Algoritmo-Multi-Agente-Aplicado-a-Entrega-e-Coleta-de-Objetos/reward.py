import numpy as np

def reward(R, steps, n_agents):
    reward_total = 0

    s_len = len(steps)-1

    for i in range(n_agents):
        for k in range(s_len):
            if steps[k+1][i]>=n_agents:
                reward_total += R[steps[k][i], steps[k+1][i]]
    return reward_total
