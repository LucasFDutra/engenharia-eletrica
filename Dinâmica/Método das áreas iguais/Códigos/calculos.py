import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
# from scipy.interpolate import interp1d

def Calculos(X, U, S, H):
    Pmec = S.real
    I = S/U
    I = I.conjugate()
    E = U+(X[0]*I)
    DELTA_0 = np.angle(E)
    Pmax_list = []
    for i in range(3):
        Pmax = (abs(E)*abs(U))/(abs(X[i]))
        Pmax_list.append(Pmax)
    DELTA_max = np.pi-np.arcsin(Pmec/Pmax_list[2])
    DELTA_cc = np.arccos(((Pmec*(DELTA_0-DELTA_max))+(Pmax_list[1]*np.cos(DELTA_0))-(Pmax_list[2]*np.cos(DELTA_max)))/(Pmax_list[1]-Pmax_list[2]))
    return I, E, Pmec, Pmax_list, DELTA_0, DELTA_cc, DELTA_max

def Interpolacao(t,delta):
    f = np.polyfit(t,delta,deg=3)
    return f

def SolvePoly(y, p):
    p[3]-=y
    x = np.roots(p)
    for i in range(len(x)):
        if x[i].imag == 0 and x[i].real > 0:
            raiz = x[i].real
    return raiz
