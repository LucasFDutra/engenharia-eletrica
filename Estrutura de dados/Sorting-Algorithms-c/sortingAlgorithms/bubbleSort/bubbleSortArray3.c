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

void bubbleSort(int *array, int arrayLength)
{
    int i, j;
    int tmpElement = 0;

    for (i = 1; i < arrayLength; i++)
    {
        for (j = 0; j < arrayLength - i; j++)
        {
            if (array[j] > array[j + 1])
            {
                tmpElement = *(array + j);
                *(array + j) = *(array + j + 1);
                *(array + j + 1) = tmpElement;
            }
        }
    }
}

void main()
{
    FILE *arrayFile = fopen("../../arrayFile.txt", "r");

    int i;
    int number;

    int length = 60000;

    int array[length];

    for (i = 0; i < length; i++)
    {
        fscanf(arrayFile, "%d\n", &number);
        array[i] = number;
    }
    bubbleSort(array, length);
    // printf("bubble 3\n");

    // printf("ARRAY DESORDENADO: ");
    // printArray(array, length);
    // bubbleSort(array, length);
    // printf("ARRAY ORDENADO:    ");
    // printArray(array, length);
    // printf("\n");
}