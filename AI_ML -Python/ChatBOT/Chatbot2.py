import openai_secret_manager

# Let's check the credentials
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secrets("openai")

print(secrets)

# Installing the library
#!pip install transformers

import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Define a function to generate responses
def generate_response(prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    response = model.generate(input_ids, max_length=1024, top_p=0.9, top_k=40)
    response_text = tokenizer.decode(response[0], skip_special_tokens=True)
    return response_text

# Define the chatbot
def chatbot():
    print("Hello, I am GPT-2. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input == "quit":
            print("Goodbye, have a great day!")
            break
        response = generate_response(user_input)
        print("GPT-2: " + response)

chatbot()
