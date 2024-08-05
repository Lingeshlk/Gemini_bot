import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
import google.generativeai as genai
    
def gemini(data):
     genai.configure(api_key="AIzaSyAYemsIDNy4ZIM5ZsHHTspAuXwtuwllIqQ")
     model = genai.GenerativeModel('gemini-pro')
     response = model.generate_content(data)
     print(response.text)
     return response.text

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        # try:
        print("Recognizing...")
        data = recognizer.recognize_google(audio)
        print(data)
        return data
        # except sr.UnknownValueError:
        #     print(" Not Understand")
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    # if sptext().lower() == "hey peter":
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is Tessa"
                speechtx(name)
            elif " old are you " in data1:
                age = 'i am two years old'
                speechtx(age)
            elif 'open notepad' in data1:
                os.system("notepad.exe")
            elif 'open calculator' in data1:
                os.system("calc.exe")
            elif 'open spotify' in data1:
                os.system("C:\\Users\\Asus\\AppData\\Roaming\\Spotify\\Spotify.exe")
            elif 'time ' in data1:
                time = datetime.datetime.now().strftime('%I%M%p')
                speechtx(time)
            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")
            elif data1 in ['quit','exit','bye']:
                break
            else:
                response = gemini(data1)
                print("Chatbot:",response)
                speechtx(response)
            time.sleep(5)
    #         if "your name" in data1:
    #             name = "my name is Tessa"
    #             speechtx(name)
    #         elif " old are you " in data1:
    #             age = 'i am two years old'
    #             speechtx(age)
    #         elif 'time ' in data1:
    #             time = datetime.datetime.now().strftime('%I%M%p')
    #             speechtx(time)
    #         elif 'youtube' in data1:
    #             webbrowser.open("https://www.youtube.com/")
    #         elif "joke" in data1:
    #             joke_1 = pyjokes.get_joke(language="en",category="neutral")
    #             print(joke_1)
    #             speechtx(joke_1)
    #         elif 'play song' in data1:
    #             add = r'C:\Users\Asus\Music\tamil_melody'
    #             listsong = os.listdir(add)
    #             print(listsong)
    #             os.startfile(os.path.join(add,listsong[0]))
    #         elif 'exit' in data1:
    #             print("thank you")
    #             speechtx('thank you')
    #             break
    #         time.sleep(5)

    # # else:
    # #     print("thanks")

