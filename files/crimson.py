import ctypes
import datetime
import pyttsx3
import speech_recognition  as sr
import webbrowser
import pywhatkit as kt
import os
import random
from files.dictionary import translate
from files.news  import speak_news
from files.audiobook import playaudiobook


speech = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',190)


greet_dict = {'Hello': 'Hello', 'Hi': 'Hi'}
open_launch_dict = {'open': 'open', 'launch': 'launch'}
social_media_dict = {'facebook': 'www.facebook.com', 'twitter': 'www.twitter.com', 'youtube': 'www.youtube.com'}
google_search_dict = {'what': 'what', 'who': 'who', 'why': 'why', 'which': 'which', 'where': 'where'}

# audio_lists
greetings = ['hello']
mp3_listening_problem = ['i am unable to get you.Please say it again','Sorry i am unable to get You']
processing_audio=['sure sir','ok sir','got it sir']
thanks_audio=["it's been a great time with you. i am always here to help you"]
bye_audio=['bye sir!.have  a great time','see you soon sir','i am always happy to help you']

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

error = 0

def read_voice():
    voice_text = ''
    global error
    print('Listening....')
    try:
        with sr.Microphone() as source:
            speech.pause_threshold = 1
            speech.energy_threshold = 494
            speech.adjust_for_ambient_noise(source, duration=1.5)
            audio = speech.listen(source)
            voice_text = speech.recognize_google(audio,language='en-in')
    except sr.UnknownValueError:
        if error == 0:
            # playsound(mp3_listening_problem)
            print('problem')
            speak(mp3_listening_problem[random.randint(0,2)])
            error += 1
        elif error == 1:
            print('struggling')
            # playsound(mp3_struggling)
            speak(mp3_listening_problem[random.randint(0,2)])
            error += 1
    except sr.WaitTimeoutError:
        if error == 0:
            # playsound(mp3_listening_problem)
            print('problem')
            speak(mp3_listening_problem[random.randint(0, 2)])
            error += 1
        elif error == 1:
            print('struggling')
            # playsound(mp3_struggling)
            speak(mp3_listening_problem[random.randint(0, 2)])
            error += 1
    except sr.RequestError:
        print('network error')
    return voice_text


def is_valid_note(greet_dict, voice_note):
    for key, value in greet_dict.items():
        try:
            if value == voice_note.split(' ')[0]:
                return True

            elif key == voice_note.split(' ')[1]:
                return True

        except IndexError:
            pass
    return False


def is_valid_google_search(phrase):
    if (google_search_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        # playsound('crimson voice/GoodMorning.mp3')
        speak("Good Morning ")
    elif 12 < hour <= 18:
        # playsound('crimson voice/Good_Afternoon.mp3')
        speak("Good Afternoon ")
    elif 18 < hour <= 22:
        # playsound('crimson voice/Good_Afternoon.mp3')
        speak("Good Evening ")
    else:
        # playsound('crimson voice/GoodNIght.mp3')
        speak("Good night")



if __name__ == "__main__":
    wish_me()
    # playsound('crimson voice/hii_i_m_crimson.mp3')
    speak("hii. I am Dizzy an Artificial Personal Assistant")
    speak("how can i help you")
    while True:
        voice_note = read_voice().lower()
        print('cmd:{}'.format(voice_note))
        if is_valid_note(greet_dict, voice_note):
            print('In open...')
            # playsound(random.choice(mp3_greeting))
            speak("hello sir . Nice to meet you. What about you sir?")

        elif is_valid_note(open_launch_dict, voice_note):
            print('In open...')
            speak(processing_audio[random.randint(0,len(processing_audio)-1)])
            if is_valid_note(social_media_dict, voice_note):
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('explorer C:\\{}'.format(voice_note.replace('open ', '').replace('launch', ' ')))
                speak("opening explorer for you")
                print('explorer C:\\{}'.format(voice_note.replace('open ', '')))
                continue
        elif is_valid_google_search(voice_note):
            print('Searching on google...')
            speak("let me search it on google for you")
            webbrowser.open('https://www.google.com/search?q={}'.format(voice_note))

        elif 'lock' in voice_note:
            for value in ['pc', 'system', 'pc', 'windows']:
                speak(processing_audio[random.randint(0, len(processing_audio) - 1)])
                ctypes.windll.user32.LockWorkStation()

        elif "play random song" in voice_note or "play random music " in voice_note or "play some music " in voice_note:
            music_dir="D:\\mobile\\favourite"
            songs=os.listdir(music_dir)
            leng=int(len(songs))
            speak("Playing Music ... ")
            os.startfile(os.path.join(music_dir,songs[random.randint(0,leng-1)]))

        elif "play song" in voice_note or "play some music " in voice_note:
            speak("Which song do you want to play sir ?")
            kt.playonyt(voice_note)

        elif "today news " in voice_note or "news headlines" in voice_note or "news" in voice_note:
            speak(processing_audio[random.randint(0,len(processing_audio)-1)])
            speak_news()

        elif 'dictionary' in voice_note:
            speak('What you want to search in your intelligent dictionary?')
            translate(voice_note)

        elif "play some audio book for me" in voice_note:
            playaudiobook()

        elif 'thank you' in voice_note:
            speak(thanks_audio)
            print("always welcome")

        elif 'by' in voice_note:
            speak(bye_audio[random.randint(0,len(bye_audio)-1)])
            wish_me()
            exit()
