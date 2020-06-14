import numpy as np

def Tabela(H, F, Pmec, Pmax_list, DELTA_0):
    DELTA_t = 0.01
    k = (np.pi*F*(DELTA_t**2))/H

    Pe_01 = Pmax_list[1]*np.sin(DELTA_0)
    Pa_01 = Pmec-Pe_01
    Pa_02 = Pa_01/2
    K_Pa_02 = k*Pa_02
    DELTA_delta = K_Pa_02
    DELTA = DELTA_0

    deltas = [DELTA]

    t = np.arange(0,1,DELTA_t)
    intervalo = len(t)

    for i in range(intervalo-1):
        Pmax = Pmax_list[1]
        sen_d = np.sin(DELTA)
        Pe = Pmax*sen_d
        Pa = Pmec-Pe
        K_Pa = k*Pa
        DELTA_delta = DELTA_delta+K_Pa
        DELTA = DELTA+DELTA_delta
        deltas.append(DELTA)

    return t, deltas
