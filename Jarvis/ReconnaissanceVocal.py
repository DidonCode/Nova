from speech_recognition import Recognizer, Microphone

def CheckVoice():
    recognizer = Recognizer()
    with Microphone() as MicrophoneSource:
        recognizer.adjust_for_ambient_noise(MicrophoneSource)
        if MicrophoneSource != None:
            AudioRecorded = recognizer.listen(MicrophoneSource)
            try:
                VoiceText = recognizer.recognize_google(AudioRecorded, language="fr-FR")
                VoiceText = format(VoiceText)
                if "Jack" in VoiceText:
                    return VoiceText
                elif "Jacques" in VoiceText:
                    return VoiceText
            except Exception as ex:
                return None
        else:
            return None
    print(VoiceText)
    return None