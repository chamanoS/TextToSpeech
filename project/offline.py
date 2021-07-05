import pyttsx3  

# initialize Text-to-speech engine  
engine = pyttsx3.init()  
# convert this text to speech  
text = "Welcome to CareerEra, A python project to convert text to speech. This has been submitted by Chamano Ramashia"  
engine.say(text)  
# play the speech  
engine.runAndWait() 

# get details of speaking rate  
rate = engine.getProperty("rate")  
print(rate)
   
engine.setProperty("rate", 100)  
engine.say(text)  
engine.runAndWait()  

voices = engine.getProperty("voices")  
print(voices)  