#import nltk
from nltk.chat.util import Chat, reflections

# Define some rules for the chatbot to follow
pairs = [
    ["my name is (.*)", ["Hello %1! How can I assist you today?"]],
    ["(hi|hello|hey)", ["Hi there! How can I help you?"]],
    ["(what is your name?|what's your name?)", ["My name is Chatbot. How can I assist you?"]],
    ["(what can you do?|what are your capabilities?)", ["I can help you with basic tasks like setting reminders, giving directions, and answering questions."]],
    ["(thanks|thank you)", ["You're welcome!"]],
    ["(bye|goodbye)", ["Goodbye! Have a great day!"]],
]

# Create a function to run the chatbot
def run_chatbot():
    chatbot = Chat(pairs, reflections)
    chatbot.converse()


	# Run the chatbot
run_chatbot()
