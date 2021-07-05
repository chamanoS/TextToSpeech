# use google text to speech package(api)
#pip and latest python version
from gtts import gTTS
import os

fh = open("text.txt", "r")
#replace(), replaces the line endings
myText = fh.read().replace("\n", "")

language = 'en'
#make a request
output = gTTS(text=myText, lang=language, slow=False)

output.save("myOutput.mp3")
fh.close()
os.system("start myOutput.mp3")