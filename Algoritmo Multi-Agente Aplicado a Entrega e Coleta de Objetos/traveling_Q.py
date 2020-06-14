import numpy as np

def traveling_Q(Q_, sequences, dim_env, n_repositories, n_agents):
    Q = Q_.copy()
    states_x = np.arange(n_agents, dtype = int)
    states_y = np.zeros(n_agents, dtype = int)

    steps = [states_x]

    for choice_order in sequences:
        for i in choice_order:
            i = int(i)
            y_index = np.where(Q[states_x[i]] >= np.max(Q[states_x[i]]))[0]
            if y_index[0] == 0:
                y_index = 0
            elif y_index.shape[0] > 1:
                y_index = int(np.random.choice(y_index, 1))
            else:
                y_index = int(y_index)

            states_y[i] = y_index

            if states_y[i] >= (dim_env-n_repositories):
                Q[states_x[i], states_y[i]] = 0
            else:
                Q[:,states_y[i]] = 0

        states_x = states_y.copy()
        steps.append(states_x)
        states_y = np.zeros(n_agents, dtype=int)
    return steps
