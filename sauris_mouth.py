class mouth(object):

    import speech_recognition
    import pyttsx

    #THIS CREATES mouth

    def __init__(self, name):
        self.name = name

    def create_mouth():
        speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
        speech_engine.setProperty('rate', 150)

    def speak(text):
        speech_engine.say(text)
        speech_engine.runAndWait()
