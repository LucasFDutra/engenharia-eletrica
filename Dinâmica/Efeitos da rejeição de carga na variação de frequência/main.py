import numpy as np
import matplotlib.pyplot as plt

def f_equation(f0, H, Pa):
    t = np.linspace(0,7,1000)
    f = f0 + (f0/(2*H))*Pa*t
    return f, t

def P_acelerante(P_gerada_total, P_carga, P_retirada):
    Pgr = P_gerada_total-P_retirada
    Pa = (Pgr - P_carga)/Pgr
    return Pa

# Variáveis gerais 2 e 3
PG1, PG2, PG3, PG4 = 0.5, 2, 1.5, 1

#-----------------------------------Número 2-----------------------------------#
# Mantendo a inércia constante e variando a potência gerada remanescente       #
#------------------------------------------------------------------------------#
plt.figure(figsize=(12,7))
Heq, f0, PL, Pg = 3, 60, 5, 5

# caso A1 Saida de G1
Pa = P_acelerante(Pg, PL, PG1)
f, t = f_equation(f0, Heq, Pa)
plt.plot(t, f, color='red', label='Saida de G1, PG = '+str(PG1))

# caso B1 Saida de G4
Pa = P_acelerante(Pg, PL, PG4)
f, t = f_equation(f0, Heq, Pa)
plt.plot(t, f, color='blue', label='Saida de G4, PG = '+str(PG4))

# caso C1 Saida de G3
Pa = P_acelerante(Pg, PL, PG3)
f, t = f_equation(f0, Heq, Pa)
plt.plot(t, f, color='green', label='Saida de G3, PG = '+str(PG3))

# caso D1 Saida de G2
Pa = P_acelerante(Pg, PL, PG2)
f, t = f_equation(f0, Heq, Pa)
plt.plot(t, f, color='orange', label='Saida de G4, PG = '+str(PG2))

plt.title('Inércia constante e potência remanescente variante')
plt.xlabel('Tempo [s]')
plt.ylabel('frequência [Hz]')
plt.grid(True)
plt.legend()
plt.savefig('Exercicio 2')
plt.show()

#-----------------------------------Número 3-----------------------------------#
# Mantendo a potência gerada remanescente e variando a inércia                 #
#------------------------------------------------------------------------------#
plt.figure(figsize=(12,7))
H1, H2, H3, P_retirada = 3, 5, 7, PG2

# caso A2 Saida de G2 Heq = 3
Pa = P_acelerante(Pg, PL, P_retirada)
f, t = f_equation(f0, H1, Pa)
plt.plot(t, f, color='red', label='Saida de G2, Heq = '+str(H1))

# caso B2 Saida de G2 Heq = 5
Pa = P_acelerante(Pg, PL, P_retirada)
f, t = f_equation(f0, H2, Pa)
plt.plot(t, f, color='blue', label='Saida de G2, Heq = '+str(H2))

# caso C2 Saida de G2 Heq = 7
Pa = P_acelerante(Pg, PL, P_retirada)
f, t = f_equation(f0, H3, Pa)
plt.plot(t, f, color='green', label='Saida de G2, Heq = '+str(H3))

plt.title('Potência remanescente constante e inércia variante')
plt.xlabel('Tempo [s]')
plt.ylabel('frequência [Hz]')
plt.grid(True)
plt.legend()
plt.savefig('Exercicio 3')
plt.show()

#-----------------------------------Número 4-----------------------------------#
# Rejeição de carga                                                            #
#------------------------------------------------------------------------------#
# Variáveis gerais
plt.figure(figsize=(12,7))
PG1, PG2, Heq, P_retirada, PL = 0.5, 4.5, 3, 0.5, 5
Pa = P_acelerante(Pg, PL, P_retirada)
Sc = -Pa

# Antes da rejeição
f, t = f_equation(f0, Heq, Pa)
t_ = np.where(t>=1.4)[0][0]
f = f[0:t_]

# caso 1 Rejeição igual a Sc
PL_ = PL - Sc*PL
Pa_ = P_acelerante(Pg, PL_, P_retirada)
f_, t = f_equation(f[-1], Heq, Pa_)
f_ = f_[0:len(t)-t_]
f_ = np.append(f, f_)
plt.plot(t, f_, color='green', label='Rejeição igual a Sc')

# caso 2 Rejeição igual a 30%
PL_ = PL - 0.3*PL
Pa_ = P_acelerante(Pg, PL_, P_retirada)
f_, t = f_equation(f[-1], Heq, Pa_)
f_ = f_[0:len(t)-t_]
f_ = np.append(f, f_)
plt.plot(t, f_, color='red', label='Rejeição igual a 30%')

# caso 3 Rejeição igual a 5%
PL_ = PL - 0.05*PL
Pa_ = P_acelerante(Pg, PL_, P_retirada)
f_, t = f_equation(f[-1], Heq, Pa_)
f_ = f_[0:len(t)-t_]
f_ = np.append(f, f_)
plt.plot(t, f_, color='blue', label='Rejeição igual a 5%')

plt.title('Rejeição de carga')
plt.xlabel('Tempo [s]')
plt.ylabel('frequência [Hz]')
plt.grid(True)
plt.legend()
plt.savefig('Exercicio 4')
plt.show()
