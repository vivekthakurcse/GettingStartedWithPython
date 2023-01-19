#pylint:disable=W0621
#pylint:disable=W0703
import webbrowser
import os

command = input("Enter : ").lower

def openSite(link):
	try:
		webbrowser.open(link)
	except Exception as e :
		print(e)
		print("A network error occurred ")

#def openApp(path):
#		os.startfile(path)
	
if __name__ == "__main__" :
	
	while True:
		if "open google" in command :		
			link = "https://www.google.com"
			openSite(link)
		elif "open YouTube" in command:
			link = "https://www.youtube.com"
			openSite(link)