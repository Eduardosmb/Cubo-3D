import pygame 
import numpy as np

# Distância focal da câmera
distancia_focal = 150

# Criação da matriz inicial contendo as coordenadas dos vértices do cubo
matriz_incial = np.array([[-100,100,100,1],[-100,100,-100,1],[100,100,100,1],[100,100,-100,1],[-100,-100,100,1],[-100,-100,-100,1],[100,-100,100,1],[100,-100,-100,1]]).T

# Criação da matriz auxiliar responsável pela projeção do cubo na tela
matriz_aux = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,distancia_focal],[0,0,-1/distancia_focal,0]])

# Criação da matriz de rotação inicial do cubo
Matriz_R = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

# Criação da matriz de rotação final do cubo
Matriz_R_final = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

# Inicialização do Pygame
pygame.init()

# Definição da cor utilizada para desenhar o cubo
cor = (255,0,0)

# Definição da largura e altura da janela de exibição
width, height = 600, 800

# Inicialização do relógio utilizado para controlar a taxa de quadros por segundo
clock = pygame.time.Clock()

# Definição da taxa de quadros por segundo
FPS = 60

# Criação da janela de exibição
screen = pygame.display.set_mode((height, width))

# Variável que controla se o programa está em execução ou não
rodando = True

cubo_em_rotacao = True

# Ângulo de rotação em torno do eixo x
angulo_x = 0.0 
# Velocidade angular constante
velocidade_angular_x = 0.001 

# Loop principal
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Se o botão de scroll para baixo foi pressionado, a variável "distancia_focal" é reduzida em 10 e a matriz_aux é recalculada com os novos valores.
            if event.button == 5: 
                if distancia_focal > 10:
                    distancia_focal -= 10
                    matriz_aux = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,distancia_focal],[0,0,-1/distancia_focal,0]])

            # Se o botão de scroll para cima foi pressionado, a variável "distancia_focal" é aumentada em 10 e a matriz_aux é recalculada com os novos valores.
            elif event.button == 4:
                distancia_focal += 10
                matriz_aux = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,distancia_focal],[0,0,-1/distancia_focal,0]])



        #se clicar a tecka m, muda a cor do cubo para uma cor aleatoria
        if pygame.key.get_pressed()[pygame.K_m]:
            cor = (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))

        
        #se clicar a tecka w rotaciona o eixo x
        if pygame.key.get_pressed()[pygame.K_w]:
            angulo_x = velocidade_angular_x
            Matriz_R = np.array([[1,0,0,0],[0,np.cos(angulo_x),-np.sin(angulo_x),0],[0,np.sin(angulo_x),np.cos(angulo_x),0],[0,0,0,1]])

        #se clicar a tecka s rotaciona o eixo y
        if pygame.key.get_pressed()[pygame.K_s]:
            angulo_x = - velocidade_angular_x
            Matriz_R = np.array([[1,0,0,0],[0,np.cos(angulo_x),-np.sin(angulo_x),0],[0,np.sin(angulo_x),np.cos(angulo_x),0],[0,0,0,1]])
        
        #se clicar a tecka a rotaciona o eixo z
        if pygame.key.get_pressed()[pygame.K_q]:
            angulo_x = velocidade_angular_x
            Matriz_R = np.array([[np.cos(angulo_x),-np.sin(angulo_x),0,0],[np.sin(angulo_x),np.cos(angulo_x),0,0],[0,0,1,0],[0,0,0,1]])
        
        #se clicar a tecka d rotaciona o eixo z
        if pygame.key.get_pressed()[pygame.K_e]:
            angulo_x = - velocidade_angular_x
            Matriz_R = np.array([[np.cos(angulo_x),-np.sin(angulo_x),0,0],[np.sin(angulo_x),np.cos(angulo_x),0,0],[0,0,1,0],[0,0,0,1]])

        #se clicar a tecka q rotaciona o eixo z
        if pygame.key.get_pressed()[pygame.K_a]:
            angulo_x = velocidade_angular_x
            Matriz_R = np.array([[np.cos(angulo_x),0,np.sin(angulo_x),0],[0,1,0,0],[-np.sin(angulo_x),0,np.cos(angulo_x),0],[0,0,0,1]])
        
        #se clicar a tecka e rotaciona o eixo z
        if pygame.key.get_pressed()[pygame.K_d]:
            angulo_x = - velocidade_angular_x
            Matriz_R = np.array([[np.cos(angulo_x),0,np.sin(angulo_x),0],[0,1,0,0],[-np.sin(angulo_x),0,np.cos(angulo_x),0],[0,0,0,1]])

        # Verifica se o cubo está em rotação antes de definir a velocidade angular
        if pygame.key.get_pressed()[pygame.K_i]:
            cubo_em_rotacao = False
        elif pygame.key.get_pressed()[pygame.K_o]:
            cubo_em_rotacao = True


        # Define a velocidade angular de acordo com o estado atual da rotação do cubo
        if cubo_em_rotacao:
            velocidade_angular_x = 0.001
        else:
            velocidade_angular_x = 0.0
    

    # Translada o cubo para o centro da tela
    matriz_T = np.array([[1,0,0,400],[0,1,0,300],[0,0,1,0],[0,0,0,1]])

    # Matriz de rotacao em torno do eixo y
    Matriz_R_Y = np.array([[np.cos(angulo_x),0,np.sin(angulo_x),0],[0,1,0,0],[-np.sin(angulo_x),0,np.cos(angulo_x),0],[0,0,0,1]])

    # Matriz de rotacao em torno do eixo z
    Matriz_R_Z = np.array([[np.cos(angulo_x),-np.sin(angulo_x),0,0],[np.sin(angulo_x),np.cos(angulo_x),0,0],[0,0,1,0],[0,0,0,1]])


    # Matriz de translação ao longo do eixo z
    Matriz_T_Z = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,200],[0,0,0,1]])

    #Multiplicação de matrizes para obter a matriz de rotação final  que será usada posteriormente para rotacionar o cubo nos eixos x, y e z.
    Matriz_R_final = Matriz_R @ Matriz_R_final

    # Criado a matriz resultante feita através da translação para o centro da tela, a rotação nos eixos y e z, a translação ao longo do eixo z e a rotação final nos eixos x, y e z.
    matriz_resultante = matriz_T @ matriz_aux @ Matriz_T_Z @ Matriz_R_final @ matriz_incial

    # Desenhar a tela

    screen.fill((0,0,0))

    #Definindo e desenhando as linhas do cubo
    pygame.draw.line(screen,(cor),(matriz_resultante[0,0]/matriz_resultante[3,0], matriz_resultante[1,0]/matriz_resultante[3,0]),(matriz_resultante[0,2]/matriz_resultante[3,2], matriz_resultante[1,2]/matriz_resultante[3,2]),width=5)
    pygame.draw.line(screen,(cor),(matriz_resultante[0,0]/matriz_resultante[3,0], matriz_resultante[1,0]/matriz_resultante[3,0]),(matriz_resultante[0,1]/matriz_resultante[3,1], matriz_resultante[1,1]/matriz_resultante[3,1]),width=5)
    pygame.draw.line(screen,(cor),(matriz_resultante[0,2]/matriz_resultante[3,2], matriz_resultante[1,2]/matriz_resultante[3,2]),(matriz_resultante[0,3]/matriz_resultante[3,3], matriz_resultante[1,3]/matriz_resultante[3,3]),width=5)
    pygame.draw.line(screen,(cor),(matriz_resultante[0,1]/matriz_resultante[3,1], matriz_resultante[1,1]/matriz_resultante[3,1]),(matriz_resultante[0,3]/matriz_resultante[3,3], matriz_resultante[1,3]/matriz_resultante[3,3]),width=5)
    pygame.draw.line(screen,(cor),(matriz_resultante[0,0]/matriz_resultante[3,0], matriz_resultante[1,0]/matriz_resultante[3,0]),(matriz_resultante[0,4]/matriz_resultante[3,4], matriz_resultante[1,4]/matriz_resultante[3,4]),width=5)
    pygame.draw.line(screen,(cor),(matriz_resultante[0,1]/matriz_resultante[3,1], matriz_resultante[1,1]/matriz_resultante[3,1]),(matriz_resultante[0,5]/matriz_resultante[3,5], matriz_resultante[1,5]/matriz_resultante[3,5]),width=5)
    pygame.draw.line(screen,(cor),(matriz_resultante[0,2]/matriz_resultante[3,2], matriz_resultante[1,2]/matriz_resultante[3,2]),(matriz_resultante[0,6]/matriz_resultante[3,6], matriz_resultante[1,6]/matriz_resultante[3,6]),width=5)
    pygame.draw.line(screen,(cor),(matriz_resultante[0,3]/matriz_resultante[3,3], matriz_resultante[1,3]/matriz_resultante[3,3]),(matriz_resultante[0,7]/matriz_resultante[3,7], matriz_resultante[1,7]/matriz_resultante[3,7]),width=5)
    pygame.draw.line(screen,(cor),(matriz_resultante[0,4]/matriz_resultante[3,4], matriz_resultante[1,4]/matriz_resultante[3,4]),(matriz_resultante[0,6]/matriz_resultante[3,6], matriz_resultante[1,6]/matriz_resultante[3,6]),width=5)
    pygame.draw.line(screen,(cor),(matriz_resultante[0,4]/matriz_resultante[3,4], matriz_resultante[1,4]/matriz_resultante[3,4]),(matriz_resultante[0,5]/matriz_resultante[3,5], matriz_resultante[1,5]/matriz_resultante[3,5]),width=5)
    pygame.draw.line(screen,(cor),(matriz_resultante[0,6]/matriz_resultante[3,6], matriz_resultante[1,6]/matriz_resultante[3,6]),(matriz_resultante[0,7]/matriz_resultante[3,7], matriz_resultante[1,7]/matriz_resultante[3,7]),width=5)
    pygame.draw.line(screen,(cor),(matriz_resultante[0,5]/matriz_resultante[3,5], matriz_resultante[1,5]/matriz_resultante[3,5]),(matriz_resultante[0,7]/matriz_resultante[3,7], matriz_resultante[1,7]/matriz_resultante[3,7]),width=5)


    # Atualizando a tela
    pygame.display.flip()

    

pygame.quit()