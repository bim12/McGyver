#! usr/bin/python3
#-*- coding:utf-8 -*-


"""
The game or MacGyver must escape the labyrinth
It must have the following elements (scattered in the labyrinth): 
a needle, a small plastic tube and ether.
They will allow MacGyver to create a syringe and lull the guardian to sleep...

Python scrits
Files : mc_gyver.py, classes.py, constants.py, l1 = (labyrinth structure file)
"""

import pygame
from pygame.locals import *
from classes import *
from constants import *

pygame.init()

#Opening the Pygame window (square: width = height)
window = pygame.display.set_mode((window_side, window_height))
#Icon
icon = pygame.image.load(image_icon)
pygame.display.set_icon(icon)
#Title
pygame.display.set_caption(window_title)

#Primary loop
follow = 1
while follow:
	#Loading and viewing the home screen
	home = pygame.image.load(image_home).convert()
	window.blit(home,(0,0))
	
	#Refreshment
	pygame.display.flip()

	#These variables are reset to 1 at each loop turn
	continue_game = 1
	continue_home = 1

	#Welcome loop
	while continue_home:
	
		#Speed limitation of the loop
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#If the user leaves, we put the variables
			#of loop to 0 to browse none and close
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continue_home = 0
				continue_game = 0
				follow = 0
				#Variable de choice du level
				choice = 0

			#Hit F10 to retourn to menu if Mc Loose or Winn
			if event.type == KEYDOWN and event.key == K_F10:
					continue_home = 0
					continue_game = 0
					image_home = home_bis

			elif event.type == KEYDOWN:				
				#Lancement du level
				if event.key == K_F1:
					continue_home = 0	#Leave home
					choice = 'l1'		#Level to load
		

	#we check that the player has made a choice
	#to not load if he leaves
	if choice != 0:
		#Load the background
		backgr = pygame.image.load(image_bg).convert()

		#Level generation
		level = Level(choice)
		level.generate()
		level.display(window)

		#Pass the index of the line where the objects are
		line_tube = level.line_tube
		tube = level.r1[0] # Index of the location where the object is in the line

		line_ether = level.line_ether
		ether = level.r2[0]# Index of the location where the object is in the line

		line_needle = level.line_needle
		needle = level.r3[0]# Index of the location where the object is in the line

		#Creation of the counter of the objects retrieved
		object_count = 0
		
		# Creating MacGyver
		Mc = Person("pictures/MacGyver.png", level)

				
	#THE GAME LOOP
	while continue_game:
		
		#Loop speed limit
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():
		
			#If the user leaves, we put the variable that continues the game to 0
			#ET the general variable to 0 to close the window
			if event.type == QUIT:
				continue_game = 0
				follow = 0
				
				
			elif event.type == KEYDOWN:
				#If the user press Esc here, we return only to the menu
				if event.key == K_ESCAPE:
					continue_game = 0
				
				#MagGyver moving keys
				if event.key == K_RIGHT:
					Mc.displacement('right')
				if event.key == K_LEFT:
					Mc.displacement('left')		
				if event.key == K_UP:
					Mc.displacement('top')		
				if event.key == K_DOWN:
					Mc.displacement('bottom')

		#Display to new positions
		window.blit(backgr, (0,0))
		level.display(window)
		window.blit(Mc.direction, (Mc.x, Mc.y)) #Mc.direction
		pygame.display.flip()

		#Counter incrementation based on the objects retrieved
		if level.structure[Mc.case_y][Mc.case_x] == '1':
			#print('plastic_tube')
			level.structure[line_tube][tube] = '0'
			object_count += 1

			
		if level.structure[Mc.case_y][Mc.case_x] == '2':
			#print('ether')
			level.structure[line_ether][ether] = '0'
			object_count += 1
			
			
		if level.structure[Mc.case_y][Mc.case_x] == '3':
			#print('needle')
			level.structure[line_needle][needle] = '0'
			object_count += 1
				
		#print(object_count)

		#Display counter
		if object_count == 0:
			level.structure[15][1] = 'c'
		if object_count == 1 :
			#show number 1
			level.structure[15][1] = 'd'

		if object_count == 2:
			#show number 2
			level.structure[15][1] = 'e'

		if object_count == 3:
			#show number 3
			level.structure[15][1] = 'f'
			#show syringe
			level.structure[15][2] = 'g'

		#Lost part -> Restart
		if level.structure[Mc.case_y][Mc.case_x] == 'a' and object_count <= 2 :
			continue_game = 0
			image_home = image_reload
		
		# VICTORY -> End of GAME
		if level.structure[Mc.case_y][Mc.case_x] == 'a' and object_count == 3 :
			continue_game = 0
			image_home = image_winn		