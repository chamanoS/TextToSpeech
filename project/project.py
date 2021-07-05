from gtts import gTTS
import os

fh = open("text.txt", "r")
myText = fh.read().replace("\n","")
language = 'en'
output = gTTS(text=myText, lang=language, slow=False)

output.save("myOutput.mp3")
fh.close()
os.system("start myOutput.mp3")