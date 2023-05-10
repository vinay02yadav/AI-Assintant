import pyttsx3
import webbrowser
import smtplib
import random
import configparser
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)


def speak(audio):
    print('Ultron: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('02vyadav@gmail.com', 'vinay02@')
    server.sendmail('02vyadav@gmail.com', to, content)
    server.close()


greetMe()
speak('Hello, I am Ultron!')
speak('How may I help you?')


def myCommand():

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        r.non_speaking_duration = 0.5
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! I did not get that! Try typing the command!')
        query = str(input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "stop" in query:
            speak("quitting sir")
            quit()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif "shut down" in query:
            os.system('shutdown -s')

        elif "shutdown" in query:
            os.system('shutdown -s')

        elif "who are you" in query:
            speak("I am Ultron an artificial intelligence. my owner is vinay. speed 1 terahertz , memory 1 terabyte .")

        elif "tell me about yourself" in query:
            speak(
                "I am Ultron an artificial intelligence. mmade by vinay. speed 1 terahertz , memory unlimited .")

        elif "hello" in query:
            speak("hi , I am good whats about you")

        elif "fine" in query:
            speak("thats great,how may i help you")

        elif 'play music' in query:
            music_dir = 'D:\\music\\'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "who is arnav" in query:
            speak(
                "arnav is tatti , pagal , mental guy. he is also known as shiv bidi and anda.")
            print(
                "arnav is tatti , pagal , mental guy. he is also known as shiv bidi and anda.")

        elif "who is pashu" in query:
            print("pashu lived in manesar. but nowadays he is living in vinays house")
            speak("pashu lived in manesar. but nowadays he is living in vinays house")

        elif "who is Pashu" in query:
            print("pashu lived in manesar. but nowadays he is living in vinays house")
            speak("pashu lived in manesar. but nowadays he is living in vinays house")

        elif "who is aditya" in query:
            print("aditya also known as padamtatti. ye pure din me padta hi rahta hai.")
            speak("aditya also known as padamtatti. ye pure din me padta hi rahta hai.")

        elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open visual studio code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'google' or 'GOOGLE' in query:
            speak("yes sir")

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = myCommand()
                to = "02vyadav@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir , I am not able to send this email")
