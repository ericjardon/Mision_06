#Autor: Eric Andrés Jardón Chao
#Espirógrafo: Mision Imposible 06.

import pygame   # Librería de pygame
import math
import random

def obtenerColor():
    color=(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
    return color

# Dimensiones de la pantalla
ANCHO = 700
ALTO = 600
# Colores
BLANCO = (255, 255, 255)
randomColor1=obtenerColor()
randomColor2=obtenerColor()
randomColor3=obtenerColor()


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        for angulo in range(0,(360*(r//math.gcd(r,R))+1)): #Primer figura
            a = math.radians(angulo)
            k= r/R
            coordX= int(R*((1-k)*math.cos(a)+l*k*math.cos(a*((1-k)/k))))
            coordY= int(R*((1-k)*math.sin(a)-l*k*math.sin(a*((1-k)/k))))
            pygame.draw.circle(ventana,randomColor1,(ANCHO//2+coordX,ALTO//2-coordY),1)
        r2=r-50
        R2=R+50
        l2=1-l
        for angulo in range(0,(360*(r2//math.gcd(r2,R2))+1)): #Segunda figura: otro radio interno, otro l, otro color.
            a = math.radians(angulo)
            k = r2 / R2
            coordX= int(R2*((1-k)*math.cos(a)+l2*k*math.cos(a*((1-k)/k))))
            coordY= int(R2*((1-k)*math.sin(a)-l2*k*math.sin(a*((1-k)/k))))
            pygame.draw.circle(ventana,randomColor2,(ANCHO//2+coordX,ALTO//2-coordY),1)

        r3=r+70
        R3=R-70
        l3=l+0.5
        for angulo in range(0,(360*(r3//math.gcd(r3,R3))+1)): #Para la tercer figura: otro radio interno, otro l, otro color.
            a = math.radians(angulo)
            k = r3 / R3
            coordX= int(R3*((1-k)*math.cos(a)+l3*k*math.cos(a*((1-k)/k))))
            coordY= int(R3*((1-k)*math.sin(a)-l3*k*math.sin(a*((1-k)/k))))
            pygame.draw.circle(ventana,randomColor3,(ANCHO//2+coordX,ALTO//2-coordY),1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame
# Función principal, aquí resuelves el problema
def main():
    r=int(input("Teclea el parámetro r:"))
    R=int(input("teclea el parámetro R:"))
    l=float(input("Teclea el parámetro l: "))
    dibujar(r,R,l)   # Por ahora, solo dibuja


# Llamas a la función principal
main()