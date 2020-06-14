#include <stdio.h>
#include <stdlib.h>

void printArray(int *array, int arrayLength)
{
    for (int i = 0; i < arrayLength; i++)
    {
        printf("%d ", *(array + i));
    }
    printf("\n");
}

void merge(int *array, int arrayLength, int beginning, int midlle, int end)
{
    int i = beginning;
    int j = midlle + 1;
    int index = beginning;
    int tmpArray[arrayLength];

    while (i <= midlle && j <= end)
    {
        if (*(array + i) < *(array + j))
        {
            tmpArray[index] = *(array + i);
            i++;
        }
        else
        {
            tmpArray[index] = *(array + j);
            j++;
        }
        index++;
    }
    if (i > midlle)
    {
        while (j <= end)
        {
            tmpArray[index] = *(array + j);
            j++;
            index++;
        }
    }
    else
    {
        while (i <= midlle)
        {
            tmpArray[index] = *(array + i);
            i++;
            index++;
        }
    }
    for (i = beginning; i < index; i++)
    {
        *(array + i) = tmpArray[i];
    }
}

void mergeSort(int *array, int arrayLength, int beginning, int end)
{
    int middle;
    if (beginning < end)
    {
        middle = (beginning + end) / 2;
        mergeSort(array, arrayLength, beginning, middle);
        mergeSort(array, arrayLength, middle + 1, end);

        merge(array, arrayLength, beginning, middle, end);
    }
}

void main()
{
    FILE *arrayFile = fopen("../../arrayFile.txt", "r");

    int i;
    int number;

    int length = 30000;

    int array[length];

    for (i = 0; i < length; i++)
    {
        fscanf(arrayFile, "%d\n", &number);
        array[i] = number;
    }
    mergeSort(array, length, 0, length - 1);

    // printf("ARRAY DESORDENADO: ");
    // printArray(array, length);
    // mergeSort(array, length, 0, length - 1);
    // printf("ARRAY ORDENADO:    ");
    // printArray(array, length);
    // printf("\n");
}