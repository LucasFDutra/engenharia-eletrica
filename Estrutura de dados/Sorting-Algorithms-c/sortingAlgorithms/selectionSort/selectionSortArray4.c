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

int getIndexOfSmallestElement(int *array, int arrayLength, int startPoint)
{
    int i;
    int position = startPoint;
    int smallValue = *(array + startPoint);
    for (i = startPoint + 1; i < arrayLength; i++)
    {
        if (*(array + i) < smallValue)
        {
            smallValue = *(array + i);
            position = i;
        }
    }
    return position;
}

void selectionSort(int *array, int arrayLength)
{
    int i, position, tmpElement;
    for (i = 0; i < arrayLength; i++)
    {
        position = getIndexOfSmallestElement(array, arrayLength, i);
        tmpElement = *(array + i);
        *(array + i) = *(array + position);
        *(array + position) = tmpElement;
    }
}

void main()
{
    FILE *arrayFile = fopen("../../arrayFile.txt", "r");

    int i;
    int number;

    int length = 90000;

    int array[length];

    for (i = 0; i < length; i++)
    {
        fscanf(arrayFile, "%d\n", &number);
        array[i] = number;
    }
    selectionSort(array, length);

    // printf("ARRAY DESORDENADO: ");
    // printArray(array, length);
    // selectionSort(array, length);
    // printf("ARRAY ORDENADO:    ");
    // printArray(array, length);
    // printf("\n");
}