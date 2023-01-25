from gtts import gTTS
from playsound import playsound

mytext = "Welcome to the jungle!"
myobj = gTTS(text=mytext, lang="en", tld="co.uk")
myobj.save("/mnt/c/Users/Red/Desktop/Coding/Projects/Wikipedia-Aloud/welcome.mp3")
