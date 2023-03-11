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

def chatbot():
 
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

if __name__ == "__main__":
    chatbot()