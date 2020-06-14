#include <stdio.h>
#include <stdlib.h>

typedef struct list
{
    int value;
    struct list *nextPointer;
} simpleList;

simpleList *appendList(simpleList *list, int newValue)
{

    if (list == NULL)
    {
        list = calloc(1, sizeof(simpleList));
        list->value = newValue;
    }
    else
    {
        simpleList *tmp;
        tmp = list;

        while (tmp->nextPointer != NULL)
        {
            tmp = tmp->nextPointer;
        }
        tmp = tmp->nextPointer = calloc(1, sizeof(simpleList));
        tmp->value = newValue;
    }
    return list;
}

void showList(simpleList *list)
{
    simpleList *tmp;
    tmp = list;

    while (tmp != NULL)
    {
        if (tmp->nextPointer != NULL)
        {
            printf("%d -> ", tmp->value);
        }
        else
        {
            printf("%d \n", tmp->value);
        }
        tmp = tmp->nextPointer;
    }
}

int compareValue(simpleList *list, int value)
{
    simpleList *tmp = list;
    int checker = 0;

    while (tmp != NULL)
    {
        if (tmp->value == value)
        {
            checker = 1;
            break;
        }
        tmp = tmp->nextPointer;
    }
    return checker;
}

int getElementByIndex(simpleList *list, int index)
{
    simpleList *tmp = list;
    int element = -1;
    int count = 0;
    while (tmp != NULL)
    {
        if (index == count)
        {
            element = tmp->value;
            break;
        }
        tmp = tmp->nextPointer;
        count++;
    }
    return element;
}

int getIndexByElement(simpleList *list, int element)
{
    simpleList *tmp = list;
    int index = -1;
    int count = 0;
    while (tmp != NULL)
    {
        if (element == tmp->value)
        {
            index = count;
            break;
        }
        tmp = tmp->nextPointer;
        count++;
    }
    return index;
}

simpleList *reverseList(simpleList *list, simpleList *path)
{
    if (list->nextPointer != NULL)
    {
        path = reverseList(list->nextPointer, path);
    }

    return (appendList(path, list->value));
}

simpleList *search(simpleList *nodes[], int beginning, int destiny)
{
    int count = 0;
    int checker = 0;
    int element, index;
    simpleList *queue = NULL;
    simpleList *origin = NULL;
    simpleList *tmp = nodes[beginning];
    simpleList *path = NULL;
    int newOrigin, a;

    queue = appendList(queue, beginning);
    origin = appendList(origin, -1);

    while (checker == 0)
    {
        while (tmp != NULL)
        {
            if (compareValue(queue, tmp->value) == 0)
            {
                origin = appendList(origin, getElementByIndex(queue, count));
                queue = appendList(queue, tmp->value);
                if (tmp->value == destiny)
                {
                    checker = 1;
                    break;
                }
            }
            tmp = tmp->nextPointer;
        }

        count++;
        newOrigin = getElementByIndex(queue, count);

        if (newOrigin != -1)
        {
            tmp = nodes[newOrigin];
        }
        else
        {
            checker = 1;
        }
    }
    element = destiny;
    while (element != -1)
    {
        index = getIndexByElement(queue, element);
        path = appendList(path, getElementByIndex(queue, index));
        element = getElementByIndex(origin, index);
    }
    return (reverseList(path, NULL));
}

void main()
{
    int exist, numberOfNodes, beginning, destiny;

    printf("digite o numero de nós: ");
    scanf("%d", &numberOfNodes);
    simpleList *nodes[numberOfNodes];

    printf("agora será necessário informar se existe caminho ou não entre dois nós\n");
    printf("digite: \n{1} para sim\n{0} para não\n");

    for (int i = 0; i < numberOfNodes; i++)
    {
        nodes[i] = NULL;
        for (int j = 0; j < numberOfNodes; j++)
        {
            printf("existe caminho de %d para %d: ", i, j);
            scanf("%d", &exist);
            if (exist == 1)
            {
                nodes[i] = appendList(nodes[i], j);
            }
        }
    }

    printf("digite o ponto de partida: ");
    scanf("%d", &beginning);
    printf("digite o ponto de destino: ");
    scanf("%d", &destiny);

    simpleList *path = search(nodes, beginning, destiny);

    if (path->value == -1)
    {
        printf("não existe caminho para ir de %d a %d \n", beginning, destiny);
    }
    else
    {
        printf("uma opção de caminho para ir de %d a %d é: \n", beginning, destiny);
        showList(path);
    }
}
