import pyttsx3


text_speech = pyttsx3.init()


answer = input("Hello we are codingthumbs team . What would u wanna here ...just type..:)  ")

text_speech.say(answer)

text_speech.runAndWait()
