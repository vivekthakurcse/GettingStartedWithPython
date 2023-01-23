import speech_recognition as sr
import pyttsx3
import sys
import os
import datetime
import subprocess
import webbrowser
import pywhatkit as kit
import pyautogui as key

engine = pyttsx3.init()
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 200)

def speak(say):
    engine.say(say)
    engine.runAndWait()


def takecommand(recognizer, microphone) -> dict:
    
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    response = {"success": True,
                "error": None,
                "transcription": None}
    try:
        response["transcription"] = recognizer.recognize_google(audio,language="en")
        response["transcription"] = response["transcription"].lower()
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize"

    return response


def takequery():
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

#  wish me function for on start event
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("A warm Good Morning boss ")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon boss ")
    else:
        speak("Good Evening boss")

# to open web link
def openweb(link):
    try:
        webbrowser.open(link)  
    except Exception as e :
        print("Network failure!\n" , e)
        speak("boss i would like to adivce you to check the internet connection")
        
def search_google(question):
    try:
        webbrowser.open(question)
    except Exception as e :
        print("Network failure!\n" , e)
     
def clear(): 
    return os.system('cls')

my_phrases = {
            # start event
              'hello': ['Hello boss', 'wakeup'],
              'wake up':['online boss', 'wakeup'],
              'are you up': ['yes boss', 'wakeup'],
              'are you there': ['always boss','wakeup'],
              'good morning': ['a very good morning',None],

            # describing it self
              'what can you do': ["i can open  web automation features, i can send whatsapp messages , some system automated works and so many small things currently i am in my developing phases its all i can do",None],
              'tell me what are things you can do': ["i am an AI based voice assistant i posses web automation features, i can send whatsapp messages , some system automated works and so many small things currently i am in my developing phases its all i can do", None],
              'things you can do': ["as i am an AI based voice assistant i posses web automation features, i can send whatsapp messages , some system automated works and so many small things currently i am in my developing phases its all i can do",None],
              'tell them what are the things you can  do': ["as i am an AI based voice assistant i posses web automation features, i can send whatsapp messages , some system automated works and so many small things currently i am in my developing phases its all i can do",None],
            #  telling his name 
              'who are you': ['I am ELSA, a nlp based voice assistant',None],            
              'what should I call you': ['my name is VS209 but you can also call me ELSA',None],
              'i call you':['you can  call me ELSA',None],
              'what is your name':['my name is vs2306 ',None],
              'your name':['my name is vs2306 but you can also call me ELSA',None],
              'shutdown the system': ['Turning off', 'shutdown'],
              'turn off': ['Goodbye ;)', 'shutdown'],
              'good night': ['One moment please...', 'shutdown'],
            
            # ------------- social sites ----------------
            # insta
              'open instagram': ['okay boss', 'open ig'],
              'open my instagram': ['here is your instagram boss', 'open ig'],
              'open my ig': ['okay boss here is your ig', 'open ig'],
              'check instagram': ['wait for a second boss', 'open ig'],
              'check my instagram': ['okay boss', 'open ig'],
              'can look at my instagram' : ['let me check boss', 'open ig'],
              'can look at my ig' : ['hold on boss let me check', 'open ig'],
              'whats going on at my instagram' : ['let me check boss', 'open ig'],
              'can look at my insta' : ['hold on boss let me check', 'open ig'],
              'whats going on at my insta' : ['let me check boss', 'open ig'],
            # fb
              'open facebook': ['okay boss', 'open fb'],
              'open my facebook': ['here is your instagram boss', 'open fb'],
              'open my fb': ['okay boss here is your ig', 'open fb'],
              'check fb': ['wait for a second boss', 'open fb'],
              'check my facebook': ['okay boss', 'open fb'],
              'can look at my facebook' : ['let me check boss', 'open fb'],
              'can look at my fb' : ['hold on boss let me check', 'open fb'],
              'whats going on at my facebook' : ['let me check boss', 'open fb'],
            # twitter
              'open twitter': ['okay boss', 'open tw'],
              'open my twitter': ['happy tweeting boss', 'open tw'],
              'show me some tweets': ['okay boss here is your tweet feeds', 'open tw'],
              'any tweets': ['wait for a second boss', 'open tw'],
              'check my tweets': ['okay boss', 'open fb'],
              'can look at my twitter' : ['let me check boss', 'open tw'],
              'can look at my tweets' : ['hold on boss let me check', 'open tw'],
              'whats going on at my twitter' : ['let me check boss', 'open tw'],
            # github
              'open github': ['okay boss', 'open git'],
              'open my github': ['happy tweeting boss', 'open git'],
              'show me my repos': ['okay boss here is your tweet feeds', 'open git'],
              'any git issues': ['wait for a second boss', 'open git'],
              'check my github': ['okay boss', 'open fb'],
              'can look at my repos' : ['let me check boss', 'open git'],
              'whats going on at my github' : ['let me check boss', 'open git'],
            # stack overflow
              'open stack':['happy copying pasting boss' , 'open stack'],
              'open stackoverflow':['happy copying pasting boss' , 'open stack'],
              'open stack over flow':['happy copying pasting boss' , 'open stack'],
            # whatsapp
              'open whatsapp': ['okay boss', 'open wa'],
              'open my whatsapp': ['hold on a second sir', 'open wa'],
              'show me my dms': ['and here is your dm boss', 'open wa'],
              'have i got any messages on whatsapp': ['wait for a second boss  let me check', 'open wa'],
              'do i have any messages on whatsapp': ['boss ..let me check', 'open wa'],
              'can look at my dm' : ['as you wish boss', 'open wa'],
              'show me my whatsapp' : ['as your order here is your whatsapp', 'open wa'],
              
            # ------------------------ Googles -----------------------------
            #   mail box support
              'open gmail': ['okay boss', 'open email'],
              'open my gmail': ['hold on a second sir', 'open email'],
              'show me my mailbox': ['and here is your dm boss', 'open email'],
              'have i got any emails': ['wait for a second boss  let me check', 'open email'],
              'do i have any emails': ['boss ..let me check', 'open email'],
              'can look at my mailbox' : ['as you wish boss', 'open email'],
              'show me my emails' : ['as your order here is your whatsapp', 'open email'],
            #  google search support
              'open google': ['okay boss', search_google],
              'search' :['okay boss', search_google],
              'search about' : ['hold on boss', search_google],
            # youtube search support
              'open youtube': ['okay boss', 'open youtube'],
              'search on youtube' : ['hold on boss', 'open youtube'],
              'play my youtube': ['as you say', 'open youtube'],
              
}

unknown_command_phrase = ["i didnt understand" ,None]




 
if __name__ == "__main__" :    
    
    clear()
    while True:
        
        engine.runAndWait()
        microphone = sr.Microphone()
        recognizer = sr.Recognizer()
        print("Listening........")
        # call function 
        response = takecommand(recognizer, microphone)
        pattern = response['transcription']
        say, command = my_phrases.get(pattern,unknown_command_phrase)
        speak(say)

        if command == None:
            print(f'user said : {pattern}')
        elif command == 'wakeup':
            wishme()
        elif 'open ig' in command:
            link = 'www.instagram.com'
            openweb(link)
        elif 'open fb' in command:
            link = 'www.facebook.com'
            openweb(link)
        elif 'open tw' in command:
            link = 'www.twitter.com'
            openweb(link)
        elif 'open git' in command:
            link = 'https://github.com/explore'
            openweb(link)
        elif 'open stack' in command:
            link = 'https://www.stackoverflow.com'
            openweb(link)
        elif 'open wa' in command:
            link = 'https://web.whatsapp.com/'
            openweb(link)
        # search automation --------------------
        elif 'search_google' in command :
            question = takequery().lower()
            search_google(question)
        else: 
            subprocess.check_output(command,shell=True)
