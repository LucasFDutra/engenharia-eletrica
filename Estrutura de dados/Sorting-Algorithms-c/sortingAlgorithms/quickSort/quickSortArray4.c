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

int partition(int *array, int beginning, int end)
{
    int left, right, tmpElement, loc, flag;
    left = beginning;
    loc = left;
    right = end;
    flag = 0;

    while (flag != 1)
    {
        while ((*(array + loc) <= *(array + right)) && (loc != right))
        {
            right--;
        }
        if (loc == right)
        {
            flag = 1;
        }
        else
        {
            tmpElement = *(array + loc);
            *(array + loc) = *(array + right);
            *(array + right) = tmpElement;
            loc = right;
        }
        if (flag != 1)
        {
            while ((*(array + loc) >= *(array + left)) && (loc != left))
            {
                left++;
            }
            if (loc == left)
            {
                flag = 1;
            }
            else
            {
                tmpElement = *(array + loc);
                *(array + loc) = *(array + left);
                *(array + left) = tmpElement;
                loc = left;
            }
        }
    }
    return loc;
}

void quickSort(int *array, int beginning, int end)
{
    int loc;
    if (beginning < end)
    {
        loc = partition(array, beginning, end);
        quickSort(array, beginning, loc - 1);
        quickSort(array, loc + 1, end);
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
    quickSort(array, 0, length - 1);

    // printf("ARRAY DESORDENADO: ");
    // printArray(array, length);
    // quickSort(array, 0, length - 1);
    // printf("ARRAY ORDENADO:    ");
    // printArray(array, length);
    // printf("\n");
}