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
  Tg(teta) = X0/Y0 = Xp/Yp
$$

Para obtermos o valor da projeção de Xp, podemos isolar o Xp:

$$
  Xp = X0Yp/Y0
$$

Apartir disso criamos uma nova variavel Wp = Yp/Y0, que pode ser substituida na equacção acima, resultando em:

$$
  Xp = X0Wp
$$


Dessa forma já temos todos os dados necessários para descubrirmos os valores das coordenadas da nossa projeção. Portanto podemos montar a equação:

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 0 & -d\\
0 & -1/d & 0 \\
\end{bmatrix}
\hspace{0.5in}
\begin{bmatrix}
X0 \\
Y0 \\
1 \\
\end{bmatrix}
\hspace{0.5in}
= \begin{bmatrix}
XpWp \\
Yp \\
Wp\\
\end{bmatrix}
$$

Agora que já sabemos fazer a transformação em 2D consguimos fazer em 3D. A lógica continua a mesma, porém agora iremos adicionar um novo ponto representando a dimensão Z.  Primeiramente iremos escolher uma das três dimensões para ser o pinhole, ou seja, uma dessas direções vai ser por onde iremos enxergar o cubo, desse modo ela será uma variável estática(sempre terá o mesmo valor). Dessa forma podemos construir as matrizes já apresentadas aneteriormente:

$$
\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & -d\\
0 & 0 & -1/d & 0 \\
\end{bmatrix}
\hspace{0.5in}
\begin{bmatrix}
X0 \\
Y0 \\
z0 \\
1 \\
\end{bmatrix}
\hspace{0.5in}
= \begin{bmatrix}
XpWp \\
YpWp \\
Z0 \\
Wp\\
\end{bmatrix}
$$

Assim, conseguimos realizar uma projeção de um cubo 3D em um plano 2D através do metodo pinhole. Agora, ainda precisamos realizar transformações de rotação com o cubo. Para isso, temos que fazer uma sequencia multiplicação de matrizes.

  1. Criamos uma matriz para transladamos o cubo para o centro da tela:

  
$$
R_x = \begin{bmatrix}
1 & 0 & 0 & \Delta x \\
0 & 1 & 0 & \Delta y\\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$


  2. Multiplicamos a matriz de cima com a matriz pinhole:


  3. Multiplicamos a matriz de cima com uma matriz de translação do eixo Z, para podermos visualizar o cubo:


  4. multiplicamos o resultado por uma das matrizes de rotação:


$$
R_x = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) & 0 \\
0 & \sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_y = \begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
-\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_z = \begin{bmatrix}
\cos(\theta) & - \sin(\theta) & 0 & 0 \\
\sin(\theta) & \cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$




  5. Por fim multiplicamos o resultado pela matriz inicial com as coordenadas do cubo:



