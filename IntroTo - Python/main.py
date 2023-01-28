# copyrights reserved to vivek thakur | vivek1kumar2thakur@gmail.com
from ast import Try
from asyncio import queues
from email.mime import audio
from http import client
from logging import shutdown
import shutil
import smtplib
from unittest import result
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import os
import sys
import time
import subprocess
import pywhatkit as kit
import pyautogui as key
import openai
from googletrans import Translator


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening........")
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)
        print("unable to recognize")
        return "none"

    return query

def translateData(Text):
    try :
        line = str(Text)
        translator = Translator()
        translated = translator.translate(line, to_language='en-in')
        print(f"You Said : {translated.text}")
        return translated.text
    except Exception as e:
        print(e)
        print("unable to translate")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("A warm Good Morning boss ")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon boss ")
    else:
        speak("Good Evening boss")


def sendMsg(num, message):
    try:
        speak("what should i say boss")
        kit.sendwhatmsg_instantly(num, message)
    except Exception as e:
        print(e)


def pressKey(key1, key2):
    try:
        key.hotkey(key1, key2)
    except Exception as e:
        print(e)


def get_connected_devices():
    output = subprocess.run(
        ['arp', '-a'], stdout=subprocess.PIPE).stdout.decode()
    lines = output.split('\n')
    devices = []
    for line in lines:
        words = line.split()
        if len(words) == 3:
            ip_address = words[0]
            mac_address = words[1]
            devices.append((ip_address, mac_address))
    return devices


if __name__ == "__main__":
    
    def clear(): return os.system('cls')
    clear()

    while True:
        command = takeCommand()
        query = translateData(command).lower()
        query.replace("saturday", "").lower().replace("umm", "").replace("hmm", "").replace("ammmm", "")

        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia......')
                query = query.replace("saturday", "").replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=4)
                speak("Boss! According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("sorry boss i didnt find any information about it")
        # wakeup
        elif 'wakeup' in query or 'are you online' in query:
            speak("online boss")
            wishme()       
        # Browsing the internet
        elif 'open youtube' in query:
            speak("okay boss")
            webbrowser.open("www.youtube.com")
        elif 'open google' in query or 'search on google' in query:
            speak("okay boss ")
            speak("what should i search boss?")
            webbrowser.open("www.google.com")
            query = query.replace("search", "")
            webbrowser.open(query)
        elif 'open instagram' in query or 'check my instagram ' in query:
            speak("boss here is you IG ")
            webbrowser.open("www.instagram.com")
        elif 'look at my facebook' in query or 'open facebook' in query:
            speak(" boss here is you FB ")
            webbrowser.open("www.facebook.com")
        elif 'check my whatsapp' in query or 'open whatsapp' in query or 'whatsapp' in query:
            speak("sure boss")
            webbrowser.open("web.whatsapp.com")
        elif 'open github ' in query or 'check my github' in query:
            speak("Okay Boss I am opening your GitHub ")
            webbrowser.open("www.github.com")
        elif 'stackoverflow' in query:
            speak("Here you go to stackoverflow ")
            webbrowser.open("stackoverflow.com")
        elif 'Pinterest' in query:
            speak("I am look at your pinterest")
            webbrowser.open("www.pinterest.com")
        elif 'open twitter' in query or 'look at my twitter' in query:
            speak("okay boss as you say")
            webbrowser.open("www.twitter.com")
        elif 'any emails' in query or 'have i got any email' in query or 'check my inbox' in query:
            speak("wait boss  let me check")
            webbrowser.open("www.gmail.com")
        elif 'open gmail' in query or 'do i have any mail' in query or 'check my mailbox' in query:
            speak("wait a second boss")
            webbrowser.open("www.gmail.com")

        # Browser Automation
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("Boss here is the location of")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/"+location+"")
        elif 'search' in query:
            query = query.replace("search", "").replace("about", "")
            kit.search(query)
        elif 'play' in query or 'songs' in query or 'song' in query:
            query = query.replace("play", "")
            kit.playonyt(query)
        elif 'hit some music' in query or 'play a playlist' in query:
            webbrowser.open("https://www.youtube.com/playlist?list=PL1vn5tgOq_leTAH5RKUbX6mC_1T2sgsVK")

        # Current time displaying function
        elif 'time' in query or 'whats the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir Its{strTime}")

        # WhatsApp Message Automation
        elif 'message to pandey' in query or 'message to pande' in query:
            num = "+91 8292747763"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to dainwi' in query:
            num = "+91 9905308845"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to anshu' in query:
            num = "+91 9334384975"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to aditya' in query or 'message to addi' in query:
            num = "+91 79924 47995"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to arya' in query:
            num = "+91 6203248782"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to aman' in query:
            num = "+91 7488166428"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to rahul bhaiya' in query:
            num = "+91 8002030975"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to ashish bhaiya' in query:
            num = "+91 9304679355"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to shamma' in query or 'message to my lifeline' in query:
            num = "+91 7004796612"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to mummy' in query or 'message to my mom' in query:
            num = "+91 6201702236"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to my sister' in query:
            num = "+91 9955030944"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to chasmish' in query or 'message to nandini' in query or 'message to nandani' in query:
            num = "+91 8114552003"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
        elif 'message to vivek' in query:
            num = "+91 6299902752"
            message = takeCommand().lower().replace("say", "").replace("tell", "")
            sendMsg(num, message)
            
            
        # System Automation
        elif 'close this tab' in query or 'exit tab' in query or 'close tab' in query or 'close it' in query or 'close' in query:
            pressKey('ctrl', 'w')
        elif 'closed this tab' in query or 'closed tab' in query or 'closed it' in query or 'closed' in query:
            pressKey('ctrl', 'w')
        elif 'closed this app' in query or 'closed app' in query or 'close this app' in query or 'close this application' in query or 'closed this application' in query:
            pressKey('Alt', 'f4')
        elif 'refresh this tab' in query or 'refresh tab' in query or 'refresh it' in query :
            pressKey('ctrl' , 'R')
        elif 'select all' in query or 'select' in query :
            pressKey('ctrl', 'A')
        elif 'copy this tab' in query or 'copy tab' in query or 'copy' in query :
            pressKey('ctrl', 'C')
        # elif 'open text file' in query or 'open file' in query or 'open' in query :
            # os.startfile("C:/Users/hp/Desktop/VS 2306/Saturday-Update-001/unused.txt")
            # 
        # elif 'record' in query or 'start recording' in query or 'screen recorder' in query:
        #     pressKey('Windows', 'Alt', 'R')

        # Shutdown the System
        elif 'good night' in query or 'shutdown the system' in query:
            speak("good night boss")
            os.system("shutdown /s /t 1")
            
        # Some lite hackings
        elif 'hack' in query or 'obtain all connected devices' in query or 'show me all devices you can hack' in query:
            devices = get_connected_devices()
            for device in devices:
                speak('Okay boss as you say')
                print(f'IP address: {device[0]} MAC address: {device[1]}')
                
        # Introduction to everyone
        elif 'introduce yourself' in query:
            speak("Hello everyone I am VS2306 you can also call me Saturday")
            speak("I am an AI based voice assistant.")
            speak("i would like to know your names")
        elif 'hii i am ' in query or 'hello i am ' in query or 'hello saturday i am ' in query or 'myself' in query:
            query = query.replace("Hii i am", "").replace("hello i am", "").replace("hello saturday i am", "").replace("myself", "")
            speak("hello" + query)
        elif 'saturday meet him' in query or 'meet her' in query or 'she is' in query or 'he is' in query:
            intro_name = query.replace("saturday meet him he is", "").replace("saturday meet her she is", "")
            speak("hello" + intro_name)
            
        # Recognized users
        elif 'i am amit' in query or 'i am aditya' in query or 'i am dainwi' in query or 'i am arya' in query:
            speak("Welcome Sir")
            print("User recognised")
        elif 'i am kumar' in query:
            speak("Welcome back boss")
            print("master recognised")
        elif 'i am vivek' in query:
            speak("Welcome back master")
            print("master recoginised")
        elif 'myself amit' in query or 'myself aditya' in query or 'myself dainwi' in query or 'myself arya' in query:
            speak("Welcome sir")
            print("User recognised")
        elif 'i am nandani' in query or 'i am nandini' in query or 'myself nandini' in query or 'myself nandani' in query:
            speak("Welcome ma'am")
            print("User recognised")
            
            
        # Small Talks
        elif 'what are doing' in query or 'whats going on' in query or 'whats upp Saturday' in query:
            speak("Nothing Boss! what about you")
        elif 'whats going on' in query:
            speak("just nothing")
        elif 'how are you' in query:
            speak("I am fine")
            speak("and you?")
        elif 'I am fine ' in query or 'i am also fine' in query or 'fine' in query:
            speak("I am glad that you are fine too")
        elif 'what is love' in query or 'love' in query:
            speak("love is the seventh sense that destroys all six sense")
        elif 'who i am?' in query:
            speak("if you are talking me then definitely you are a human")
        elif 'can i ask a question' in query or 'another question' in query:
            try:
                speak("yes boss whats the question")
                question = takeCommand()
                results = wikipedia.summary(question, sentences=2)
                speak("Boss!")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("sorry boss i didnt find this on net")                
        elif 'thank you' in query or 'thanks' in query:
            speak("you are welcome")
        elif 'but' in query:
            speak("i dont kmow sir")
        elif 'tell them your features' in query or 'things you can do' in query:
            speak("as i am an AI based voice assistant i posses web automation features, i can send whatsapp messages , some system automated works and so many small things")
            speak("currently i am in my developing phases its all i can do")
        elif 'fuck off' in query or 'disgusting' in query:
            speak("sir dont be that much rude")
        else :
            print("sorry boss i didnt find this on net")
        # currently on going on this AI based voice assistant
