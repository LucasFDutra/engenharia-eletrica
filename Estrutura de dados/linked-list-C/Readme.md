O presente repositório advem de um trabalho da matéria de Algoritmos e estruturas de dados, e visa efetuar o comparativo entre dois métodos de adicionar um item ao fim de uma lista ligada. O comparativo será efetuado monitorando o tempo de execução de cada código.

A base de dados utilizada serão duas imagens, que se encontram neste repositório, as imagens [img02.pgm](https://raw.githubusercontent.com/LucasFDutra/linked-list-C/master/Imagens/Originais/img02.pgm) e [img03.pgm](https://raw.githubusercontent.com/LucasFDutra/linked-list-C/master/Imagens/Originais/img03.pgm).

A descrição detalhada do trabalho pode ser vista [aqui](https://github.com/LucasFDutra/linked-list-C/blob/master/Lab.%20005.pdf).

O primeiro algoritmo a ser executado será uma lista ligada simples. E como se sabe, para inserir um novo item no final da lista é necessário percorrer ela inteira, até encontrar o final da lista, e só então podemos adicionar um item. Logo, o número de operações que devemos efetuar é sempre dependente da quantidade de itens presentes na lista. Ou seja, temos um algoritmo com oredem N, sendo que N varia com o tamanho da lista (On).

O segundo algoritmo, que ficou a encoargo dos alunos escolherem, é uma lista ligada circular duplamente encadeada, que efetuaria o mesmo número de operações independente da quantidade de itens que a lista compreendesse, ou seja, ela possui ordem constante:

- Ligar o ponteiro anterior do novo nó ao fim da lista;
- Ligar o ponteiro proximo do novo nó ao inicio da lista;
- Ligar o ponteiro anterior da cabeça da lista ao novo nó;
- Ligar o ponteiro proximo do final da lista ao novo nó;

Após os códigos estarem prontos eles contam com as seguintes funções:

```C
int readFile(FILE *file)
void appendList(simpleList *list, simpleList *newItem)
void showList(simpleList *list)
void writeFile(FILE *file, char *p2, int lines, int columns, int value255, simpleList *list, int originalColor, int newColor)
```

Sendo que dentro da função `writeFile` está a substituição de um dado valor da lista por outro.

Como tudo será automatizado, e não queremos fator humano atrapalhando o teste, irei definir o pixel a ser substituido será sempre 0 por 198.

As implementações podem ser encontradas na pasta `Listas` nesse link [aqui](https://github.com/LucasFDutra/linked-list-C/tree/master/Listas)

> Os códigos provavelmente rodarão somente em sistemas linux, devido a necessidade de transição entre diretórios, o que é feito de forma diferente no windows e linux.

O comparativo será executado utilizando o python, o código python irá executar comandos diretamente no teminal do linux, e assim ele compilará os arquivos .c e irá mandar cada um rodar 100 vezes, o tempo de execução de cada código será salvo e mostrado em um gráfico com a ajuda do matplotlib.

O código em python pode ser encontrado [aqui](https://github.com/LucasFDutra/linked-list-C/tree/master/Grafics)

Olhando no repositório pode ver 4 arquivos .c, dois para a imagem img02 e dois para a imagem img03, sendo que cada imagem conta com dois algoritmos, o de lista ligada simples e o de lista circular duplamente encadeada.

Os gráficos comparativos podem ser vistos abaixo:

![](https://github.com/LucasFDutra/linked-list-C/blob/master/Graphics/grafico%20img002.png?raw=true)

![](https://github.com/LucasFDutra/linked-list-C/blob/master/Graphics/grafico%20img003.png?raw=true)

Caso você seja usuário linux, pode executar todos os testes apenas clonando o repositório em sua máquina e executando o arquivo `runTest.sh` com o comando `./runTest.sh` em seu terminal ou dando duplo click nele e permitindo a execução.
