import pytesseract


from PIL import Image


import pyttsx3


from googletrans import Translator


img = Image.open("bill3.png")


print(img)

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\Tesseract.exe'

result = pytesseract.image_to_string(img)

with open('abc.txt', mode='w') as file:
    file.write(result)
    print(result)

p = Translator()

k = p.translate(result, dest='english')
print(k)
engine = pyttsx3.init()


engine.say(k)
engine.runAndWait()
