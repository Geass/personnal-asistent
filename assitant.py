import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import wikipedia
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import spacy
from googleapiclient.discovery import build

wikipedia.set_lang('pl')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Dzień Dobry, Panie Szymonie")
        print("Dzień Dobry, Panie Szymonie")
    elif hour>=12 and hour<18:
        speak("Dzień Dobry, Panie Szymonie")
        print("Dzień Dobry, Panie Szymonie")
    else:
        speak("Dobry wieczór, Panie Szymonie")
        print("Dobry wieczór, Panie Szymonie")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Słucham...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='pl-PL')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Czy mógłbyś powtórzyć?")
            return "None"
        return statement

print("Łącze się ze światem, prosze daj mi chwilkę...")
speak("Łącze się ze światem, prosze daj mi chwilkę...")
wishMe()

def search(query):
    service = build("customsearch", "v1", developerKey="xxxx")
    result = service.cse().list(q=query, cx="xxxxx").execute()
    return result

def generate_answer(search_results):
    # Load the Polish language model
    nlp = spacy.load('pl_core_news_sm')

    # Process the search results
    answer = ""
    if 'items' in search_results:
        for item in search_results['items']:
            if 'snippet' in item:
                doc = nlp(item['snippet'])
                # Generate the answer using the processed text
                # ...
    return answer

def answer_question(question):
    # Search for the answer
    search_results = search(question)
    # Generate the answer
    answer = generate_answer(search_results)
    # Speak the answer
    speak(answer)

if __name__=='__main__':
    while True:
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "to wszystko" in statement or "dziękuje" in statement or "stop" in statement:
            speak('zamykanie programu')
            print('zamykanie programu')
            break

        if 'wikipedia' in statement:
            speak('Przeszukuje Wikipedie...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'wyszukaj'  in statement:
            statement = statement.replace("wyszukaj", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)	

        elif 'otwórz youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Otwieram Youtube...")
            time.sleep(5)

        elif 'otwórz google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Otwieram Google...")
            time.sleep(5)

        elif 'otwórz gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Otwieram Gmail...")
            time.sleep(5)

        elif 'muzyczka' in statement:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=zi60ZrJj34M")
            speak("Gramy...")
            time.sleep(5)


       
