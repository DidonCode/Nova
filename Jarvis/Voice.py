import pyttsx3

import datetime

SpeakSpeed = 140

engine = pyttsx3.init()
AllVoices = engine.getProperty('voices')

def Speak(Text):
    engine.setProperty("voice", "french")
    engine.setProperty("rate", SpeakSpeed)
    engine.say(Text)
    engine.runAndWait()