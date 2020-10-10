import pyttsx3
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate=engine.getProperty('rate')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate',180)

urls=['D:\FFOutput\Projects\Crimson\\files\stories\story1.txt','D:\FFOutput\Projects\Crimson\\files\stories\story2.txt']

book=open(urls[random.randint(0,1)],'r')

a=book.read()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def playaudiobook():
    speak(a)