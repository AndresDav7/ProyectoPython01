import pygame, sys
import time
import tkinter as tk
from tkinter import*

pygame.init()
def cargar_imagen(nombre, transparente=False):
    imagen = pygame.image.load(nombre)
    imagen = imagen.convert()
    if transparente:
        color = imagen.get_at((0, 0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen

class BotonPlay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.imagen = cargar_imagen("Imagenes/boton1.png", True)
        self.rect = self.imagen.get_rect()
        self.rect.bottom = 590 #Pos en y de self.imagen(sprite)
        self.rect.left = 15 # Pos en x de self.imagen(sprite)
        self.speed = 3


ventana = pygame.display.set_mode((700,500)) #Tamaño de la Pantalla
pygame.display.set_caption('Megaman X') #Nombre de la Pantalla       

while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #ventana.blit(imagen,(0,0))
    #pygame.display.update()
