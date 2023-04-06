# Cubo-3D
Esse é um trabalho da disciplina Algebra Linear e Teoria da Informação, do curso ciências da computação do insper. A ideia é criar uma projeção 3D de um cubo, de maneira que seja possível controlar as direções em que o cubo gira e sua distância focal. Tudo isso tendo como base o funcionamento de uma camera pinhole e um ponto de projeção.



# Modelo matemático

Para representarmos um cubo 3D em um plano 2D precisaremos passar por diversos passos. Mas antes é necessário entendermos como a lógica usada é aplicada quando se tem apenas duas dimensões. Primeiro, iremos montar nossa matriz inicial:  

$$
inicial = \begin{bmatrix}
X0 \\
Y0 \\
1 \\
\end{bmatrix}
$$

  - Nesse caso o X0 e o Y0 representam o X e o Y iniciais do cubo, enquanto o 1 representa a dsitância focal escolhida.

Agora, para chegarmos nos valores X e Y das projeções, podemos realizar uma semelhanca de traingulo:

$$
  Tg(teta)
$$









Primeiramente, iremos escolher uma das três dimensões para ser o pinhole, ou seja, uma dessas direções vai ser por onde iremos enxergar o cubo, desse modo ela terá um valor fixo de "1", para que não haja transformações nela durante o processo. Dessa forma podemos construir uma matriz com nossas dimensoes, onde o 1 equivale a distância focal escolhida:

$$
inicial = \begin{bmatrix}
X0 \\
Y0 \\
1 \\
\end{bmatrix}
$$
