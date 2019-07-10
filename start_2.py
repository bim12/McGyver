#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Learn Pygame
Pour y accéder, il faudra taper CONSTANTE, plutôt que pygame.CONSTANTE ! :)
Celà vous permettra une meilleure lisibilité dans l'utilisation de
ces constantes, vous verrez plus tard à quoi elles serviront
"""
import os
import pygame
from pygame.locals import*

bg_file = 'pictures/background.jpg'
personne = 'pictures/MacGyver.png'
ether= "pictures/ether.png"

pygame.init()

###	print(dir(pygame.init())) dir() permet de recuperer les methodes et les attributs d'une classe ####

#Ouverture de la fentre pygame  #######################################################################
fenetre = pygame.display.set_mode((600,480))
fenetre_w,fenetre_h = fenetre.get_width(),fenetre.get_height() # recuperer les dimensions de la fentre


#chargement et collage du fond	#######################################################################
fond = pygame.image.load(bg_file).convert()#permet un chargement +rapide
fenetre.blit(fond,(0,0))

#Chargement et collage du personnage et de l'objet ether       	   ####################################
#perso.set_colorkey(perso,(255,255,255))
ether = pygame.image.load(ether).convert()
perso = pygame.image.load(personne).convert()
perso.set_colorkey((0,0,0))#transparence du noir(0,0,0)
#position_perso = perso.get_rect()


position_ether = fenetre.blit(ether,(100,0))
perso_h,perso_w = perso.get_height(),perso.get_width() 	# recuperer la taille de l'image	##########
perso_x = fenetre_w / 2 - perso_w / 2
perso_y = fenetre_h / 2 - perso_h / 2
position_perso=fenetre.blit(perso,(perso_x,perso_y))	# positioner le personnage au centre #########

###	print(position_perso.x,position_perso.y) position x,y coin haut gauche de l'image  ###############
fenetre.blit(perso,position_perso)
fenetre.blit(ether,position_ether)
#Rafrechissement de l'ecran
pygame.display.flip()
pygame.key.set_repeat(400, 30)	# déplacement en maintenant les touches enfocees	##################


#version 1	##########################################################################################
continuer = 1
ether_state = 1
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		if event.type == KEYDOWN:
			if event.key == K_DOWN:
				# On descend la personne (coordonnes x=0; et y = 3 pixelles vers le bas
				position_perso = position_perso.move(0,5)
				print(position_perso.x,position_perso.y)
			if event.key == K_UP:
				position_perso = position_perso.move(0,-5)
				print(position_perso.x,position_perso.y)
			if event.key == K_LEFT:
				position_perso = position_perso.move(-5,0)
				print(position_perso.x,position_perso.y)
			if event.key == K_RIGHT:
				position_perso = position_perso.move(5,0)
				print(position_perso.x,position_perso.y)
		if event.type == MOUSEBUTTONDOWN :
			if event.button == 1:
				position_perso = fenetre.blit(perso,(event.pos[0],event.pos[1]))
				#print(position_perso.x,position_perso.y)
		if position_ether.colliderect(position_perso):
			print('colision')
			position_ether=fenetre.blit(ether,(0,440))



	#Recolage de la fenetre 	#######################################################################
	fenetre.blit(fond,(0,0))
	fenetre.blit(perso,position_perso)
	fenetre.blit(ether,position_ether)
	
	
		
		
		
	#Rafrechissement

	pygame.display.flip()

'''
#version 2
continuer = 1
while continuer:
    event = pygame.event.wait ()
    if event.type == pygame.QUIT:
        continuer = 0 # Be IDLE friendly
        pygame.quit ()
'''