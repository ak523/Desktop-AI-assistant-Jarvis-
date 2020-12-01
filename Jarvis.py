import pyttsx3
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis! Sir please tell me how may I help you?")


def takeCommand():
    # it takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please..")
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('aryanoffialacc@gmail.com','Aryan@2001')
#     server.sendmail('aryanoffialacc@gmail.com',to,content)
#     server.close()


if __name__ == "__main__":
    # speak("Aryan is awesome!")
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")

        elif 'open the code' in query:
            codePath = "C:\\Users\\Aryan Kadiya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open the vlc' in query:
            codePath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(codePath)

        elif 'open the premiere pro' in query:
            codePath = "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2020\\Adobe Premiere Pro.exe"
            os.startfile(codePath)


        # elif 'email to aryan' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand
        #         to = "aryankadiya@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")

        #     except Exception as e:
        #         print(e)
        #         speak("Sorry unable to send email!")

        elif 'shutdown jarvis' in query:
            break
