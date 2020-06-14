import Malha_Aberta as ma
import PID_Controller as P

escolha = int(input('malha aberta = 1 \nmalha fechada = 2 \n'))

if escolha == 1:
    #ma.pulso(porta, frequência, duty_cycle)
    ma.pulso(2, 10000, 50)
if escolha == 2:
    #PID(porta, Frequencia, KP, KI, KD, Hv, Vref, Limite_do_Saturador):
    P.PID(2, 10000, 6.1603*(10**(-4)), 1.1544, 1.5413*(10**(-6)), 0.1, 20, 60)
