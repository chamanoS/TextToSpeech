# use google text to speech package(api)
#pip and latest python version
from gtts import gTTS
import os

#read and convert text file to speech
fh = open("text.txt", "r")
#replace(), replaces the line endings
myText = fh.read().replace("\n", "")

#choose a language support(english)
language = 'en'
#slow=false means play fast
output = gTTS(text=myText, lang=language, slow=False)

#save and name your output file
output.save("myOutput.mp3")
fh.close()#closes the file handlers
os.system("start myOutput.mp3")