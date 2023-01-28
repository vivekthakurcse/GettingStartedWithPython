from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# response generation of this AI
chatbot = ChatBot("vs2306")
trainer = ListTrainer(chatbot)

trainer.train(
    [
        "hello" ,
        "hii" ,
        "how are you",
        "i am good",
        "that is good to hear",
        "thank you",
        "you're welcome"
    ]
)

while True :
    
    user_input = input(">>> ").lower()
    response = chatbot.get_response(user_input)
    print(response)