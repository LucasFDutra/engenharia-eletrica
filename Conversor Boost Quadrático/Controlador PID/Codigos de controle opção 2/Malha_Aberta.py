#---------------------------------------#
# Titulo: Biblioteca Malha aberta       #
# Autor: Lucas Felipe Dutra             #
#---------------------------------------#

#----------------------------------Bibliotecas-----------------------------------------#
import PWM

#----------------------------------Loop do PWM-----------------------------------------#
def pulso(porta, frequencia, duty_cycle):
    #--------------------------Configurações da placa----------------------------------#
    pwm = PWM.pwm(2)
    pwm.set_frequency(porta,frequencia)
    #------------------Tenta executar o PWM com um dado duty cycle---------------------#
    try:
        while True:
            pwm.set_duty_cycle(porta, duty_cycle)   # Define o duty cycle que utilizaremos
    except KeyboardInterrupt:
        pass
    #----------------------------Após o término do código------------------------------#
    pwm.write(sb, 0)
    pwm.stop()
