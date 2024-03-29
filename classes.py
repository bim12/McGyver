#! usr/bin/python3
#-*- coding:utf-8 -*-

"""Classes of MacGyver game"""

import pygame
from pygame.locals import *
from constants import *
from random import sample

class Level:
	"""Class to create a level"""
	def __init__(self, file):
		self.file = file
		self.structure = 0
		self.line_tube=0
		self.r1 = 0
		self.line_ether = 0
		self.r2 = 0
		self.line_needle = 0
		self.r3 = 0
	
	
	def generate(self):
		"""Level generation method according to the level file.
			We create a general list, containing a list per line to display.
			And we randomly place 3 objects in the free slots. """	
		#On opens the file
		with open(self.file, "r") as file:
			self.structure = [[sprite for sprite in line if sprite !='\n'] for line in file]

		#Take three lines from random voids to deposit objects: 
		#tube,ether,needle( either 1,2,3)
		l_has =sample([x for x in range(len(self.structure)) if '0' in self.structure[x]],k=3)
		
		#Save locations (l_has = line hasard choice )
		self.line_tube = l_has[0]
		self.line_ether = l_has[1]
		self.line_needle = l_has[2]

		# In each of the lines find the indexes of the '0' locations, 
		# and place them in the corresponding lists
		l_has_1 = [index for index,spt in enumerate(self.structure[l_has[0]]) if '0' in spt]
		l_has_2 = [index for index,spt in enumerate(self.structure[l_has[1]]) if '0' in spt]
		l_has_3 = [index for index,spt in enumerate(self.structure[l_has[2]]) if '0' in spt]
		
		#identify the index of a random zero that 
		#would be replaced in each one of the random lines
		self.r1 = sample(l_has_1,k=1)
		self.r2 = sample(l_has_2,k=1)
		self.r3 = sample(l_has_3,k=1)
		
		#replacement of zeros with objects
		self.structure[l_has[0]][self.r1[0]] = '1'
		self.structure[l_has[1]][self.r2[0]] = '2'
		self.structure[l_has[2]][self.r3[0]] = '3'
	
	def display(self, window):
		"""Method to display the level according to structure list returned by generate()"""
		#Loading images
		wall = pygame.image.load(image_wall).convert()
		start = pygame.image.load(image_start).convert()
		arrival = pygame.image.load(image_arrival).convert_alpha()
		bottom_b = pygame.image.load(image_bottom).convert()
		plastic_tube=pygame.image.load(image_plastic_tube).convert_alpha()
		ether=pygame.image.load(image_ether).convert_alpha()
		needle=pygame.image.load(image_needle).convert_alpha()
		c0 = pygame.image.load(image_counter_0).convert_alpha()
		c1 = pygame.image.load(image_counter_1).convert_alpha()
		c2 = pygame.image.load(image_counter_2).convert_alpha()
		c3 = pygame.image.load(image_counter_3).convert_alpha()
		sy = pygame.image.load(image_syringe).convert_alpha()

		#We browse the level list
		num_line = 0
		for line in self.structure:
			#We browse lists of lines
			num_case = 0
			for sprite in line:
				#On calculates the actual position in pixels
				x = num_case * sprite_size
				y = num_line * sprite_size
				if sprite == 'w':		   
					window.blit(wall, (x,y))
				elif sprite == 's':		   
					window.blit(start, (x,y))
				elif sprite == '1':
					window.blit(plastic_tube,(x,y))
				elif sprite == '2':
					window.blit(ether,(x,y))
				elif sprite == '3':
					window.blit(needle,(x,y))
				elif sprite == 'a':		  
					window.blit(arrival,(x,y))
				elif sprite == 'b':
					window.blit(bottom_b,(x,y))
				elif sprite == 'c':
					window.blit(c0,(x,y))
				elif sprite == 'd':
					window.blit(c1,(x,y))
				elif sprite == 'e':
					window.blit(c2,(x,y))
				elif sprite == 'f':
					window.blit(c3,(x,y))
				elif sprite == 'g':
					window.blit(sy,(x,y))
				num_case += 1
			num_line += 1
						
class Person:
	"""Class to create a character"""
	def __init__(self, img, level):
		#Sprites of the character
		self.default = pygame.image.load(img).convert_alpha()

		#Position of the character in boxes and pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction 
		self.direction = self.default
		#Level in which the character is located
		self.level = level
	
	
	def displacement(self, direction):
		"""Method for moving the character"""
		
		# Move to the right
		if direction == 'right':
			#To not exceed the screen
			if self.case_x < (number_sprite_side - 1):
				#Check that the destination box is not a wall
				if self.level.structure[self.case_y][self.case_x+1] != 'w':
					# Moving a box
					self.case_x += 1
					#Calculation of the "real" pixel position
					self.x = self.case_x * sprite_size
			#The right way 
			self.direction = self.default
		
		#Move to the left
		if direction == 'left':
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x-1] != 'w':
					self.case_x -= 1
					self.x = self.case_x * sprite_size
			self.direction = self.default
		
		#Move up
		if direction == 'top':
			if self.case_y > 0:
				if self.level.structure[self.case_y-1][self.case_x] != 'w':
					self.case_y -= 1
					self.y = self.case_y * sprite_size
			self.direction = self.default
		
		#Move down
		if direction == 'down':
			if self.case_y < (number_sprite_side - 1):
				if self.level.structure[self.case_y+1][self.case_x] != 'w':
					self.case_y += 1
					self.y = self.case_y * sprite_size
			self.direction = self.default