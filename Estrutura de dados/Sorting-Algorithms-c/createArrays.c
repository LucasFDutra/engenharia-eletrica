#include <stdio.h>
#include <stdlib.h>

void main()
{
    FILE *arrayFile = fopen("../arrayFile.txt", "w");

    int i;
    int randomNumber;

    int length = 90000;

    srand(time(NULL));

    for (i = 0; i < length; i++)
    {
        fprintf(arrayFile, "%d\n", rand() % 10000);
    }
}