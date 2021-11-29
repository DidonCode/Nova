import Vocal
import Voice
import Horloge

# Voice.Speak("Bonjours Monsieur") # Bonjours Monsieur que puis-je faire pour vous

m = Vocal.vocalThread()
m.start()

while True:
	alarme = Horloge.CheckAlarme()

	if alarme != None:
		Voice.Speak("L'alarme de " + alarme + " sonne")
		print("alarme")

	pass