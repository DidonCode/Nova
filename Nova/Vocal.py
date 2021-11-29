import threading

from speech_recognition import Recognizer, Microphone
import speech_recognition as sr

import Voice

import Web
import Music
import Horloge

IA_Name = "nova"

class vocalThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		with Microphone() as source:
			r = sr.Recognizer()
			while True:
				audio_data = r.listen(source)
				try:
					result = r.recognize_google(audio_data, language="fr-FR")

					if result != None:
						command(result)
						result = None
					print("oui")
				except Exception as ex:
					print("loop")

def command(voiceText):
	print("> " + voiceText)

	if IA_Name in voiceText:
		if "recherche" in voiceText:
			voiceText = voiceText.replace(IA_Name + " recherche ", '')

			global WebClass
			WebClass = Web.infow()
			WebClass.get_info(voiceText)
			WebClass.read()

		if "lance" in voiceText:
			voiceText = voiceText.replace(IA_Name + " lance ", '')
			Voice.Speak("Voici la video " + voiceText)

			global MusicClass
			MusicClass = Music.music()
			MusicClass.play(voiceText)

		if "pause" in voiceText:
			MusicClass.pause()

		if "ferme" in voiceText:
			if MusicClass != None:
				MusicClass.close()
				MusicClass = None

			if WebClass != None:
				WebClass.close()
				WebClass = None

			Voice.Speak("La fenétre a été fermé")

		if "donne-moi la date" in voiceText:
			Voice.Speak(Horloge.Date())

		if "mets une alarme pour " in voiceText:
			voiceText = voiceText.replace(IA_Name + " mets une alarme pour ", '')
			Voice.Speak("L'alarme a bien été crée")
			Horloge.CreateAlarme(voiceText)

		if "enleve l'alarme de " in voiceText:
			voiceText = voiceText.replace(IA_Name + " enleve l'alarme de ", '')
			if Horloge.DeleteAlarme(voiceText) == True:
				Voice.Speak("L'alarme a bien été enlevé")
			else:
				Voice.Speak("Cet alarme n'existe pas")

		if "combien fait" in voiceText:
			voiceText = voiceText.replace(IaName + " combien fait ", '')
			voiceText = voiceText.replace("x", '*')
			voiceText = voiceText.replace("puissance", '**')
			Calcul = str(eval(voiceText))
			Voice.Speak(voiceText + " fait " + Calcul)