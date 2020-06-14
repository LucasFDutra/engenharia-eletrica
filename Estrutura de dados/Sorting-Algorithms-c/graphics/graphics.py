import os
import numpy as np
import matplotlib.pyplot as plt
import time

timeBubbleSort = np.array([])

timeBubbleSortArray1 = np.array([])
timeBubbleSortArray2 = np.array([])
timeBubbleSortArray3 = np.array([])
timeBubbleSortArray4 = np.array([])


timeInsertionSort = np.array([])

timeInsertionSortArray1 = np.array([])
timeInsertionSortArray2 = np.array([])
timeInsertionSortArray3 = np.array([])
timeInsertionSortArray4 = np.array([])

timeMergeSort = np.array([])

timeMergeSortArray1 = np.array([])
timeMergeSortArray2 = np.array([])
timeMergeSortArray3 = np.array([])
timeMergeSortArray4 = np.array([])

timeQuickSort = np.array([])

timeQuickSortArray1 = np.array([])
timeQuickSortArray2 = np.array([])
timeQuickSortArray3 = np.array([])
timeQuickSortArray4 = np.array([])

timeSelectionSort = np.array([])

timeSelectionSortArray1 = np.array([])
timeSelectionSortArray2 = np.array([])
timeSelectionSortArray3 = np.array([])
timeSelectionSortArray4 = np.array([])

os.system('gcc ../createArrays.c -o ../createArrays.run')
os.system('../createArrays.run')

print('criação do arquivo de array OK')

repeat = 5

for i in range(repeat):
    initialTimeBubbleSort = time.time()

    initalTime = time.time()
    os.system('./bubbleSort/bubbleSortArray1.sh')
    finalTime = time.time()
    timeBubbleSortArray1 = np.append(
        timeBubbleSortArray1, finalTime - initalTime)

    initalTime = time.time()
    os.system('./bubbleSort/bubbleSortArray2.sh')
    finalTime = time.time()
    timeBubbleSortArray2 = np.append(
        timeBubbleSortArray2, finalTime - initalTime)

    initalTime = time.time()
    os.system('./bubbleSort/bubbleSortArray3.sh')
    finalTime = time.time()
    timeBubbleSortArray3 = np.append(
        timeBubbleSortArray3, finalTime - initalTime)

    initalTime = time.time()
    os.system('./bubbleSort/bubbleSortArray4.sh')
    finalTime = time.time()
    timeBubbleSortArray4 = np.append(
        timeBubbleSortArray4, finalTime - initalTime)

    finalTimeBubbleSort = time.time()
    timeBubbleSort = np.append(
        timeBubbleSort, finalTimeBubbleSort - initialTimeBubbleSort)

print('fim do bubble sort')

for i in range(repeat):
    initialTimeInsertionSort = time.time()

    initalTime = time.time()
    os.system('./insertionSort/insertionSortArray1.sh')
    finalTime = time.time()
    timeInsertionSortArray1 = np.append(
        timeInsertionSortArray1, finalTime - initalTime)

    initalTime = time.time()
    os.system('./insertionSort/insertionSortArray2.sh')
    finalTime = time.time()
    timeInsertionSortArray2 = np.append(
        timeInsertionSortArray2, finalTime - initalTime)

    initalTime = time.time()
    os.system('./insertionSort/insertionSortArray3.sh')
    finalTime = time.time()
    timeInsertionSortArray3 = np.append(
        timeInsertionSortArray3, finalTime - initalTime)

    initalTime = time.time()
    os.system('./insertionSort/insertionSortArray4.sh')
    finalTime = time.time()
    timeInsertionSortArray4 = np.append(
        timeInsertionSortArray4, finalTime - initalTime)

    finalTimeInsertionSort = time.time()
    timeInsertionSort = np.append(
        timeInsertionSort, finalTimeInsertionSort - initialTimeInsertionSort)

print('fim do Insertion sort')

for i in range(repeat):
    initialTimeMergeSort = time.time()

    initalTime = time.time()
    os.system('./mergeSort/mergeSortArray1.sh')
    finalTime = time.time()
    timeMergeSortArray1 = np.append(
        timeMergeSortArray1, finalTime - initalTime)

    initalTime = time.time()
    os.system('./mergeSort/mergeSortArray2.sh')
    finalTime = time.time()
    timeMergeSortArray2 = np.append(
        timeMergeSortArray2, finalTime - initalTime)

    initalTime = time.time()
    os.system('./mergeSort/mergeSortArray3.sh')
    finalTime = time.time()
    timeMergeSortArray3 = np.append(
        timeMergeSortArray3, finalTime - initalTime)

    initalTime = time.time()
    os.system('./mergeSort/mergeSortArray4.sh')
    finalTime = time.time()
    timeMergeSortArray4 = np.append(
        timeMergeSortArray4, finalTime - initalTime)

    finalTimeMergeSort = time.time()
    timeMergeSort = np.append(
        timeMergeSort, finalTimeMergeSort - initialTimeMergeSort)

print('fim do Merge sort')


for i in range(repeat):
    initialTimeQuickSort = time.time()

    initalTime = time.time()
    os.system('./quickSort/quickSortArray1.sh')
    finalTime = time.time()
    timeQuickSortArray1 = np.append(
        timeQuickSortArray1, finalTime - initalTime)

    initalTime = time.time()
    os.system('./quickSort/quickSortArray2.sh')
    finalTime = time.time()
    timeQuickSortArray2 = np.append(
        timeQuickSortArray2, finalTime - initalTime)

    initalTime = time.time()
    os.system('./quickSort/quickSortArray3.sh')
    finalTime = time.time()
    timeQuickSortArray3 = np.append(
        timeQuickSortArray3, finalTime - initalTime)

    initalTime = time.time()
    os.system('./quickSort/quickSortArray4.sh')
    finalTime = time.time()
    timeQuickSortArray4 = np.append(
        timeQuickSortArray4, finalTime - initalTime)

    finalTimeQuickSort = time.time()
    timeQuickSort = np.append(
        timeQuickSort, finalTimeQuickSort - initialTimeQuickSort)

print('fim do Quick sort')


for i in range(repeat):
    initialTimeSelectionSort = time.time()

    initalTime = time.time()
    os.system('./selectionSort/selectionSortArray1.sh')
    finalTime = time.time()
    timeSelectionSortArray1 = np.append(
        timeSelectionSortArray1, finalTime - initalTime)

    initalTime = time.time()
    os.system('./selectionSort/selectionSortArray2.sh')
    finalTime = time.time()
    timeSelectionSortArray2 = np.append(
        timeSelectionSortArray2, finalTime - initalTime)

    initalTime = time.time()
    os.system('./selectionSort/selectionSortArray3.sh')
    finalTime = time.time()
    timeSelectionSortArray3 = np.append(
        timeSelectionSortArray3, finalTime - initalTime)

    initalTime = time.time()
    os.system('./selectionSort/selectionSortArray4.sh')
    finalTime = time.time()
    timeSelectionSortArray4 = np.append(
        timeSelectionSortArray4, finalTime - initalTime)

    finalTimeSelectionSort = time.time()
    timeSelectionSort = np.append(
        timeSelectionSort, finalTimeSelectionSort - initialTimeSelectionSort)

print('fim do Selection sort')

plt.figure(figsize=(20, 10))
plt.title('Tempos gastos no algoritmo Bubble Sort')
plt.plot(timeBubbleSortArray1, color='red', label='Array 1')
plt.plot(timeBubbleSortArray2, color='blue', label='Array 2')
plt.plot(timeBubbleSortArray3, color='green', label='Array 3')
plt.plot(timeBubbleSortArray4, color='black', label='Array 4')
y = np.max([timeBubbleSortArray1, timeBubbleSortArray2, timeBubbleSortArray3, timeBubbleSortArray4])
plt.text(x=0,y=y, s='Média Array1: '+str(np.around(np.mean(timeBubbleSortArray1), 2)), fontsize=20)
plt.text(x=0.9,y=y, s='Média Array2: '+str(np.around(np.mean(timeBubbleSortArray2), 2)), fontsize=20)
plt.text(x=1.8,y=y, s='Média Array3: '+str(np.around(np.mean(timeBubbleSortArray3), 2)), fontsize=20)
plt.text(x=2.7,y=y, s='Média Array4: '+str(np.around(np.mean(timeBubbleSortArray4), 2)), fontsize=20)
plt.legend(loc=1, prop={'size': 20})
plt.savefig('Bubble Sort Por Array.png')


plt.figure(figsize=(20, 10))
plt.title('Tempos gastos no algoritmo Insertion Sort')
plt.plot(timeInsertionSortArray1, color='red', label='Array 1')
plt.plot(timeInsertionSortArray2, color='blue', label='Array 2')
plt.plot(timeInsertionSortArray3, color='green', label='Array 3')
plt.plot(timeInsertionSortArray4, color='black', label='Array 4')
y = np.max([timeInsertionSortArray1, timeInsertionSortArray2, timeInsertionSortArray3, timeInsertionSortArray4])
plt.text(x=0,y=y, s='Média Array1: '+str(np.around(np.mean(timeInsertionSortArray1), 2)), fontsize=20)
plt.text(x=0.9,y=y, s='Média Array2: '+str(np.around(np.mean(timeInsertionSortArray2), 2)), fontsize=20)
plt.text(x=1.8,y=y, s='Média Array3: '+str(np.around(np.mean(timeInsertionSortArray3), 2)), fontsize=20)
plt.text(x=2.7,y=y, s='Média Array4: '+str(np.around(np.mean(timeInsertionSortArray4), 2)), fontsize=20)
plt.legend(loc=1, prop={'size': 20})
plt.savefig('Insertion Sort Por Array.png')

plt.figure(figsize=(20, 10))
plt.title('Tempos gastos no algoritmo Merge Sort')
plt.plot(timeMergeSortArray1, color='red', label='Array 1')
plt.plot(timeMergeSortArray2, color='blue', label='Array 2')
plt.plot(timeMergeSortArray3, color='green', label='Array 3')
plt.plot(timeMergeSortArray4, color='black', label='Array 4')
y = np.max([timeMergeSortArray1, timeMergeSortArray2, timeMergeSortArray3, timeMergeSortArray4])
plt.text(x=0,y=y, s='Média Array1: '+str(np.around(np.mean(timeMergeSortArray1), 2)), fontsize=20)
plt.text(x=0.9,y=y, s='Média Array2: '+str(np.around(np.mean(timeMergeSortArray2), 2)), fontsize=20)
plt.text(x=1.8,y=y, s='Média Array3: '+str(np.around(np.mean(timeMergeSortArray3), 2)), fontsize=20)
plt.text(x=2.7,y=y, s='Média Array4: '+str(np.around(np.mean(timeMergeSortArray4), 2)), fontsize=20)
plt.legend(loc=1, prop={'size': 20})
plt.savefig('Merge Sort Por Array.png')

plt.figure(figsize=(20, 10))
plt.title('Tempos gastos no algoritmo Quick Sort')
plt.plot(timeQuickSortArray1, color='red', label='Array 1')
plt.plot(timeQuickSortArray2, color='blue', label='Array 2')
plt.plot(timeQuickSortArray3, color='green', label='Array 3')
plt.plot(timeQuickSortArray4, color='black', label='Array 4')
y = np.max([timeQuickSortArray1, timeQuickSortArray2, timeQuickSortArray3, timeQuickSortArray4])
plt.text(x=0,y=y, s='Média Array1: '+str(np.around(np.mean(timeQuickSortArray1), 2)), fontsize=20)
plt.text(x=0.9,y=y, s='Média Array2: '+str(np.around(np.mean(timeQuickSortArray2), 2)), fontsize=20)
plt.text(x=1.8,y=y, s='Média Array3: '+str(np.around(np.mean(timeQuickSortArray3), 2)), fontsize=20)
plt.text(x=2.7,y=y, s='Média Array4: '+str(np.around(np.mean(timeQuickSortArray4), 2)), fontsize=20)
plt.legend(loc=1, prop={'size': 20})
plt.savefig('Quick Sort Por Array.png')

plt.figure(figsize=(20, 10))
plt.title('Tempos gastos no algoritmo Selection Sort')
plt.plot(timeSelectionSortArray1, color='red', label='Array 1')
plt.plot(timeSelectionSortArray2, color='blue', label='Array 2')
plt.plot(timeSelectionSortArray3, color='green', label='Array 3')
plt.plot(timeSelectionSortArray4, color='black', label='Array 4')
y = np.max([timeSelectionSortArray1, timeSelectionSortArray2, timeSelectionSortArray3, timeSelectionSortArray4])
plt.text(x=0,y=y, s='Média Array1: '+str(np.around(np.mean(timeSelectionSortArray1), 2)), fontsize=20)
plt.text(x=0.9,y=y, s='Média Array2: '+str(np.around(np.mean(timeSelectionSortArray2), 2)), fontsize=20)
plt.text(x=1.8,y=y, s='Média Array3: '+str(np.around(np.mean(timeSelectionSortArray3), 2)), fontsize=20)
plt.text(x=2.7,y=y, s='Média Array4: '+str(np.around(np.mean(timeSelectionSortArray4), 2)), fontsize=20)
plt.legend(loc=1, prop={'size': 20})
plt.savefig('Selection Sort Por Array.png')

plt.figure(figsize=(20, 10))
plt.title('Tempos totais gastos em cada algoritmo')
plt.plot(timeBubbleSort, color='red', label='Bubble Sort')
plt.plot(timeInsertionSort, color='blue', label='Insertion Sort')
plt.plot(timeMergeSort, color='green', label='Merge Sort')
plt.plot(timeQuickSort, color='orange', label='Quick Sort')
plt.plot(timeSelectionSort, color='black', label='Selection Sort')
y = np.max([timeBubbleSort, timeInsertionSort, timeMergeSort, timeQuickSort, timeSelectionSort])
plt.text(x=0,y=y, s='Média Bubble: '+str(np.around(np.mean(timeBubbleSort), 2)), fontsize=17)
plt.text(x=0.8,y=y, s='Média Insertion: '+str(np.around(np.mean(timeInsertionSort), 2)), fontsize=17)
plt.text(x=1.6,y=y, s='Média Quick: '+str(np.around(np.mean(timeQuickSort), 2)), fontsize=17)
plt.text(x=2.4,y=y, s='Média Merge: '+str(np.around(np.mean(timeMergeSort), 2)), fontsize=17)
plt.text(x=3.2,y=y, s='Média Selection: '+str(np.around(np.mean(timeSelectionSort), 2)), fontsize=17)
plt.legend(loc=4, prop={'size': 20})
plt.savefig('Total dos algoritmos de sort.png')
