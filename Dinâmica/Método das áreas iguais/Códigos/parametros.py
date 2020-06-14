def Parametro_X():
    Xr = [float(i) for i in input('Digite as partes REAIS de X: ').split(' ')]
    Xi = [float(i) for i in input('Digite as partes IMG de X: ').split(' ')]
    X = [complex(Xr[i], Xi[i]) for i in range(len(Xr))]
    return X

def Parametro_U():
    Ur = float(input('digite a parte REAL de U: '))
    Ui = float(input('digite a parte IMG de U: '))
    U = complex(Ur, Ui)
    return U

def Parametro_S():
    P = float(input('digite o valor da potência ativa: '))
    Q = float(input('digite o valor da potência reativa: '))
    S = complex(P,Q)
    return S

def Parametro_H():
    H = float(input('digite o valor da constante de inércia da máquina: '))
    return H

def Parametro_F():
    f = float(input('digite o valor da frequência do sistema: '))
    return f
