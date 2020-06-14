import numpy as np
import updateQ
import choice
import change_order as co
import traveling_Q
import reward
import pandas as pd
import progressbar


def fit(R, Q, n_agents, n_repositories, n_objects, epochs=250, sub_epochs=25, gamma=0.8, alpha=0.9):
    best_reward = 0
    dim_env = len(R)
    sequence_len = int(2 * np.ceil(n_objects/n_agents))
    new_rewards = []
    sequences = []
    bests_rewards = []
    ps = []
    p = 1

    pbar = progressbar.ProgressBar()
    for i in range(sequence_len):
        sequences.append(np.random.permutation(n_agents))

    Q_ = Q.copy()
    for i in pbar(range(epochs)):
        new_sequences = co.change_order(sequences, p)

        for j in range(sub_epochs):
            R_ = R.copy()
            states_x = np.arange(n_agents, dtype=int)
            states_y = np.zeros(n_agents, dtype=int)

            for k in range(sequence_len):
                choice_order = new_sequences[k].copy()
                for k1 in choice_order:
                    k1 = int(k1)
                    states_y[k1] = choice.x_to_y(R_, states_x[k1])
                    if states_y[k1] >= n_agents:
                        R_, Q_ = updateQ.updateQ(
                            R_, Q_, states_x[k1], states_y[k1], n_repositories, dim_env, gamma, alpha)
                states_x = states_y.copy()
                states_y = np.zeros(n_agents, dtype=int)

        steps = traveling_Q.traveling_Q(
            Q_, new_sequences, dim_env, n_repositories, n_agents)
        new_Reward = reward.reward(R, steps, n_agents)
        new_rewards.append(new_Reward)

        if new_Reward >= best_reward:
            best_reward = new_Reward
            best_sequences = new_sequences.copy()
            sequences = new_sequences.copy()
            best_Q = Q_.copy()
            best_steps = steps.copy()
            delta = (new_Reward-best_reward)/best_reward
            p = np.exp(delta)
        else:
            delta = (new_Reward-best_reward)/best_reward
            p = np.exp(delta)
            if p >= 0.9 and np.random.random() <= 0.1:
                sequences = new_sequences.copy()
            else:
                sequences = best_sequences.copy()

        ps.append(p)
        bests_rewards.append(best_reward)

    return best_Q, best_sequences, new_rewards, bests_rewards, best_steps, ps
