# Implementation of a program that takes the voice from the user and

# and write it in a text file which can be converted into a pdf notes.

import speech_recognition as sr

def Listen():

 

     r = sr.Recognizer() 

     with sr.Microphone() as source: 

         r.adjust_for_ambient_noise(source) 

         audio = r.listen(source) # Listening  Teacher

     try: 

         query = r.recognize_google(audio, language='en-in') 

         query = query.lower() 

     except Exception as e: 

         print(e) 

         print("unable to recognize") # Catching a general exepction

         return "none" 

  

     return query

 

 # main loop

while True :

 		with open("notes.txt", "a") as f:

		data = Listen().lower() # Listening to teacher

		f.write(f"{data}\n") # Writing the data to text file

		

# The Part that convert this text file into an pdf is pending

# It can be complete by You Guys ^_^
