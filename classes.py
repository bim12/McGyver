"""Classes du jeu de MacGyver"""

import pygame
from pygame.locals import * 
from constants import *
from random import *

class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
		self.ligne_tube=0
		self.r1 = 0
		self.ligne_ether = 0
		self.r2 = 0
		self.ligne_needle = 0
		self.r3 = 0
	
	
	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau

		
		#Nombre des lignes contenent le '0' soit le labyrinthe pour deposer les objets
		vides=[]
		for index,ligne in enumerate(self.structure):
			if '0' in ligne:
				vides.append(index)

		#prendre trois lignes depuis les vides au hasard pour y deposer des objets tube,ether,needle( soit 1,2,3)
		l_has =sample(vides,k=3)
		#Enregistrer les emplacements
		self.ligne_tube = l_has[0]
		self.ligne_ether = l_has[1]
		self.ligne_needle = l_has[2]

		# dans chaque une des lignes trouver les index des emplcement des '0' et les placer dans les listes correspondantes
		l_has_1=[]
		l_has_2=[]
		l_has_3=[]

		for index,spt in enumerate(self.structure[l_has[0]]):
			if '0' in spt:
				l_has_1.append(index)

		for index,spt in enumerate(self.structure[l_has[1]]):
			if '0' in spt:
				l_has_2.append(index)
		
		for index,spt in enumerate(self.structure[l_has[2]]):
			if '0' in spt:
				l_has_3.append(index)
		

		#identifier l'index d'un zero pris au hasard qui serais remplacée dans chaque une des lignes
		self.r1=sample(l_has_1,k=1)
		self.r2=sample(l_has_2,k=1)
		self.r3=sample(l_has_3,k=1)
		
		#remplacement des zeros avec les objets
		self.structure[l_has[0]][self.r1[0]]='1'
		self.structure[l_has[1]][self.r2[0]]='2'
		self.structure[l_has[2]][self.r3[0]]='3'

		#print(self.structure)

	
	def afficher(self, fenetre):
		'''Méthode permettant d'afficher le niveau en fonction
		de la liste de structure renvoyée par generer()"""
		Chargement des images (seule celle d'arrivée contient de la transparence)'''
		mur = pygame.image.load(image_mur).convert()
		depart = pygame.image.load(image_depart).convert()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()
		plastic_tube=pygame.image.load(image_plastic_tube).convert_alpha()
		ether=pygame.image.load(image_ether).convert_alpha()
		needle=pygame.image.load(image_needle).convert_alpha()


		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'w':		   #m = Mur
					fenetre.blit(mur, (x,y))
				elif sprite == 's':		   #d = Départ
					fenetre.blit(depart, (x,y))
				elif sprite == '1':
					fenetre.blit(plastic_tube,(x,y))
				elif sprite == '2':
					fenetre.blit(ether,(x,y))
				elif sprite == '3':
					fenetre.blit(needle,(x,y))
				elif sprite == 'a':		   #a = Arrivée
					fenetre.blit(arrivee, (x,y))
				num_case += 1
			num_ligne += 1
			
			
class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, droite, gauche, haut, bas, niveau):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve 
		self.niveau = niveau
	
	
	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""
		
		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'w':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			# #Image dans la bonne direction
			self.direction = self.droite
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'w':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'w':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'w':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas
