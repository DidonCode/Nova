import datetime

Alarme = []

def CreateAlarme(Hour):
	Alarme.append(Hour)

def DeleteAlarme(Hour):
	for i in Alarme:
		if i == Hour:
			Alarme.remove(Hour)
			return True
		else:
			return False
	return False

def CheckAlarme():
	DateTime = datetime.datetime.now()

	for i in Alarme:
		Time = str(DateTime.hour) + "h" + str(DateTime.minute)
		TimeExtra = str(DateTime.hour) + "h" + str(DateTime.minute + 1)
		print(i + "  " + Time)
		if i == Time and i < TimeExtra:
			return i
			break
		else:
			return None
	return None

def Date():
	MonthList = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juni", "Juin", "Juillet", "Septembre", "Octobre", "Novembre", "Décembre"]
	DateTime = datetime.datetime.now()
	Date = "Nous somme le " + str(DateTime.day) + " " + MonthList[DateTime.month - 1] + " " + str(DateTime.year) + ", il est " + str(DateTime.hour) + " heure et " + str(DateTime.minute) + " minute"
	return Date