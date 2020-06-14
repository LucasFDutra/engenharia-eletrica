#include <stdio.h>
#include <stdlib.h>

typedef struct list
{
  int line;
  int column;
  int pixelValue;
  struct list *nextPointer;
} simpleList;

int readFile(FILE *file)
{
  int value;
  fscanf(file, "%d", &value);
  return (value);
}

void appendList(simpleList *list, simpleList *newItem)
{
  simpleList *tmp;
  tmp = list;

  if (list->column != NULL && list->line != NULL)
  {
    while (tmp->nextPointer != NULL)
    {
      tmp = tmp->nextPointer;
    }

    tmp = tmp->nextPointer = calloc(1, sizeof(simpleList));
  }
  tmp->column = newItem->column;
  tmp->line = newItem->line;
  tmp->pixelValue = newItem->pixelValue;
  tmp->nextPointer = NULL;
}

void showList(simpleList *list)
{
  simpleList *tmp;
  tmp = list;

  do
  {
    printf("line: %d, column: %d, pixelValue: %d \n", tmp->line, tmp->column, tmp->pixelValue);
    tmp = tmp->nextPointer;
  } while (tmp->nextPointer != NULL);
  printf("line: %d, column: %d, pixelValue: %d \n", tmp->line, tmp->column, tmp->pixelValue);
}

void writeFile(FILE *file, char *p2, int lines, int columns, int value255, simpleList *list, int originalColor, int newColor)
{
  simpleList *tmp;
  tmp = list;
  int numberOfItem = 1;
  int extraValue = 0;

  if (originalColor == extraValue)
  {
    extraValue = newColor;
  }

  fputs(p2, file);
  fprintf(file, "\n");
  fprintf(file, "%d %d\n", lines, columns);
  fprintf(file, "%d\n", value255);

  while (numberOfItem <= lines * columns)
  {
    if (tmp != NULL && (((tmp->line - 1) * columns) + tmp->column) == numberOfItem)
    {
      if (originalColor == tmp->pixelValue)
      {
        tmp->pixelValue = newColor;
      }
      fprintf(file, "%d\n", tmp->pixelValue);
      tmp = tmp->nextPointer;
    }
    else
    {
      fprintf(file, "%d\n", extraValue);
    }
    numberOfItem += 1;
  }
}

void main()
{
  FILE *rFile = fopen("../Imagens/Originais/img02.pgm", "r");
  FILE *wFile = fopen("../Imagens/Copias/img02_simpleList.pgm", "w");
  char p2[3];
  int lines, columns, value255, originalColor, newColor;
  int columnOfItem = 1;
  int lineOfItem = 1;

  originalColor = 0;
  newColor = 198;

  simpleList *imgSimpleList;
  simpleList newItem;

  imgSimpleList = calloc(1, sizeof(simpleList));

  fgets(p2, 3, rFile);
  fscanf(rFile, "%d %d\n", &lines, &columns);
  fscanf(rFile, "%d", &value255);

  while (!feof(rFile))
  {
    newItem.pixelValue = readFile(rFile);
    if (newItem.pixelValue != 0 && lineOfItem <= lines)
    {
      newItem.column = columnOfItem;
      newItem.line = lineOfItem;
      newItem.nextPointer = NULL;
      appendList(imgSimpleList, &newItem);
    }
    columnOfItem += 1;
    if (columnOfItem > columns)
    {
      columnOfItem = 1;
      lineOfItem += 1;
    }
  }
  // showList(imgSimpleList);

  writeFile(wFile, p2, lines, columns, value255, imgSimpleList, originalColor, newColor);

  simpleList *tmp;
  tmp = imgSimpleList;
  while (imgSimpleList != NULL)
  {
    tmp = imgSimpleList->nextPointer;
    free(imgSimpleList);
    imgSimpleList = tmp;
  }
}
