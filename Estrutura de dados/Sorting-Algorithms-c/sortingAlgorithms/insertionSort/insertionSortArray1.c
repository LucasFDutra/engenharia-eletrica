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

void insertionSort(int *array, int arrayLength)
{
    int i, j;
    int tmpElement = 0;

    for (i = 1; i < arrayLength; i++)
    {
        tmpElement = *(array + i);
        j = i - 1;

        while (tmpElement <= *(array + j) && j >= 0)
        {
            *(array + j + 1) = *(array + j);
            j = j - 1;
        }
        *(array + j + 1) = tmpElement;
    }
}

void main()
{
    FILE *arrayFile = fopen("../../arrayFile.txt", "r");

    int i;
    int number;

    int length = 10000;

    int array[length];

    for (i = 0; i < length; i++)
    {
        fscanf(arrayFile, "%d\n", &number);
        array[i] = number;
    }
    insertionSort(array, length);
    // printf("insertion 1\n");

    // printf("ARRAY DESORDENADO: ");
    // printArray(array, length);
    // insertionSort(array, length);
    // printf("ARRAY ORDENADO:    ");
    // printArray(array, length);
    // printf("\n");
}