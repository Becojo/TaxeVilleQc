#!/usr/bin/env python
#import
from __future__ import division
import math
import os 

# Variables
tranche = 100
evaluation = None
arrondissement = None
tempo = None
number = None
cout_taxe = None
pourcentage_eval = None 

# Immeubles residentiels de 1 a 5 logements (taux de base)
immeuble_1_5 = {
	'Vanier':0.7986,
	'Lac St-Charles':0.8371,
	'Sillery':0.8454,
	'Beauport':0.8498,
	'Charlesbourg':0.8506,
	'Ste-Foy':0.8592,
	'Quebec':0.9279,
	'St-Emile':0.8552,
	'Cap-Rouge':0.8960,
	'Loretteville':0.9436,
	'Val-Belair':0.9826
}
# Immeubles residentiels de 6 logements et plus
immeuble_6 = {
	'Vanier':0.8705,
	'Lac St-Charles':0.9124,
	'Sillery':0.9215,
	'Beauport':0.9263,
	'Charlesbourg':0.9271,
	'Ste-Foy':0.9365,
	'Quebec':1.0114,
	'St-Emile':0.9321,
	'Cap-Rouge':0.9766,
	'Loretteville':1.0285,
	'Val-Belair':1.0711
}
#Immeubles non residentiels
Immeuble_non = {
	'Vanier':3.1103,
	'Lac St-Charles':3.0440,
	'Sillery':3.0742,
	'Beauport':3.0902,
	'Charlesbourg':3.0931,
	'Ste-Foy':3.1543,
	'Quebec':3.3742,
	'St-Emile':3.0850,
	'Cap-Rouge':3.1184,
	'Loretteville':3.2461,
	'Val-Belair':3.2151
}
#Terrains vagues desservis
terrain = {
	'Vanier':1.5972,
	'Lac St-Charles':1.6742,
	'Sillery':1.6908,
	'Beauport':1.6996,
	'Charlesbourg':1.7012,
	'Ste-Foy':1.7184,
	'Quebec':1.8558,
	'St-Emile':1.7104,
	'Cap-Rouge':1.7920,
	'Loretteville':1.8872,
	'Val-Belair':1.9652
}

type_immeuble = {
	1 : "immeuble_1_5",
	2 : "immeuble_6",
	3 : "immeuble_non",
	4 : "terrain"
}

# Debut du script
os.system('clear')
print "Let's have some fun ! \n"
evaluation = raw_input("L'evaluation de votre immeuble ou terrain est de combien ? ")
number = raw_input("""Quel est le type d'immeuble ?\n 
	1. Immeubles residentiels de 1 a 5 logements (taux de base)\n
	2. Immeubles residentiels de 6 logements et plus\n
	3. Immeubles non residentiels\n
	4. Terrains vagues desservis\n
	Indiquez le numeros : 
	 """)
arrondissement = raw_input("""Dans quel arrondissement etes-vous ?\n
	 Vanier, Lac St-Charles, Sillery, \n 
	 Beauport, Charlesbourg, Ste-Foy, \n
	 Quebec, St-Emile, Cap-Rouge, \n
	 Loretteville,Val-Belair \n
	 Ecrivez le nom de l'arrondissement (Attention a la casse) : 
	 """)

cout_taxe = terrain[arrondissement] * (float(evaluation) / 100)
pourcentage_eval = float(cout_taxe)/float(evaluation) * 100

print '\n'
os.system('clear')
print "Le type d'immeuble :  " + type_immeuble[1] + "\n"
print "L'arrondissement :  " + arrondissement + "\n"
print  terrain[arrondissement] 
print '\n'
print "L'evaluation de la propriete est de : " + evaluation + "\n"
print "Cout des taxes : "
print  terrain[arrondissement] * (float(evaluation) / 100)
print "\n"
print "Pourcentage du cout des taxes compare a l'evaluation"  + "\n"
print  str(pourcentage_eval) + "%"


