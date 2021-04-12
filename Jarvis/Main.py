import webbrowser
import re

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from robobrowser import RoboBrowser

from googletrans import Translator

import os

import ReconnaissanceVocal
import Voice
import Horloge
import Interface

Init = True
IaName = "Jack"

print("Starting...")

Voice.Speak("Bonjours Monsieur")

def CheckWord(VoiceText):
    print(">" + VoiceText)
    if "zéro" in VoiceText:
        VoiceText = VoiceText.replace("zéro", '0')

    if "redémarre" in VoiceText:
        exec(open("Main.py").read())
        exit()

    if "arrêt" in VoiceText:
        Voice.Speak("Enrevoir Monsieur")
        exit()

    if "lance-moi" in VoiceText:
        VoiceText = VoiceText.replace(IaName + " lance-moi ", '')
        webbrowser.open('https://www.' + VoiceText + '/')
        Voice.Speak("Voici " + VoiceText)

    if "donne-moi la date" in VoiceText:
        Voice.Speak(Horloge.Date())

    if "combien fait" in VoiceText:
    	VoiceText = VoiceText.replace(IaName + " combien fait ", '')
    	VoiceText = VoiceText.replace("x", '*')
    	VoiceText = VoiceText.replace("puissance", '**')
    	Calcul = str(eval(VoiceText))
    	print(">" + Calcul)
    	Voice.Speak(VoiceText + " fait " + Calcul)

    if "mets une alarme pour" in VoiceText:
    	VoiceText = VoiceText.replace(IaName + " mets une alarme pour ", '')
    	Voice.Speak("Une alarme a était mise pour " + VoiceText)
    	Horloge.CreateAlarme(VoiceText)

    if "enlève l'alarme de" in VoiceText:
    	VoiceText = VoiceText.replace(IaName + " enlève l'alarme de ", '')
    	if Horloge.DeleteAlarme(VoiceText) == True:
    		Voice.Speak("L'alarme de " + VoiceText + " a était enlever")
    	else:
    		Voice.Speak("L'alarme de " + VoiceText + " n'existe pas")
	
    if "lance l'interface" in VoiceText:
    	Voice.Speak("d'accord Monsieur je vous lance l'interface")
    	Interface.StartInterface()

    if "ouvre" in VoiceText:
    	VoiceText = VoiceText.replace(IaName + " ouvre ", '')
    	Path = "C:\'Users\'Richard\'Desktop\'TruckersMP.inc"
    	os.startfile(Path)

    if "recherche" in VoiceText:
        VoiceText = VoiceText.replace(IaName + " recherche ", '')

        # br = RoboBrowser()

        # br.open('https://www.google.com/search?q=' + VoiceText)
        webbrowser.open('https://www.google.com/search?q=' + VoiceText)
        # src = str(br.parsed())

        # start = '<div class="kno-rdesc"><div><span>Le'
        # end = '</div></div></span>'

        # ResearchResult = re.search('%s(.*)%s' % (start, end), src).group(1)

        Voice.Speak("Voici ce que j'ai trouvé sur " + VoiceText)# + " " + ResearchResult

    if "comment on dit" in VoiceText:
    	# VoiceText = VoiceText.replace(IaName + " en ", '')
    	# VoiceText = VoiceText.replace("comment on dit ", '')

    	# VoiceSplit = VoiceText
    	# VoiceSplit = VoiceSplit.split()

    	# if VoiceSplit[0] == "espagnol":
    	# 	Langue = "es"
    	# elif VoiceSplit[0] == "anglais":
    	# 	Langue = "en"
    	# else:
    	# 	Langue = ""
    	# 	pass

    	# VoiceTextTrading = VoiceText
    	# VoiceTextTrading = VoiceText.replace(VoiceSplit[0] + " ", '')

    	# print(VoiceText)
    	# print(Langue)
    	# print(VoiceTextTrading)

        translator = Translator()
        result = translator.translate('Mikä on nimesi', src='fi', dest='fr')

        print(result.src)
        print(result.dest)
        print(result.text)
    	# Voice.Speak(Translated.text)


while Init:
	Alarme = Horloge.CheckAlarme()
	if Alarme != None:
		Voice.Speak("Monsieur l'alarme de " + Alarme + " sonne")

	Vocal = ReconnaissanceVocal.CheckVoice()
	if Vocal != None:
		CheckWord(Vocal)

	print("Loop")