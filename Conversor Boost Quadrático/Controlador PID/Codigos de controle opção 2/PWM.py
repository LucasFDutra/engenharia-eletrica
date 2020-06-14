#--------------------------------------#
# Titulo: Biblioteca de PWM            #
# Autor: Lucas Felipe Dutra            #
#--------------------------------------#

#--------------------------------------------------------------------------------------#
#                                      Hertz                                           #
#              1: 40000 20000 10000 8000 5000 4000 2500 2000 1600                      #
#                  1250  1000   800  500  400  250  200  100   50                      #
#                                                                                      #
#               2: 20000 10000  5000 4000 2500 2000 1250 1000  800                     #
#                    625   500   400  250  200  125  100   50   25                     #
#                                                                                      #
#               4: 10000  5000  2500 2000 1250 1000  625  500  400                     #
#                    313   250   200  125  100   63   50   25   13                     #
#        sample                                                                        #
#         rate                                                                         #
#         (us)  5:  8000  4000  2000 1600 1000  800  500  400  320                     #
#                    250   200   160  100   80   50   40   20   10                     #
#                                                                                      #
#               8:  5000  2500  1250 1000  625  500  313  250  200                     #
#                    156   125   100   63   50   31   25   13    6                     #
#                                                                                      #
#              10:  4000  2000  1000  800  500  400  250  200  160                     #
#                    125   100    80   50   40   25   20   10    5                     #
#--------------------------------------------------------------------------------------#
# OBS.: Depois de escolher uma faixa de uso do PWM você só consegue trocar reiniciando #
# O raspberry.                                                                         #
#--------------------------------------------------------------------------------------#

#------------------------------------Bibliotecas---------------------------------------#
import pigpio
import os

#------------------------------------Objeto PWM----------------------------------------#
class pwm:
    #-----------------------definindo faixa de frequência------------------------------#
    def __init__(self, faixa):
        if faixa == 1:
            command = 'sudo pigpiod -s 1'
        elif faixa == 2:
            command = 'sudo pigpiod -s 2'
        elif faixa == 4:
            command = 'sudo pigpiod -s 4'
        elif faixa == 5:
            command = 'sudo pigpiod -s 5'
        elif faixa == 8:
            command = 'sudo pigpiod -s 8'
        elif faixa == 10:
            command = 'sudo pigpiod -s 10'

        os.system(command)

        #------------------------------------------------------------------------------#
        # OBS.: se seu raspberry tiver senha para comandos como root,não use o comando #
        # anterior, use o comando abaixo e coloque a sua senha no lugar de password    #
        # e retire o a palava "sudo" das strings nos if.                               #
        #                                                                              #
        # os.system('echo %s|sudo -S %s' % (password, command))                        #
        #------------------------------------------------------------------------------#

        self.pi = pigpio.pi()

    #------------------------------Definindo a Frequência------------------------------#
    def set_frequency(self, porta, frequencia):
        self.pi.set_mode(porta, pigpio.OUTPUT)
        self.pi.set_PWM_frequency(porta, frequencia)
        #print('Frequência: {}'.format(self.pi.get_PWM_frequency(porta)))

    #------------------------------Definindo o Duty Cycle------------------------------#
    def set_duty_cycle(self, porta, duty_cycle):
        self.pi.set_PWM_dutycycle(porta, int(duty_cycle*255/100))
        #print('Duty Cycle: {}'.format(int(self.pi.get_PWM_dutycycle(porta)*100/255)))

    #-------------Define se queremos a porta em nivel alto ou baixo constante----------#
    def write(self, porta, nivel):
        self.pi.write(porta, nivel)

    #--------------------------Interrompemos o uso das portas--------------------------#
    def stop(self):
        self.pi.stop()
