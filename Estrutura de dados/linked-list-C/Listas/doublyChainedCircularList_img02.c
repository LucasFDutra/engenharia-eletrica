#include <stdio.h>
#include <stdlib.h>

typedef struct list
{
  int column;
  int line;
  int pixelValue;
  struct list *nextPointer;
  struct list *previousPointer;
} chainList;

int readFile(FILE *file)
{
  int value;
  fscanf(file, "%d", &value);
  return (value);
}

void appendList(chainList *list, chainList *newItem)
{
  chainList *tmp;
  tmp = calloc(1, sizeof(chainList));
  if (list->column != NULL && list->line != NULL)
  {
    tmp->previousPointer = list->previousPointer;
  }
  else
  {
    tmp = list;
    tmp->previousPointer = list;
  }
  tmp->nextPointer = list;
  list->previousPointer->nextPointer = tmp;
  list->previousPointer = tmp;

  tmp->column = newItem->column;
  tmp->line = newItem->line;
  tmp->pixelValue = newItem->pixelValue;
}

void showList(chainList *list)
{
  chainList *tmp;
  tmp = list;

  do
  {
    printf("linha: %d, coluna: %d, valor: %d\n", tmp->line, tmp->column, tmp->pixelValue);
    tmp = tmp->nextPointer;
  } while (tmp != list);
}

writeFile(FILE *file, char *p2, int lines, int columns, int value255, chainList *list, int originalColor, int newColor)
{
  int numberOfItem = 1;
  int extraValue = 0;
  fputs(p2, file);
  fprintf(file, "\n");
  fprintf(file, "%d %d\n", lines, columns);
  fprintf(file, "%d\n", value255);

  if (originalColor == extraValue)
  {
    extraValue = newColor;
  }

  chainList *tmp = list;

  while (numberOfItem <= lines * columns)
  {
    if (((tmp->line - 1) * columns) + tmp->column == numberOfItem)
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
  FILE *wFile = fopen("../Imagens/Copias/img02_chainList.pgm", "w");
  char p2[3];
  int lines, columns, value255, originalColor, newColor;
  int lineOfItems = 1;
  int columnOfItems = 1;
  chainList *imgChainList = calloc(1, sizeof(chainList));
  chainList newItem;

  originalColor = 0;
  newColor = 198;

  fgets(p2, 3, rFile);
  fscanf(rFile, "%d %d\n", &lines, &columns);
  fscanf(rFile, "%d", &value255);

  while (!feof(rFile))
  {
    newItem.pixelValue = readFile(rFile);
    if (newItem.pixelValue != 0 && lineOfItems <= lines)
    {
      newItem.column = columnOfItems;
      newItem.line = lineOfItems;
      newItem.previousPointer = NULL;
      newItem.nextPointer = NULL;

      appendList(imgChainList, &newItem);
    }

    columnOfItems += 1;

    if (columnOfItems > columns)
    {
      columnOfItems = 1;
      lineOfItems += 1;
    }
  }

  // showList(imgChainList);
  writeFile(wFile, p2, lines, columns, value255, imgChainList, originalColor, newColor);

  chainList *tmp;
  tmp = imgChainList;

  while (tmp != tmp->nextPointer)
  {
    tmp = imgChainList->nextPointer;
    imgChainList->nextPointer->previousPointer = imgChainList->previousPointer;
    imgChainList->previousPointer->nextPointer = tmp;
    free(imgChainList);
    imgChainList = tmp;
  }
  free(imgChainList);
}
