O controle em questão é de um conversor boost quadrático.

Aqui você irá encontrar o um PDF com o layout da placa, os caculos do projeto, incluindo o controlador PID, e tudo simulado no PSIM.

Para o controle, deixei 2 opções de como fazer, mas que no fundo são a mesma coisa. Apenas a segunda opção possui diferenças relevantes:

- Opção 1: é uma versão mais simples.

- Opção 2: é uma versão resumida da opção 1, em que os códigos agora são bibliotecas, sendo assim o controle PID pode ser feito em apenas uma linha.

> OBS 1.: Como o raspberry não possui conversor AD integrado, utilizou-se o Arduino para esta função.
Para isso bastou apenas ligar o arduino no raspberry via cabo USB e nada mais (o próprio raspberry funciona como fonte de alimentação do arduino). O código que deve ser gravado no arduino também se encontra junto aos demais arquivos.
  Lembre que deve-se olhar qual porta o arduino se encontra, visto que ela não é fixa, assim precisamos alterar no código python de malha fechada (dica.. instale o arduino para ARM e olhe por lá qual porta ele está utilizando).

> OBS 2.: Como o controle que eu precisava a frequência do PWM era de 10KHz e o raspberry vem configurado para no máximo 8KHz, tive que criar uma outra biblioteca para PWM me baseando na biblioteca "pigpio" para assim mudar a taxa de amostragem e garantir maiores frequências.

> OBS 3.: Fique atento aos pinos do raspberry, pois a biblioteca de PWM não segue a numeração que está DENTRO da bolinha, ele segue o que nome que está do lado, ou seja: GPIO2 é o pino 2, GPIO3 é o pino 3...

<figure>
  <p><img src='https://1.bp.blogspot.com/-HBBmS0QSLP4/VilmEGuNjAI/AAAAAAAAEOc/rR1zW34Bz50/s1600/raspberrypi_a_plus_GPIO.png'>
  <figcaption>Fonte: https://www.arduinoecia.com.br/2015/10/apache-web-server-raspberry-pi-a-plus.html</figcaption>
</figure>
