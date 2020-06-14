import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import calculos as ca
import tabela as tb

def Potencia_x_Delta(E, I, Pmec, Pmax_list, DELTA_0, DELTA_cc, DELTA_max, Tcc, cont):
    DELTA = np.arange(0,np.pi,0.001)

    p_mec = Pmec+(DELTA-DELTA)
    colors = ['black', 'blue', 'yellow', 'cyan']
    potencias = [p_mec]

    for i in range(4):
        if i>0:
            potencias.append(Pmax_list[i-1]*np.sin(DELTA))
        plt.plot(DELTA, potencias[i], color=colors[i])

    plt.fill_between(DELTA, potencias[0], potencias[2], where = DELTA>=DELTA_0, facecolor='red', interpolate=True)
    plt.fill_between(DELTA, potencias[0], potencias[2], where = DELTA>DELTA_cc, facecolor='w', interpolate=True)

    plt.fill_between(DELTA, potencias[0], potencias[3], where = DELTA>=DELTA_cc, facecolor='green', interpolate=True)
    plt.fill_between(DELTA, potencias[0], potencias[3], where = DELTA>DELTA_max, facecolor='w', interpolate=True)

    font_size = 12
    plt.text(0, (Pmax_list[0]-(font_size*1/100)), 'E: '+ str(E), {'color': 'black', 'fontsize': font_size})
    plt.text(0, (Pmax_list[0]-(font_size*2/100)), 'I: '+ str(I), {'color': 'black', 'fontsize': font_size})
    plt.text(0, (Pmax_list[0]-(font_size*3/100)), '$\delta$0: '+ str(round(DELTA_0, 4)), {'color': 'black', 'fontsize': font_size})
    plt.text(0, (Pmax_list[0]-(font_size*4/100)), '$\delta$max '+ str(round(DELTA_max, 4)), {'color': 'black', 'fontsize': font_size})
    plt.text(0, (Pmax_list[0]-(font_size*5/100)), '$\delta$cc: '+ str(round(DELTA_cc, 4)), {'color': 'black', 'fontsize': font_size})
    plt.text(0, (Pmax_list[0]-(font_size*6/100)), 'Tcc: '+ str(round(Tcc, 4)), {'color': 'black', 'fontsize': font_size})

    legend = [
        Line2D([0],[0],
              marker=5,
              color='w',
              label='Pmec',
              markerfacecolor=colors[0],
              markersize=10),
        Line2D([0],[0],
              marker=5,
              color='w',
              label='P_antes',
              markerfacecolor=colors[1],
              markersize=10),
        Line2D([0],[0],
              marker=5,
              color='w',
              label='P_durante',
              markerfacecolor=colors[2],
              markersize=10),
        Line2D([0],[0],
              marker=5,
              color='w',
              label='P_depois',
              markerfacecolor=colors[3],
              markersize=10),
        Line2D([0],[0],
              marker='o',
              color='w',
              label='A1',
              markerfacecolor='r',
              markersize=10),
        Line2D([0],[0],
              marker='o',
              color='w',
              label='A2',
              markerfacecolor='g',
              markersize=10),]

    plt.xlabel('ângulo [rad]')
    plt.ylabel('potência da máquina [pu]')
    plt.grid(True)
    plt.legend(handles=legend, loc='best')
    plt.savefig('Potencia_x_Delta_' + str(cont) + '.png')
    plt.close()

def Delta_x_Tempo(t, delta, y):
    dim = len(delta)
    colors = ['red', 'yellow', 'green', 'black', 'magenta']

    for i in range(dim):
        plt.scatter(t, delta[i], color='blue', marker='.', label='Pontos reais '+str(i))
        plt.plot(t, y[i], color=colors[i], label='Curva interpolada '+str(i))
    plt.xlabel('tempo [s]')
    plt.ylabel('delta [rad]')
    plt.grid(True)
    plt.legend(loc='best')
    plt.savefig('Delta_x_Tempo.png')
    plt.close()

def Delta_cc_x_Pmec(X, U, S, H, Pmax, cont):
    pm = S.real
    t = np.arange(pm,Pmax*0.9,0.01)
    Pmec_list = []
    Deltas = []
    for i in t:
        S = complex(i,S.imag)
        _, _, Pmec, _, _, DELTA_cc, _ = ca.Calculos(X, U, S, H)
        Pmec_list.append(Pmec)
        Deltas.append(DELTA_cc)
    plt.plot(Pmec_list, Deltas)
    plt.xlabel('Potência mecânica [pu]')
    plt.ylabel('delta_cc [rad]')
    plt.grid(True)
    plt.savefig('Delta_cc_x_Pmec_' + str(cont) + '.png')
    plt.close()

def Tcc_x_H(X, U, S, F, cont):
    h = np.arange(1,10,0.01)
    Tcc_list = []
    for i in h:
        _, _, Pmec, Pmax_list, DELTA_0, DELTA_cc, _ = ca.Calculos(X, U, S, i)
        t, deltas = tb.Tabela(i, F, Pmec, Pmax_list, DELTA_0)
        y = ca.Interpolacao(t,deltas)
        f = (y[3]) + (y[2]*t) + (y[1]*(t**2)) + (y[0]*(t**3))
        Tcc = ca.SolvePoly(DELTA_cc, y)
        Tcc_list.append(Tcc)
    plt.plot(h, Tcc_list)
    plt.xlabel('Constante de inércia [s]')
    plt.ylabel('Tempo de chaveamento [s]')
    plt.grid(True)
    plt.savefig('Tcc_x_H_' + str(cont) + '.png')
    plt.close()
