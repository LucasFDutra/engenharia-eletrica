import numpy as np

def CreateEnvironment(dir_agents, dir_objects, dir_repositories, f_mult=1):
    agents = np.genfromtxt(dir_agents, delimiter=',')
    objects = np.genfromtxt(dir_objects, delimiter=',')
    repositories = np.genfromtxt(dir_repositories, delimiter=',')

    n_objects = len(objects)
    n_agents = len(agents)
    n_repositories = len(repositories)

    dim_env = n_objects+n_agents+n_repositories
    R = -1*np.ones([dim_env, dim_env])
    Q = np.zeros([dim_env, dim_env])

    # Distancia entre agentes e objetos
    for i in range(n_agents):
        for j in range(n_objects):
            R[i,j+n_agents] = f_mult/np.linalg.norm(agents[i]-objects[j,0:2])

    # Distancia entre objetos e repositórios
    for i in range(n_objects):
        for j in range(n_repositories):
            if objects[i,2] == j:
                R[i+n_agents, j+n_agents+n_objects] = f_mult/np.linalg.norm(objects[i,0:2] - repositories[j])

    # Distancias entre repositórios e objetos
    for i in range(n_repositories):
        for j in range(n_objects):
            R[i+n_agents+n_objects, j+n_agents] = f_mult/np.linalg.norm(repositories[i] - objects[j,0:2])

    return R, Q, n_agents, n_repositories, n_objects
