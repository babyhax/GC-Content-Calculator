#!/usr/bin/env python
#GC-Inhoud.py
#Python script dat de GC-Content van een DNA bestand kan berekenen
#https://github.com/Plofkip/GC-Inhoud

genen = open("voer-hier-het-txt-bestand-in.txt","r")

#Converteert de variabelen naar integers
g=0;
a=0;
c=0;
t=0;

#Slaat de eerste regel over
genen.readline()

#Telt de waarden van de GACT variabelen op voor elke GACT die voorkomt
for line in genen:
	line = line.lower()
	for char in line:
		if char == "g":
			g+=1
		if char == "a":
			a+=1
		if char == "c":
			c+=1
		if char == "t":
			t+=1

#Print de GACT waarde
print "aantal g's: " + str(g)
print "aantal a's: " + str(a)
print "aantal c's: " + str(c)
print "aantal t's: " + str(t)

#0. Converteert het naar een floating point
gc = (g+c+0.) / (a+t+c+g+0.)

#Print de uiteindelijke GC-Inhoud waarde
print "gc inhoud: " + str(gc)
