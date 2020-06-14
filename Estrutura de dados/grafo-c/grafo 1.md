```C
    int exist, numberOfNodes, beginning, destiny;

    numberOfNodes = 9;
    simpleList *nodes[numberOfNodes];

    int i = 0;
    nodes[i] = NULL;
    nodes[i] = appendList(nodes[i], 1);
    nodes[i] = appendList(nodes[i], 2);
    nodes[i] = appendList(nodes[i], 3);

    i = 1;
    nodes[i] = NULL;
    nodes[i] = appendList(nodes[i], 4);

    i = 2;
    nodes[i] = NULL;
    nodes[i] = appendList(nodes[i], 1);
    nodes[i] = appendList(nodes[i], 6);

    i = 3;
    nodes[i] = NULL;
    nodes[i] = appendList(nodes[i], 2);
    nodes[i] = appendList(nodes[i], 6);

    i = 4;
    nodes[i] = NULL;
    nodes[i] = appendList(nodes[i], 2);
    nodes[i] = appendList(nodes[i], 5);

    i = 5;
    nodes[i] = NULL;
    nodes[i] = appendList(nodes[i], 2);
    nodes[i] = appendList(nodes[i], 7);

    i = 6;
    nodes[i] = NULL;
    nodes[i] = appendList(nodes[i], 5);
    nodes[i] = appendList(nodes[i], 7);
    nodes[i] = appendList(nodes[i], 8);

    i = 7;
    nodes[i] = NULL;
    nodes[i] = appendList(nodes[i], 4);
    nodes[i] = appendList(nodes[i], 8);

    i = 8;
    nodes[i] = NULL;
    nodes[i] = appendList(nodes[i], 5);

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
```
