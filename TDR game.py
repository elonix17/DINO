import pygame
import sys
#import numpy as np
import random
import time

ancho_ventana = 1024
alto_ventana = 500
puntuacion = 0

pygame.init()
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))


class cubo:
    
    def __init__(self):
        self.x, self.y = 150, 400
        self.w, self.h = 70, 80
    
        self.color = (255,0,0)
        self.saltando = False
        self.y_salto = 0
        self.agachado = False
        
    def color_nuevo(self, color):
        self.color = color
        
    def ancho_nuevo(self, ancho):
        self.w = ancho
    
    def display(self):
        pygame.draw.rect(ventana, self.color, pygame.Rect(self.x, self.y, self.w, self.h))

    def f(self):
        return((-4*self.y_salto*(self.y_salto-1))*250)
    
    def actualizar(self):
        if (self.saltando):
            self.y = 400 - self.f()
            self.y_salto = self.y_salto + 0.0013
            if (self.y_salto > 1):
                self.saltando = False
                self.y_salto = 0
                self.y = 400    
        elif (self.agachado):
            self.h = 40
            self.w = 90
            self.y = 440
        elif (self.agachado == False):
            self.w = 70
            self.h = 80
            self.y = 400
        
class obstaculo:
    
    def __init__(self):
        self.x, self.y = 1030, 400
        self.h = 80
        self.color = (0,255,0)
        self.velocidad = 0.9
        self.puntua = False
        
        tipos_obstaculos = [1,2,3]
        tipo_objeto = random.choice(tipos_obstaculos)
        
        if tipo_objeto == 1:
            self.w = 30
        elif tipo_objeto == 2:
            self.w = 64
        elif tipo_objeto == 3:
            self.w = 98
    
    def display(self):
        pygame.draw.rect(ventana, self.color, pygame.Rect(self.x, self.y, self.w, self.h))   
    
    def actualizar(self):
        self.x = self.x - self.velocidad
    

#class juego:
    #cubo1 = cubo()     

def chequear_colisiones(obstaculo, cubo):
    obstaculo_Rect = pygame.Rect(obstaculo.x, obstaculo.y, obstaculo.h, obstaculo.w)
    cubo_Rect = pygame.Rect(cubo.x, cubo.y, cubo.h, cubo.w)
    collide = pygame.Rect.colliderect(obstaculo_Rect, cubo_Rect)
    if collide:
        print("colision!!!")
        return True
    else:
        return False

def limpiar_lista_obstaculos(lista_obstaculos):
    if len(lista_obstaculos)>0:
        if lista_obstaculos[0].x < -100:
            lista_obstaculos.pop(0)
    

def display_lista_obstaculos(lista_obstaculos):
    #print("===========")
    for obstaculo in lista_obstaculos:
        obstaculo.display()
        obstaculo.actualizar()
        #print(obstaculo.x)
    #print("===========")

def puntuacion_texto(text, text_color, x, y):
    text_font = pygame.font.SysFont("Arial", 30)
    img = text_font.render(text, True, text_color)
    ventana.blit(img, (x, y))

  
def puntos(lista_obstaculos):
    global puntuacion
    if len(lista_obstaculos)>0:
        if ((lista_obstaculos[0].puntua==False) and (round(lista_obstaculos[0].x) == 145)):
            lista_obstaculos[0].puntua=True
            puntuacion = puntuacion + 1    
            #print(puntuacion)
        
def main():
    cubo1 = cubo()
    #cubo2 = cubo()
    #cactus = obstaculo()
    #cactus2 = obstaculo()

    lista_obstaculos = [obstaculo()]
    
    #cubo2.color_nuevo((0,0,255))
    #cubo2.ancho_nuevo((150))

    time_inicio = round(time.time()*1000)

    lista_de_segundos = [2000, 2500, 3000, 3500]
    time_random = random.choice(lista_de_segundos)   
      
    while True:
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cubo1.saltando = True
                elif event.key == pygame.K_DOWN:
                    cubo1.agachado = True
                #if cubo1.saltando = True and cubo1.agachado = True
                    #cubo1.self.y = 400
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    cubo1.agachado = False
                #elif event.key == pygame.K_a:
                    #cubo2.saltando =True


            
        ventana.fill((0,0,0))
        cubo1.actualizar()
        cubo1.display()
        puntuacion_texto("score:", (255,255,255), 800, 25)
        puntuacion_texto(str(puntuacion), (255,255,255), 900, 25)
        puntos(lista_obstaculos)
        
        
        ### lanzamos un obstaculo cada 2 segundos ---------
        time_actual = round(time.time()*1000)
                
        if time_actual - time_inicio >= time_random:
            time_random = random.choice(lista_de_segundos)   
            lista_obstaculos.append(obstaculo())
            time_inicio = time_actual
        ### --------------------------------

        limpiar_lista_obstaculos(lista_obstaculos)        
        display_lista_obstaculos(lista_obstaculos)

        if len(lista_obstaculos) > 0:
            colision = chequear_colisiones(lista_obstaculos[0], cubo1)
            
        if colision==True:
            pygame.quit() 
            sys.exit()
                    
        #cubo2.actualizar()
        #cubo2.display()
        #print(cubo1.y)
        pygame.display.update()

    

main()