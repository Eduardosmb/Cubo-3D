import pygame 
import numpy as np

distancia_focal = 150
matriz_incial = np.array([[-100,100,100,1],[-100,100,-100,1],[100,100,100,1],[100,100,-100,1],[-100,-100,100,1],[-100,-100,-100,1],[100,-100,100,1],[100,-100,-100,1]]).T

matriz_aux = [[1,0,0,0],[0,1,0,0],[0,0,0,distancia_focal],[0,0,-1/distancia_focal,0]]

# matriz_resultante = np.dot(matriz_aux,matriz_incial)

pygame.init()

width, height = 600, 800
clock = pygame.time.Clock()

FPS = 60

screen = pygame.display.set_mode((height, width))
rodando = True

while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Transladar o cubo para o centra da tela
    matriz_T = [[1,0,0,300],[0,1,0,400],[0,0,1,0],[0,0,0,1]]
    # matriz_resultante = np.dot(matriz_T,matriz_resultante)

    Matriz_T_Z = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,200],[0,0,0,1]])

    # Matriz_R_X = np.array([[1,0,0,0],[0,np.cos(np.pi/4),-np.sin(np.pi/4),0],[0,np.sin(np.pi/4),np.cos(np.pi/4),0],[0,0,0,1]])
    # Matriz_R_Y = np.array([[np.cos(np.pi/4),0,np.sin(np.pi/4),0],[0,1,0,0],[-np.sin(np.pi/4),0,np.cos(np.pi/4),0],[0,0,0,1]])
    # Matriz_R_Z = np.array([[np.cos(np.pi/4),-np.sin(np.pi/4),0,0],[np.sin(np.pi/4),np.cos(np.pi/4),0,0],[0,0,1,0],[0,0,0,1]])

    Matriz_resultante = np.dot(matriz_T,matriz_incial)
    matriz_resultante = np.dot(matriz_resultante,Matriz_T_Z)

    # Desenhar a tela
    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,0]/matriz_resultante[3,0], matriz_resultante[1,0]/matriz_resultante[3,0]),(matriz_resultante[0,2]/matriz_resultante[3,2], matriz_resultante[1,2]/matriz_resultante[3,2]),width=5)
    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,0]/matriz_resultante[3,0], matriz_resultante[1,0]/matriz_resultante[3,0]),(matriz_resultante[0,4]/matriz_resultante[3,4], matriz_resultante[1,4]/matriz_resultante[3,4]),width=5)
    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,1]/matriz_resultante[3,1], matriz_resultante[1,1]/matriz_resultante[3,1]),(matriz_resultante[0,3]/matriz_resultante[3,3], matriz_resultante[1,3]/matriz_resultante[3,3]),width=5)
    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,2]/matriz_resultante[3,2], matriz_resultante[1,2]/matriz_resultante[3,2]),(matriz_resultante[0,3]/matriz_resultante[3,3], matriz_resultante[1,3]/matriz_resultante[3,3]),width=5)

    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,1]/matriz_resultante[3,1], matriz_resultante[1,1]/matriz_resultante[3,1]),(matriz_resultante[0,5]/matriz_resultante[3,5], matriz_resultante[1,5]/matriz_resultante[3,5]), width=5)
    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,2]/matriz_resultante[3,2], matriz_resultante[1,2]/matriz_resultante[3,2]),(matriz_resultante[0,6]/matriz_resultante[3,6], matriz_resultante[1,6]/matriz_resultante[3,6]), width=5)
    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,3]/matriz_resultante[3,3], matriz_resultante[1,3]/matriz_resultante[3,3]),(matriz_resultante[0,7]/matriz_resultante[3,7], matriz_resultante[1,7]/matriz_resultante[3,7]), width=5)
    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,4]/matriz_resultante[3,4], matriz_resultante[1,4]/matriz_resultante[3,4]),(matriz_resultante[0,5]/matriz_resultante[3,5], matriz_resultante[1,5]/matriz_resultante[3,5]), width=5)

    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,5]/matriz_resultante[3,5], matriz_resultante[1,5]/matriz_resultante[3,5]),(matriz_resultante[0,7]/matriz_resultante[3,7], matriz_resultante[1,7]/matriz_resultante[3,7]), width=5)
    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,6]/matriz_resultante[3,6], matriz_resultante[1,6]/matriz_resultante[3,6]),(matriz_resultante[0,7]/matriz_resultante[3,7], matriz_resultante[1,7]/matriz_resultante[3,7]), width=5)
    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,4]/matriz_resultante[3,4], matriz_resultante[1,4]/matriz_resultante[3,4]),(matriz_resultante[0,6]/matriz_resultante[3,6], matriz_resultante[1,6]/matriz_resultante[3,6]), width=5)
    pygame.draw.line(screen,(255,0,0),(matriz_resultante[0,0]/matriz_resultante[3,0], matriz_resultante[1,0]/matriz_resultante[3,0]),(matriz_resultante[0,1]/matriz_resultante[3,1], matriz_resultante[1,1]/matriz_resultante[3,1]),width=5)



    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()