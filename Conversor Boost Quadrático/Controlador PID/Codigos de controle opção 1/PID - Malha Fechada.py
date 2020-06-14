#---------------------------------------#
# Boost Quadrático - Malha aberta       #
# Autor: Lucas Felipe Dutra             #
#---------------------------------------#

#-------------------------------------Bibliotecas--------------------------------------#
import PWM
import serial
from time import time

#-------------------------------Leitura AD da referência-------------------------------#
def leituraAD():
    Vref_medido = arduino.readline()
    try:
        return((int(Vref_medido)*5)/1023)
    except:
        return leituraAD()

#------------------------------Parâmetros do controlador-------------------------------#
KP = 6.1603*(10**(-4))
KI = 1.1544
KD = 1.5413*(10**(-6))
Hv = 0.1
Vref = 10
Limite_do_Saturador = 60
Frequencia = 10000

#---------------------------------Configurações da placa-------------------------------#
sb = 2                          # pino 2 é o de chaveamento
pwm = PWM.pwm(2)
arduino = serial.Serial('/dev/ttyACM1', 115200) # Comunica com o arduino a 115.2 KHz
pwm.set_frequency(sb,Frequencia)

#-----------------------------------Loop de chaveamento--------------------------------#
try:
    erro_D = 0
    DI = 0
    t = time()                  # pega o instante em que se inicia o código de controle
    while True:
        #----------------------tempo de execução do loop-------------------------------#
        delta_t = time() - t
        t = time()

        #---------------------------Obtenção do erro-----------------------------------#
        erro = Vref - (leituraAD()/Hv)

        #-------------------------Controle Proporcional--------------------------------#
        DP = erro*KP

        #--------------------------Controle Derivativo---------------------------------#
        DD = (erro_D - erro)*KD/delta_t
        erro_D = erro

        #--------------------------Controle Integrador---------------------------------#
        DI += KI*erro*delta_t
        if DI > Limite_do_Saturador/100:
            DI = Limite_do_Saturador/100
        elif DI < 0:
            DI = 0

        #-------------------------------Saturador--------------------------------------#
        D = (DP+DD+DI)*100
        if D > Limite_do_Saturador:
            D = Limite_do_Saturador
        if D < 0:
            D = 0

        #---------------------------Variando o Duty Cycle------------------------------#
        pwm.set_duty_cycle(sb,D)   # o duty_cycle é ajustado para D

except KeyboardInterrupt:
    pass

#------------------------------Após termos parado o código-----------------------------#
pwm.write(sb,0)
pwm.stop()
