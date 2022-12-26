    #calender day 
     def Cal_day(self): 
         day = datetime.datetime.today().weekday() + 1 
         Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'} 
         if day in Day_dict.keys(): 
             day_of_the_week = Day_dict[day] 
             print(day_of_the_week) 
          
         return day_of_the_week 
  
     #shedule function for remembering todays plans 
     #NOTE For example I have declared my college timetable you can declare anything you want 
     def shedule(self): 
         day = self.Cal_day().lower() 
         self.talk("Boss today's shedule is") 
         Week = {"monday" : "Boss from 9:00 to 9:50 you have Cultural class, from 10:00 to 11:50 you have mechanics class, from 12:00 to 2:00 you have brake, and today you have sensors lab from 2:00", 
         "tuesday" : "Boss from 9:00 to 9:50 you have English class, from 10:00 to 10:50 you have break,from 11:00 to 12:50 you have ELectrical class, from 1:00 to 2:00 you have brake, and today you have biology lab from 2:00", 
         "wednesday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Data structures class, from 11:00 to 11:50 you have mechanics class, from 12:00 to 12:50 you have cultural class, from 1:00 to 2:00 you have brake, and today you have Data structures lab from 2:00", 
         "thrusday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Maths class, from 11:00 to 12:50 you have sensors class, from 1:00 to 2:00 you have brake, and today you have english lab from 2:00", 
         "friday" : "Boss today you have a full day of classes from 9:00 to 9:50 you have Biology class, from 10:00 to 10:50 you have data structures class, from 11:00 to 12:50 you have Elements of computing class, from 1:00 to 2:00 you have brake, and today you have Electronics lab from 2:00", 
         "saturday" : "Boss today you have a full day of classes from 9:00 to 11:50 you have maths lab, from 12:00 to 12:50 you have english class, from 1:00 to 2:00 you have brake, and today you have elements of computing lab from 2:00", 
         "sunday":"Boss today is holiday but we can't say anything when they will bomb with any assisgnments"} 
         if day in Week.keys(): 
             self.talk(Week[day]) 
  
     #college resources commands 
     #NOTE Below are some dummy links replace with your college website links 
     def college(self,command): 
         print(command) 
         if 'teams' in command: 
             self.talk('opening your microsoft teams') 
             webbrowser.open('https://teams.microsoft.com/') 
         elif 'stream' in command: 
             self.talk('opening your microsoft stream') 
             webbrowser.open('https://web.microsoftstream.com/') 
         elif 'outlook' in command: 
             self.talk('opening your microsoft school outlook') 
             webbrowser.open('https://outlook.office.com/mail/') 
         elif 'amrita portal' in command: 
             self.talk('opening your amrita university management system') 
             webbrowser.open('https://aumsam.amrita.edu/') 
         elif 'octave' in command: 
             self.talk('opening Octave online') 
             webbrowser.open('https://octave-online.net/') 
         else : 
             self.No_result_found() 
      
     #Online classes 
     def OnlineClasses(self,command): 
         print(command) 
         #Keep as many "elif" statemets based on your subject Eg: I have kept a dummy links for JAVA and mechanics classes link of MS Teams 
         if("java" in command): 
             self.talk('opening DSA class in teams') 
             webbrowser.open("https://teams.microsoft.com/java") 
         elif("mechanics" in command): 
             self.talk('opening mechanics class in teams') 
             webbrowser.open("https://teams.microsoft.com/mechanics") 
         elif 'online classes' in command: 
             self.talk('opening your microsoft teams') 
             webbrowser.open('https://teams.microsoft.com/') 
  
     #Brower Search commands 
     def B_S(self,command): 
         print(command) 
         try: 
             # ('what is meant by' in self.command) or ('tell me about' in self.command) or ('who the heck is' in self.command) 
             if ('wikipedia' in command): 
                 target1 = command.replace('search for','') 
                 target1 = target1.replace('in wikipedia','') 
             elif('what is meant by' in command): 
                 target1 = command.replace("what is meant by"," ") 
             elif('tell me about' in command): 
                 target1 = command.replace("tell me about"," ") 
             elif('who the heck is' in command): 
                 target1 = command.replace("who the heck is"," ") 
             print("searching....") 
             info = wikipedia.summary(target1,5) 
             print(info) 
             self.talk("according to wikipedia "+info) 
         except : 
             self.No_result_found() 
          
     #Browser 
     def brows(self,command): 
         print(command) 
         if 'google' in command: 
             self.talk("Boss, what should I search on google..") 
             S = self.take_Command()#taking command for what to search in google 
             webbrowser.open(f"{S}") 
         elif 'edge' in command: 
             self.talk('opening your Miscrosoft edge') 
             os.startfile('..\\..\\MicrosoftEdge.exe')#path for your edge browser application 
         else : 
             self.No_result_found() 
  
     #google applications selection