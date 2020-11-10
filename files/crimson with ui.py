from PyQt5 import QtWidgets, QtCore
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import ctypes
import datetime
import pyttsx3
import speech_recognition  as sr
import webbrowser
import pywhatkit as kt
import os
import time
import random
from files.dictionary import translate
from files.news  import speak_news
from files.audiobook import playaudiobook
import subprocess

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)


speech = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        # playsound('crimson voice/GoodMorning.mp3')
        speak("Good Morning ")
    elif 12 <= hour <= 18:
        # playsound('crimson voice/Good_Afternoon.mp3')
        speak("Good Afternoon ")
    elif 18 < hour <= 22:
        # playsound('crimson voice/Good_Afternoon.mp3')
        speak("Good Evening ")
    else:
        # playsound('crimson voice/GoodNIght.mp3')
        speak("Good night")

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()


    def run(self):
        self.DIZZI()
    error=0
    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = R.listen(source)
        try:
            print("Recognizing...")
            text = R.recognize_google(audio,language='en-in')

        except Exception:
            speak("Sorry Speak Again")
            return "None"
        return text
    
    def note(text):
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(text)
        subprocess.Popen(["notepad.exe", file_name])

    def DIZZI(self):
        wish_me()
        # playsound('crimson voice/hii_i_m_crimson.mp3')
        speak("hii.. I am Dizzy an Artificial Personal Assistant")

        while True:
            speak("how can i help you")

            qury=self.STT()
            query=qury.lower()

            print('cmd:{}'.format(query))

            if 'hi dizzi' in query or 'hello dizzi' in query :
                print('In open...')
                # playsound(random.choice(mp3_greeting))
                speak("hello sir . Nice to meet you. What about you sir?")

            elif 'open facebook' in query:
                print('In open...')
                speak('ok sir . Got it')
                webbrowser.open("www.facebook.com")

            elif 'open twitter' in query:
                print('In open...')
                speak('Sure sir . Got it')
                webbrowser.open("www.twitter.com")

            elif 'open youtube' in query:
                print('In open...')
                speak("Why not sir..")
                webbrowser.open("www.youtube.com")

            elif 'Program files' in query:
                    os.system('explorer C:\\{}'.format(query.replace('open ', '').replace('launch', ' ')))
                    speak("opening explorer for you")
                    print('explorer C:\\{}'.format(query.replace('open ', '')))
                    continue

            elif 'who' in query or  'what' in query or 'which' in query or 'where' in query or 'how' in query:
                print('Searching on google...')
                speak("let me search it on google for you")
                webbrowser.open('https://www.google.com/search?q={}'.format(query))

            elif 'lock' in query:
                for value in ['pc', 'system', 'pc', 'windows']:
                    speak("Processing Command sir. Wait for a while please")
                    ctypes.windll.user32.LockWorkStation()

            elif "play random song" in query or "play random music " in query or "play some music " in query:
                music_dir = "D:\\Songs\\favourite"
                songs = os.listdir(music_dir)
                leng = int(len(songs))
                speak("Playing Music ... ")
                os.startfile(os.path.join(music_dir, songs[random.randint(0, leng - 1)]))

            elif "play song" in query or "play some music " in query:
                speak("Which song do you want to play sir ?")
                music = self.read_voice()
                speak("Playing Music ... ")
                kt.playonyt(music)

            elif "today's news " in query or "news headlines" in query or "news" in query:
                speak("Sure sir")
                speak_news()

            elif 'dictionary' in query:
                speak('What you want to search in your intelligent dictionary?')
                element = self.read_voice()
                translate(element)

            elif "play some audiobook" in query:
                playaudiobook()

            elif "make a note" in query or "write this down" in query or "write this to notes" in query:
                speak("What would you like me to write down ?")
                note_text = self.read_voice()
                self.note(note_text)
                speak("Note successfully created")


            elif 'thank you' in query:
                speak("Mention not sir ! I am here for you only ")
                print("always welcome")

            elif 'by' in query:
                speak("bye sir!.have  a great time. See you soon sir !!")
                wish_me()
                exit()


FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow, FROM_MAIN):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1366,768)
        self.label_7 = QLabel
        self.label_30=QLabel
        self.graph1=QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n"
                                 "border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)

        Dspeak = mainT()

        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.graph1 = QMovie("./lib/pie chart.gif", QByteArray(), self)
        self.graph1.setCacheMode(QMovie.CacheAll)
        self.graph.setMovie(self.graph1)
        self.graph1.start()

        self.ts = time.strftime("%A, %d %B")

        t = time.localtime()
        self.tm = time.strftime("%H:%M:%S", t)



        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>" + self.ts + "</font>")
        self.label_5.setFont(QFont(QFont('Acens', 12)))

        self.label_3.setText("<font size=8 color='white'>" +" Time is : "+self.tm + "</font>")
        self.label_3.setFont(QFont(QFont('Acens', 12)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())