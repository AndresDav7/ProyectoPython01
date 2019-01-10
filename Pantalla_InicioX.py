import pygame, sys
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from pygame.locals import *
from random import randint, uniform, random
 
pygame.init()
def cargar_imagen(nombre, transparente=False):
    imagen = pygame.image.load(nombre)
    imagen = imagen.convert()
    if transparente:
        color = imagen.get_at((0, 0))
        imagen.set_colorkey(color, RLEACCEL)
    return imagen

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)

    def update(self):
        self.left, self.top = pygame.mouse.get_pos()

class BotonPlay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.imagen = cargar_imagen("Imagenes/boton1.png", True)
        self.rect = self.imagen.get_rect()
        self.rect.bottom = 590 #Pos en y de self.imagen(sprite)
        self.rect.left = 15 # Pos en x de self.imagen(sprite)
        self.speed = 3

icono = pygame.image.load("Imagenes/icono.png") #Ruta de la imagen de icono
pygame.display.set_icon(icono) #Cambio de icono de la ventana
 
ventana = pygame.display.set_mode((700,500)) #Tamaño de la Pantalla
pygame.display.set_caption('Megaman X') #Nombre de la Pantalla

imagen = pygame.image.load("Imagenes/fondoInicio.png") #Insertar imagen de fondo

pygame.mixer.music.load('Musica/Inicio.mp3') #Colocar la musica de fondo
pygame.mixer.music.play(5)

while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ventana.blit(imagen,(0,0))
    pygame.display.update()
