import sauris_ears
import sauris_mouth

#create ear
ear = sauris_ears.ear('sauris_ear')
ear.create_listener()

#create mouth
mouth = sauris_mouth.mouth('sauris_mouth')
mouth.create_mouth()

def get_input(ear):
    text = ear.listen()
    return text

def speak(text):
    mouth.speak(text)

def main():
    input_text=get_input(ear)
    speak(input_text)
