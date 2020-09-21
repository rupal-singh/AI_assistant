import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import sys
import pyaudio
import datetime

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
        speak("I am Jesica. Please tell me how may I help you Ma'am.")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        speak("I am Jesica. Please tell me how may I help you Ma'am.")
    else:
        speak("Good Evening")
        speak("I am Jesica. Please tell me how may I help you Ma'am.")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 0.8
        r.energy_threshold = 900
        audio= r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')            
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please.....")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query= takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia........')
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("http://youtube.com")
        elif 'open google' in query:
            webbrowser.open("http://google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("http://stackoverflow.com")
        elif 'open gmail' in query:
            webbrowser.open("http://gmail.com")
        elif 'play music' in query:
            music_dir='C:\\Users\\Rupal\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")
        elif 'open VS' in query:
            codePath = "C:\\Users\\Rupal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open video' in query:
            video_dir='C:\\Users\\Rupal\\Videos\\Captures\\Hollywood\\Harry Potter All Movies Collection (2001-2011)'
            vid = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, vid[0]))
        elif 'where is' in query:
            query = query.split(" ")
            location = query[2]
            speak("Hold on, I will show you where" +location+ "is.")
            webbrowser.open("http://www.google.com/maps/place/"+location)   
        elif 'exit' in query:
            sys.exit(0)
