import numpy as np

def change_order(sequences, p):
    # quanto maior o p menor é a distancia e menos pior é essa ordem
    p0 = 0.3
    p1 = 0.7
    p2 = 0.98
    p3 = 1
    entropies = np.array([p0, p1, p2, p3])

    i = np.where(entropies>=p)[0][0]
    if i == 3 and np.random.random() <= 0.1:
        i = np.random.randint(1,4)

    sequences_new = []

    if i == 0:
        for sequence in sequences:
            sequence = np.random.permutation(sequence)
            sequences_new.append(sequence)

    elif i == 1:
        for sequence in sequences:
            mutation_points = np.random.randint(0, len(sequence), 2)
            mutation_points = np.sort(mutation_points)
            sequence[mutation_points[0]:mutation_points[1]] = np.random.permutation(sequence[mutation_points[0]:mutation_points[1]])
            sequences_new.append(sequence)

    elif i == 2:
        for sequence in sequences:
            mutation_points = np.random.randint(0, len(sequence), 2)
            x = sequence[mutation_points[0]]
            sequence[mutation_points[0]] = sequence[mutation_points[1]]
            sequence[mutation_points[1]] = x
            sequences_new.append(sequence)

    elif i == 3:
        sequences_new = sequences.copy()

    return sequences_new
