import os
import numpy as np
import matplotlib.pyplot as plt
import time

os.system('gcc ../Listas/doublyChainedCircularList_img02.c -o ../Listas/doublyChainedCircularList_img02.run')
os.system('gcc ../Listas/doublyChainedCircularList_img03.c -o ../Listas/doublyChainedCircularList_img03.run')
os.system('gcc ../Listas/simpleLinkedList_img02.c -o ../Listas/simpleLinkedList_img02.run')
os.system('gcc ../Listas/simpleLinkedList_img03.c -o ../Listas/simpleLinkedList_img03.run')

timeDoubleChainList_02 = np.array([])
timeDoubleChainList_03 = np.array([])
timeSimpleList_02 = np.array([])
timeSimpleList_03 = np.array([])

for i in range(3):
    initialTime = time.time()
    os.system('../Listas/doublyChainedCircularList_img02.run')
    finalTime = time.time()
    timeDoubleChainList_02 = np.append(
        timeDoubleChainList_02, finalTime-initialTime)

for i in range(3):
    initialTime = time.time()
    os.system('../Listas/doublyChainedCircularList_img03.run')
    finalTime = time.time()
    timeDoubleChainList_03 = np.append(
        timeDoubleChainList_03, finalTime-initialTime)

for i in range(3):
    initialTime = time.time()
    os.system('../Listas/simpleLinkedList_img02.run')
    finalTime = time.time()
    finalTime = time.time()
    timeSimpleList_02 = np.append(timeSimpleList_02, finalTime-initialTime)

for i in range(3):
    initialTime = time.time()
    os.system('../Listas/simpleLinkedList_img03.run')
    finalTime = time.time()
    finalTime = time.time()
    timeSimpleList_03 = np.append(timeSimpleList_03, finalTime-initialTime)

plt.figure()
plt.plot(timeDoubleChainList_02, color='r', label='lista duplamente encadeada', marker='o')
plt.plot(timeSimpleList_02, color='b', label='lista simples', marker='o')
plt.legend()
plt.title('Imagem img002.pgm')
plt.savefig('grafico img002.png')

plt.figure()
plt.plot(timeDoubleChainList_03, color='r', label='lista duplamente encadeada', marker='o')
plt.plot(timeSimpleList_03, color='b', label='lista simples', marker='o')
plt.legend()
plt.title('Imagem img003.pgm')
plt.savefig('grafico img003.png')

plt.figure()
plt.plot(timeDoubleChainList_02, color='r', label='lista duplamente encadeada', marker='o')
plt.legend()
plt.title('Imagem img002.pgm')
plt.savefig('Somente a duplamente encadeada - grafico img002.png')

plt.figure()
plt.plot(timeDoubleChainList_03, color='r', label='lista duplamente encadeada', marker='o')
plt.legend()
plt.title('Imagem img003.pgm')
plt.savefig('Somente a duplamente encadeada - grafico img003.png')