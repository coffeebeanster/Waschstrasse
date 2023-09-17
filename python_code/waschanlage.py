#!/usr/bin/python3
import RPi.GPIO as GPIO			# Library für GPIO
from termcolor import cprint		# Library für Textfärbung
import time
import os
clear = os.system('clear')		# Bildschirm bei Start des Programmes löschen
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)			# Eingänge festlegen
GPIO.setup(3, GPIO.IN)
GPIO.setup(4, GPIO.IN)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(7, GPIO.OUT)			# Ausgänge festlegen
GPIO.setup(8, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.output(7, GPIO.LOW)		# Initialzustände der Ausgänge auf LOW
GPIO.output(8, GPIO.LOW)
GPIO.output(12, GPIO.LOW)
GPIO.output(14, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(20, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
# Definition der Waschprogramme
# Vollwäsche
def vollwaesche():
	vollwaeschefertig = False
	arbeitstakt = 0
	lappentraegerrichtung = 0
	gewartet = False
	gedruckt = False
	cprint("Warte auf Positionierung des Fahrzeuges", "white", "on_blue")
	while vollwaeschefertig == False:
		# Code für Vollwaesche
		while arbeitstakt == 0:
			if GPIO.input(10):
				arbeitstakt = 10
			if GPIO.input(4):
				GPIO.output(14, GPIO.HIGH)
				GPIO.output(15, GPIO.LOW)
				cprint("Vollwäsche startet...", "white", "on_blue")
				arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 1:
			if GPIO.input(10):
				arbeitstakt = 10
			if gewartet == False:
				time.sleep(5)
				cprint("Auto wird vorgewaschen...", "white", "on_blue")
				gewartet = True
			GPIO.output(8, GPIO.HIGH)		# Band zuschalten
			GPIO.output(25, GPIO.HIGH)		# Wasser zuschalten
			if lappentraegerrichtung == 0:		# Lappenträger nach links bewegen
				GPIO.output(24, GPIO.LOW)
				GPIO.output(23, GPIO.HIGH)
			if lappentraegerrichtung == 1:		# Lappenträger nach rechts bewegen
				GPIO.output(23, GPIO.LOW)
				GPIO.output(24, GPIO.HIGH)
			if GPIO.input(2):
				lappentraegerrichtung = 1
			if GPIO.input(3):
				lappentraegerrichtung = 0
			if GPIO.input(27):
				arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 2:
			if GPIO.input(10):
				arbeitstakt = 10
			if lappentraegerrichtung == 0:		# Lappenträger nach links bewegen
				GPIO.output(24, GPIO.LOW)
				GPIO.output(23, GPIO.HIGH)
			if lappentraegerrichtung == 1:		# Lappenträger nach rechts bewegen
				GPIO.output(23, GPIO.LOW)
				GPIO.output(24, GPIO.HIGH)
			if GPIO.input(2):
				lappentraegerrichtung = 1
			if GPIO.input(3):
				lappentraegerrichtung = 0
			GPIO.output(7, GPIO.HIGH)		# Bürsten zuschalten
			if not gedruckt:
				cprint("Hauptwaschgang gestartet...", "white", "on_blue")
				gedruckt = True
			if GPIO.input(22):
				gedruckt = False
				arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 3:
			if GPIO.input(10):
				arbeitstakt = 10
			GPIO.output(23, GPIO.LOW)		# Lappenträger ausschalten
			GPIO.output(24, GPIO.LOW)
			GPIO.output(25, GPIO.LOW)		# Wasser ausschalten
			if not gedruckt:
				cprint("Fahrzeug wird getrocknet...", "white", "on_blue")
				gedruckt = True
			GPIO.output(12, GPIO.HIGH)		# Lüfter zuschalten
			if GPIO.input(17):
				gedruckt = False
				arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 4:
			if GPIO.input(10):
				arbeitstakt = 10
			GPIO.output(8, GPIO.LOW)		# Band ausschalten
			GPIO.output(7, GPIO.LOW)		# Bürsten ausschalten
			if not gedruckt:
				cprint("Bitte fahren Sie vom Laufband.", "white", "on_blue")
				gedruckt = True
			gedruckt = False
			arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 5:
			if GPIO.input(10):
				arbeitstakt = 10
			if not GPIO.input(17):
				time.sleep(1)
				GPIO.output(12, GPIO.LOW)
				cprint("Waschvorgang abgeschlossen. Vielen Dank und einen schönen Tag!", "white", "on_blue")
				time.sleep(5)
				vollwaeschefertig = True
				arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 10:			# Not-Aus-Takt
			GPIO.output(7, GPIO.LOW)		# Alle Ausgänge auf LOW schalten
			GPIO.output(8, GPIO.LOW)
			GPIO.output(12, GPIO.LOW)
			GPIO.output(15, GPIO.LOW)
			GPIO.output(16, GPIO.LOW)
			GPIO.output(20, GPIO.LOW)
			GPIO.output(21, GPIO.LOW)
			GPIO.output(23, GPIO.LOW)
			GPIO.output(24, GPIO.LOW)
			GPIO.output(25, GPIO.LOW)
			os.system('clear')
			cprint("NOT-AUS betätigt!!!", "yellow", "on_red")
			print("")
			arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 11:
			cprint("Zum Quittieren [ENTER] drücken...", "white", "on_blue")
			dump = input("")
			vollwaeschefertig = True
			arbeitstakt = arbeitstakt + 1
def katzenwaesche():
	katzenwaeschefertig = False
	arbeitstakt = 0
	lappentraegerrichtung = 0
	gewartet = False
	gedruckt = False
	cprint("Warte auf Positionierung des Fahrzeuges", "white", "on_blue")
	while katzenwaeschefertig == False:
		# Code für Katzenwaesche
		while arbeitstakt == 0:
			if GPIO.input(10):
				arbeitstakt = 10
			if GPIO.input(4):
				GPIO.output(14, GPIO.HIGH)
				GPIO.output(15, GPIO.LOW)
				cprint("Katzenwäsche startet...", "white", "on_blue")
				arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 1:
			if GPIO.input(10):
				arbeitstakt = 10
			if gewartet == False:
				time.sleep(5)
				cprint("Auto wird gewaschen...", "white", "on_blue")
				gewartet = True
			GPIO.output(8, GPIO.HIGH)		# Band zuschalten
			GPIO.output(25, GPIO.HIGH)		# Wasser zuschalten
			if lappentraegerrichtung == 0:		# Lappenträger nach links bewegen
				GPIO.output(24, GPIO.LOW)
				GPIO.output(23, GPIO.HIGH)
			if lappentraegerrichtung == 1:		# Lappenträger nach rechts bewegen
				GPIO.output(23, GPIO.LOW)
				GPIO.output(24, GPIO.HIGH)
			if GPIO.input(2):
				lappentraegerrichtung = 1
			if GPIO.input(3):
				lappentraegerrichtung = 0
			if GPIO.input(22):
				cprint("Fahrzeug wird getrocknet...", "white", "on_blue")
				arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 2:
			if GPIO.input(10):
				arbeitstakt = 10
			GPIO.output(25, GPIO.LOW)		# Wasser abschalten
			GPIO.output(23, GPIO.LOW)		# Lappenträger ausschalten
			GPIO.output(24, GPIO.LOW)
			GPIO.output(12, GPIO.HIGH)		# Heizungslüfter zuschalten
			if GPIO.input(17):
				arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 3:
			if GPIO.input(10):
				arbeitstakt = 10
			GPIO.output(8, GPIO.LOW)		# Band abschalten
			if not gedruckt:
				cprint("Bitte fahren Sie vom Laufband.", "white", "on_blue")
				gedruckt = True
			gedruckt = False
			arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 4:
			if GPIO.input(10):
				arbeitstakt = 10
			if not GPIO.input(17):
				time.sleep(1)
				GPIO.output(12, GPIO.LOW)
				cprint("Waschvorgang abgeschlossen. Vielen Dank und einen schönen Tag!", "white", "on_blue")
				time.sleep(5)
				katzenwaeschefertig = True
				arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 10:			# Not-Aus-Takt
			GPIO.output(7, GPIO.LOW)		# Alle Ausgänge auf LOW schalten
			GPIO.output(8, GPIO.LOW)
			GPIO.output(12, GPIO.LOW)
			GPIO.output(15, GPIO.LOW)
			GPIO.output(16, GPIO.LOW)
			GPIO.output(20, GPIO.LOW)
			GPIO.output(21, GPIO.LOW)
			GPIO.output(23, GPIO.LOW)
			GPIO.output(24, GPIO.LOW)
			GPIO.output(25, GPIO.LOW)
			os.system('clear')
			cprint("NOT-AUS betätigt!!!", "yellow", "on_red")
			print("")
			arbeitstakt = arbeitstakt + 1
		while arbeitstakt == 11:
			cprint("Zum Quittieren [ENTER] drücken...", "white", "on_blue")
			dump = input("")
			katzenwaeschefertig = True
			arbeitstakt = arbeitstakt + 1
# Hauptprogramm
while True:
	GPIO.output(14, GPIO.HIGH) # Ampel bei Programmstart in Betrieb nehmen und auf rot schalten
	cprint("HTWK Waschanlagen Services", "white", "on_blue")
	cprint("--------------------------", "white", "on_blue")
	print("")
	cprint("Auswahl von zwei verschiedenen Waschprogrammen möglich: \"Katzenwäsche\" und \"Vollwäsche\".", "red", "on_blue")
	print("")
	cprint("Katzenwäsche: Fahrzeug abspülen und trocknen", "yellow")
	cprint("Vollwäsche: Fahrzeug abspülen, bürsten und trocknen", "green")
	print("")
	cprint("(K)atzenwäsche oder (V)ollwäsche?", "red", "on_blue")
	escape = False
	programmwortlaut = "Kein Programm"
	while escape == False:
		waschprogramm = input("--> ")
		print("")
		if waschprogramm == "k" or waschprogramm == "K":
			programmwortlaut = "Katzenwäsche"
			escape = True
		elif waschprogramm == "v" or waschprogramm == "V":
			programmwortlaut = "Vollwäsche"
			escape = True
		else:
			cprint("\"k\" für Katzenwäsche oder \"v\" für Vollwäsche eingeben!", "red")
	cprint(programmwortlaut + " wurde ausgewählt.", "white", "on_blue")
	GPIO.output(14, GPIO.LOW)
	GPIO.output(15, GPIO.HIGH)
	print("")
	cprint("Bitte fahren Sie bis zur Markierung vor. Stellen Sie danach den Motor ab und ziehen Sie die Handbremse an.", "white", "on_blue")
	cprint("Während der Fahrt Fenster und Türen geschlossen halten!!!", "red")
	if programmwortlaut == "Vollwäsche":
		vollwaesche()
	if programmwortlaut == "Katzenwäsche":
		katzenwaesche()
	os.system('clear')
