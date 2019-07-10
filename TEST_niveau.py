from random import *

with open('l1', "r") as fichier:
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
structure = structure_niveau

#Nombre des lignes contenent le '0' soit le labyrinthe pour deposer les objets
vides=[]
for index,ligne in enumerate(structure):
	if '0' in ligne:
		vides.append(index)
print('Nombre des lignes contenent le \'0\' soit le labyrinthe pour deposer les objets = ')
print(vides)
#prendre trois lignes depuis les vides au hasard pour y deposer des objets seringe, needle, et tube( soit 1,2,3)
l_has =sample(vides,k=3)
print('liste des trois lignes uniques choisises au hasard =',l_has)

# dans chaque une des lignes trouver les index des emplcement des '0' et les placer dans les listes correspondantes
l_has_1=[]
l_has_2=[]
l_has_3=[]

for index,spt in enumerate(structure[l_has[0]]):
	if '0' in spt:
		l_has_1.append(index)
print('les index des zeros de la ligne 1 l_has_1 = ',l_has_1)

for index,spt in enumerate(structure[l_has[1]]):
	if '0' in spt:
		l_has_2.append(index)
print('les index des zeros de la ligne 2 l_has_2 = ', l_has_2)

for index,spt in enumerate(structure[l_has[2]]):
	if '0' in spt:
		l_has_3.append(index)
print('les index des zeros de la ligne3 l_has_3 = ' , l_has_3)

#identifier un zero au hasard qui serais remplacée dans chaquene des lignes 
r1=sample(l_has_1,k=1)
print('zero a remplacer r1 = ',r1)
r2=sample(l_has_2,k=1)
print('zero a remplacer r2 = ',r2)
r3=sample(l_has_3,k=1)
print('zero a remplacer r3 = ',r3)

print('verification si les zeros sont bien remplacées pour chaque ligne')
print(structure[l_has[0]])
structure[l_has[0]][r1[0]]='x'
print(structure[l_has[0]])

print(structure[l_has[1]])
structure[l_has[1]][r2[0]]='y'
print(structure[l_has[1]])

print(structure[l_has[2]])
structure[l_has[2]][r3[0]]='z'
print(structure[l_has[2]])

#print(structure)
