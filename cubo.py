import pygame 
import numpy as np

distancia_focal = 150
matriz_incial = np.array([[-100,100,100,1],[-100,100,-100,1],[100,100,100,1],[100,100,-100,1],[-100,-100,100,1],[-100,-100,-100,1],[100,-100,100,1],[100,-100,-100,1]]).T

matriz_aux = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,distancia_focal],[0,0,-1/distancia_focal,0]])

pygame.init()

cor = (255,0,0)
width, height = 600, 800
clock = pygame.time.Clock()

FPS = 60

screen = pygame.display.set_mode((height, width))
rodando = True

angulo_x = 0.0  # ângulo de rotação em torno do eixo x
velocidade_angular_x = 0.0015  # velocidade angular constante

while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False


    #se clicar a tecka w rotaciona o eixo x
    if pygame.key.get_pressed()[pygame.K_m]:
        cor = (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))

    #se clicar a tecka w rotaciona o eixo x
    if pygame.key.get_pressed()[pygame.K_w]:
        angulo_x += velocidade_angular_x
        Matriz_R = np.array([[1,0,0,0],[0,np.cos(angulo_x),-np.sin(angulo_x),0],[0,np.sin(angulo_x),np.cos(angulo_x),0],[0,0,0,1]])


    # Transladar o cubo para o centro da tela
    matriz_T = np.array([[1,0,0,300],[0,1,0,400],[0,0,1,0],[0,0,0,1]])

    # Matriz de rotação em torno do eixo x
    angulo_x += velocidade_angular_x
    Matriz_R_X = np.array([[1,0,0,0],[0,np.cos(angulo_x),-np.sin(angulo_x),0],[0,np.sin(angulo_x),np.cos(angulo_x),0],[0,0,0,1]])

    # Matriz de rotacao em torno do eixo y
    Matriz_R_Y = np.array([[np.cos(angulo_x),0,np.sin(angulo_x),0],[0,1,0,0],[-np.sin(angulo_x),0,np.cos(angulo_x),0],[0,0,0,1]])

    # Matriz de rotacao em torno do eixo z
    Matriz_R_Z = np.array([[np.cos(angulo_x),-np.sin(angulo_x),0,0],[np.sin(angulo_x),np.cos(angulo_x),0,0],[0,0,1,0],[0,0,0,1]])

    Matriz_T_Z = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,200],[0,0,0,1]])

    matriz_resultante = matriz_T @ matriz_aux @ Matriz_T_Z @ Matriz_R_X @ Matriz_R_Y @ Matriz_R_Z @ matriz_incial

    # Desenhar a tela

    screen.fill((0,0,0))


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




    pygame.display.flip()

    

pygame.quit()

