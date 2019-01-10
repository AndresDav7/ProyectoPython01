import pygame, sys, random

from pygame import sprite
from random import randint
from pygame.locals import *
 
pygame.init()

clock=pygame.time.Clock()

#Cargar imagen de fondo del juego
fondo=pygame.image.load("Imagenes/FondoCielo.png")

icono = pygame.image.load("Imagenes/icono.png") #Ruta de la imagen de icono
pygame.display.set_icon(icono) #Cambio de icono de la ventana

ventana = pygame.display.set_mode((700,390)) #Tamaño de la Pantalla
pygame.display.set_caption('Megaman X') #Nombre de la Pantalla

pygame.mixer.music.load('Musica/Nivel.mp3') #Colocar la musica de fondo
pygame.mixer.music.play(7)

#Texto en juego
fuente1=pygame.font.SysFont("Calibri",27,True,False)

pygame.display.update()

x=0
y=0

pygame.joystick.init()  # variable para cargar el joystick

try:
	j = pygame.joystick.Joystick(0) # igualamos una variable para cargar la palanca
	j.init()
	print ("Joystick: {0}".format(j.get_name()))#imprimimos si lee el joytick
except pygame.error:
	print ("No joystick")


class Personaje(sprite.Sprite):
    def __init__(self):
        sprite.Sprite.__init__(self)
        #Carga la imagen y la hace transaparente
        self.spriteSheet = pygame.image.load('Imagenes/MXTra01.png').convert_alpha()
        #Seleccionamos al personaje en la imagen png
        self.image=pygame.transform.scale(self.spriteSheet.subsurface((0,0,145,150)),(75,95))
        
        #Muestra la imagen
        self.rect=self.image.get_rect()
        #Lugar donde se ubica la imagen
        self.rect.center=(ventana.get_width()/2, 180)

        self.speed=10  #Se mueve 10pixeles en la direccion 

        self.frames = 8             #Número máximo de imágenes
        self.current_frame = 0      #Frame actual
        self.frame_width = 75       #Anchura de la imagen
        self.frame_height = 95      #Altura de la imagen
        
    def updateIzquierda(self,dt,ventana):
        #Funcion en la que se actualiza el sprite y que se repita en bucle
        if self.current_frame >= self.frames-1:
            self.current_frame = 0
        else :
            #para que aparezca 8 imagenes por segundo
           self.current_frame += 8*dt
        self.image = pygame.transform.scale(
            self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width*2,0,145,150)),
            (self.frame_width,self.frame_height))
        self.image=pygame.transform.flip(self.image,True,False)

    def update(self,dt,ventana):
        #Funcion en la que se actualiza el sprite y que se repita en bucle
        if self.current_frame >= self.frames-1:
            self.current_frame = 0
        else :
            #para que aparezca 8 imagenes por segundo
           self.current_frame += 8*dt
        self.image = pygame.transform.scale(
            self.spriteSheet.subsurface((int(self.current_frame)*self.frame_width*2,0,145,150)),
            (self.frame_width,self.frame_height))
        
        
    def mover(self, x=0, y=0):
        #funcion para mover al personaje y para que no se salga de la ventana
        if self.rect.centerx+x >= ventana.get_width() or self.rect.centerx+x < 0:
            return
        if self.rect.centery+y >= ventana.get_height() or self.rect.centery+y < 0:
            return
        self.rect.center = (self.rect.centerx+x, self.rect.centery+y)      

#Generamos el sprite
megaman=Personaje()
grupo_sprites = pygame.sprite.GroupSingle()
grupo_sprites.add(megaman)

#Vacios
megaman_obstaculo=Personaje()
megaman_obstaculo.rect.center=(ventana.get_width()-20,ventana.get_height()/2)
grupo_obstaculo = pygame.sprite.GroupSingle()
grupo_obstaculo.add(megaman_obstaculo)

vacio2=Personaje()
vacio2.rect.center=(20,ventana.get_height()/2)
grupo2=pygame.sprite.GroupSingle()
grupo2.add(vacio2)

disparo1=Personaje()
disparo1.rect.center=(x,y)
grupo3=pygame.sprite.GroupSingle()
grupo3.add(disparo1)

#disparos
disparo=pygame.image.load("Imagenes/disparos.png")

disparo1=Personaje()
grupo3=pygame.sprite.GroupSingle()
grupo3.add(disparo1)

#Bucle del Juego
while True:
    dt = clock.tick(11) / 1000
    
    for eventos in pygame.event.get():
                
        if eventos.type == pygame.QUIT: #Se cerrará el juego 
            pygame.quit()
            sys.exit()

        pixels_h = pixels_v = 0

        if (eventos.type == pygame.JOYAXISMOTION):
            keys = pygame.key.get_pressed()
            if j.get_axis(0) >= 0.5:
                print ("right has been pressed")  # Right
                lead_x_change = block_size
                lead_y_change = 0
                grupo_sprites.update(dt,ventana)
                pixels_h = 10
                
            if j.get_axis(0) <= -1:
                print ("left has been pressed")   # Left
                lead_x_change = -block_size
                lead_y_change = 0
                megaman.updateIzquierda(dt,ventana)
                pixels_h = -10
                
        if eventos.type == pygame.KEYDOWN: #Para moverse a la izq. o a la der.
            keys = pygame.key.get_pressed()
            if keys[K_a]:
                megaman.updateIzquierda(dt,ventana)
                pixels_h = -10
                
            if keys[K_d]:
                grupo_sprites.update(dt,ventana)
                pixels_h = 10
                
    for i in grupo_sprites:
        i.mover(pixels_h,pixels_v)
    
    ventana.fill((0, 0, 0))
    ventana.blit(fondo,(0,0))
    grupo_sprites.draw(ventana)

    #grupo_obstaculo.draw(ventana)
    #grupo2.draw(ventana)
    
    #Tiempo/Cronometro
    segundos=pygame.time.get_ticks()/1000
    segundos= round(segundos,None)
    segundos = str(segundos)

    #Puntaje
    segundosDisp= int(segundos)
    segundosDisp=segundosDisp//3
    
    contador=fuente1.render("Tiempo: " + segundos,0,(0,0,230))
    info=fuente1.render("Puntaje: " +  str(segundosDisp) ,0,(0,0,0))

    if int(segundos)%5!=0:
        x=randint(100,580)
        y=0

    if int(segundos)%5==0:
        x=x
        y=195
    
    ventana.blit(contador,(560,25))
    ventana.blit(info,(25,25))
    
    disparo1.rect.center=(x,y)
    ventana.blit(disparo,(x,y))

    #En caso de colision 
    if pygame.sprite.collide_mask(megaman, megaman_obstaculo):
        pygame.mixer.pause()
        gameOver = pygame.image.load("Imagenes/gameOver.png")
        pygame.mixer.music.load('Musica/GameOver.mp3')
        pygame.mixer.music.play(2)
        ventana.blit(gameOver, (0, 0))
        puntajeFinal = str(segundosDisp)
        #print(puntajeFinal)
        
    if pygame.sprite.collide_mask(megaman, vacio2):
        #pygame.mixer.pause()
        gameOver = pygame.image.load("Imagenes/gameOver.png")
        #pygame.mixer.music.load('Musica/GameOver.mp3')
        #pygame.mixer.music.play(2)
        ventana.blit(gameOver, (0, 0))
        puntajeFinal = str(segundosDisp)
        #print(puntajeFinal)

    if pygame.sprite.collide_mask(megaman,disparo1):
        #pygame.mixer.pause()
        gameOver = pygame.image.load("Imagenes/gameOver.png")
        #pygame.mixer.music.load('Musica/GameOver.mp3')
        #pygame.mixer.music.play(2)
        ventana.blit(gameOver, (0, 0))
        puntajeFinal = str(segundosDisp)
        x=0
        y=0
        ventana.blit(gameOver, (0, 0))
        #print(puntajeFinal)
        

    
    pygame.display.flip()
    pygame.display.update()

