#! usr/bin/python3
#-*- coding:utf-8 -*-

"""
The game where McGyver .....
Python scrits
Files : mc_gyver.py, classes.py, constantes.py, l1 = (labyrinth structure file)
"""

import pygame
from pygame.locals import *

from classes import *
from constants import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, hauteur_fenetre))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)

#BOUCLE PRINCIPALE
continuer = 1
while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_accueil).convert()
	counter = pygame.image.load(image_counter_0).convert_alpha()
	#syringe = pygame.image.load(image_syringe_0).convert_alpha()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1

	#BOUCLE D'ACCUEIL
	while continuer_accueil:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				choix = 0
				
			elif event.type == KEYDOWN:				
				#Lancement du niveau 1
				if event.key == K_F1:
					continuer_accueil = 0	#On quitte l'accueil
					choix = 'l1'		#On définit le niveau à charger
				# #Lancement du niveau 2
				# elif event.key == K_F2:
				# 	continuer_accueil = 0
				# 	choix = 'n2'
			
		

	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		#Passer l'index de la ligne  ou se trouvent les objets
		ligne_tube=niveau.ligne_tube
		tube=niveau.r1[0] # Index de l'mplacement ou se trouve l'objet dans la ligne

		ligne_ether = niveau.ligne_ether
		ether=niveau.r2[0]# Index de l'mplacement ou se trouve l'objet dans la ligne

		ligne_needle = niveau.ligne_needle
		needle = niveau.r3[0]# Index de l'mplacement ou se trouve l'objet dans la ligne

		#Creation du compteur des objets recuperées
		object_count = 0

		# text setting
		#font_obj = pygame.font.Font('freesansbold.ttf', 22)
		#text_surface_obj = font_obj.render('O', True, blue)
		#text_rect_obj = text_surface_obj.get_rect()
		#text_rect_obj.center = (30, 620)


		#Création de McGyver
		Mc = Perso("pictures/MacGyver.png", "pictures/MacGyver.png", 
		"pictures/MacGyver.png", "pictures/MacGyver.png", niveau)

				
	#BOUCLE DE JEU
	while continuer_jeu:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0
		
			elif event.type == KEYDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == K_ESCAPE:
					continuer_jeu = 0
					
				#Touches de déplacement de Donkey Kong
				elif event.key == K_RIGHT:
					Mc.deplacer('droite')
				elif event.key == K_LEFT:
					Mc.deplacer('gauche')
				elif event.key == K_UP:
					Mc.deplacer('haut')
				elif event.key == K_DOWN:
					Mc.deplacer('bas')
			
		#Affichages aux nouvelles positions
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(Mc.direction, (Mc.x, Mc.y)) #Mc.direction = l'image dans la bonne direction
		fenetre.blit(counter, (20, 600))
		pygame.display.flip()

		#Objet recuperation and counter incrementation
		if niveau.structure[Mc.case_y][Mc.case_x] == '1':
			#print('plastic_tube')
			niveau.structure[ligne_tube][tube] = '0'
			object_count += 1

		if niveau.structure[Mc.case_y][Mc.case_x] == '2':
			#print('ether')
			niveau.structure[ligne_ether][ether] = '0'
			object_count += 1

		if niveau.structure[Mc.case_y][Mc.case_x] == '3':
			#print('needle')
			niveau.structure[ligne_needle][needle] = '0'
			object_count += 1
		print(object_count)

		#if object_count == 1 :
			#image_counter_0 = image_counter_1
		#if object_count == 2:
			#image_counter_0 = image_counter_2
		#if object_count == 3:
			#image_counter_0 = image_counter_3
			#image_syringe_0 = image_syringe_1

		#Perdu -> DOIT RECOMENCER
		if niveau.structure[Mc.case_y][Mc.case_x] == 'a' and object_count <= 2 :
			continuer_jeu = 0
			image_accueil = image_reload

		# Victoire -> Fin de jeux
		if niveau.structure[Mc.case_y][Mc.case_x] == 'a' and object_count == 3 :
			continuer_jeu = 0
			image_accueil = image_winn
