<h1 align="center"> IA - Aprendizado não Supervisionado</h1>

<h1>Introdução</h1>

<h4>Quantização de cores é o processo de redução do número de cores em uma imagem. Uma razão para fazer isso é reduzir a memória. Às vezes, alguns dispositivos podem ter limitações que podem produzir apenas um número limitado de cores. Também nesses casos é realizada a quantização de cores. Aqui usamos agrupamento k-means (K-Média) para quantização de cores.</h4>

<h4>A aplicação desenvolvida em Python, a qual utiliza a biblioteca abaixo, tem como objetivo receber algumas imagens como parâmetro de entrada e aplicar o algoritmo k-médias em cada uma variando o valor de k. Após isso, é gerado alguns dados de saída sendo então, a imagem processada, as informações como dimensões, quantidades de cores e tamanho tanto da imagem original quanto a que foi gerado pela aplicação.
</h4>

## Biblioteca utilizada.

- https://docs.opencv.org/4.x/
- https://docs.opencv.org/4.x/d5/d38/group__core__cluster.html

## Comando para instalar a biblioteca.

```
$ pip install opencv-python
```

- Página de instalação da lib: https://pypi.org/project/opencv-python/

## Tamanho definidos para a variável (K).

- 6, 15, 50, 100, 250, 500, 1000
