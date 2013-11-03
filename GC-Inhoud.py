#!/usr/bin/env python
#GCinhoud.py
#Berekent de GC inhoud

genen = open("voer-hier-bestand-in.txt","r")

#zorg dat de letters integers zijn (zet ze naar nul)
g=0;
a=0;
c=0;
t=0;

#zorg dat de eerste lijn niet meedoet
genen.readline()


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

print "aantal g's: " + str(g)
print "aantal a's: " + str(a)
print "aantal c's: " + str(c)
print "aantal t's: " + str(t)

#met 0. converteer ik hem naar een floating point
gc = (g+c+0.) / (a+t+c+g+0.)

print "gc inhoud: " + str(gc)
