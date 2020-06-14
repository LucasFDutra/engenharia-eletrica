#---------------------------------------#
# Boost Quadrático - Malha aberta       #
# Autor: Lucas Felipe Dutra             #
#---------------------------------------#

#-------------------------------------Bibliotecas--------------------------------------#
import PWM

#-------------------------------Definição da razão ciclica-----------------------------#
D = 50

#---------------------------------Configurações da placa-------------------------------#
sb = 2
pwm = PWM.pwm(2)
frequencia = 10000
pwm.set_frequency(sb,frequencia)

#-----------------------------------Loop de chaveamento--------------------------------#
try:
    while True:
        pwm.set_duty_cycle(sb,D)
except KeyboardInterrupt:
    pass

#------------------------------Após termos parado o código-----------------------------#
pwm.write(sb, 0)
pwm.stop()
