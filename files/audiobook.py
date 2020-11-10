import pyttsx3
import random
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate=engine.getProperty('rate')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',180)

path1=os.getcwd()
urls=[path1+'\story1.txt',path1+'\story2.txt']

book=open(urls[random.randint(0,1)],'r')

a=book.read()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def playaudiobook():
    speak(a)