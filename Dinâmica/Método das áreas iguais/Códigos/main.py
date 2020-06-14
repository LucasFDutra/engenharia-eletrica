import tabela as tb
import calculos as ca
import parametros as pr
import graficos as gf

X = [complex(0,0.65), complex(0,1.8), complex(0,0.8)]
U = 1
H = 5
F = 60

cont = 0
delta_list = []
f_list = []
# plotando gráficos para 5 S diferentes
S_list = [0.8, 0.9, 1, 1.1, 1.2]
for i in S_list:
    S = complex(i, 0.074)
    I, E, Pmec, Pmax_list, DELTA_0, DELTA_cc, DELTA_max = ca.Calculos(X, U, S, H)
    t, deltas = tb.Tabela(H, F, Pmec, Pmax_list, DELTA_0)
    delta_list.append(deltas)
    y = ca.Interpolacao(t,deltas)
    f = (y[3]) + (y[2]*t) + (y[1]*(t**2)) + (y[0]*(t**3))
    f_list.append(f)
    Tcc = ca.SolvePoly(DELTA_cc, y)
    gf.Potencia_x_Delta(E, I, Pmec, Pmax_list, DELTA_0, DELTA_cc, DELTA_max, Tcc, cont)
    cont+=1
S = complex(0.8,0.074)
gf.Delta_x_Tempo(t, delta_list, f_list)
gf.Delta_cc_x_Pmec(X, U, S, H, Pmax_list[0], cont)
gf.Tcc_x_H(X, U, S, F, cont)
