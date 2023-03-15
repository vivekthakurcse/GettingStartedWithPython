import speech_recognition as sr
import pyttsx3
import nltk
nltk.download('punkit')
from nltk.chat.util import Chat, reflections



pairs = [
    
    # Example patterns and responses:
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot. What's yours?"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1! Nice to meet you."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you."]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "It's okay. No worries."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Bye!", "See you later!"]
    ]
]



def convo():
 
    chatbot = Chat(pairs, reflections)
    
    while True:
        try:
            user_input = input("> ")
            chatbot_response = chatbot.respond(user_input)
            print(chatbot_response)
            
            if chatbot_response == "I'm sorry, I don't understand.":
                new_response = input("What should I say? ")
                pairs.append([user_input, new_response])
                print("Thanks! I'll remember that.")
        except KeyboardInterrupt:
         
            print("Goodbye!")
            break
            
            

# Initializing the engine to speak
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)





# Speak Functionality
def speak(text):
    engine.say(text)
    engine.runAndWait()





# Listen Functionality
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
            



if __name__ == "__main__":
    convo()