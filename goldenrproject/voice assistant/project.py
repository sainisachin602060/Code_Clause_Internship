import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import time
import os
import webbrowser


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#function which speak in a lady voice. 
def speak(myaudio):
    engine.say(myaudio)
    engine.runAndWait()
 


#first function which give you some greet message. 
def greet():
    hours=int(datetime.datetime.now().hour)
   
    if hours>=0 and hours<11:
        speak('Good Morning sir')  
        print('Good Morning Sir')   
    elif hours>=11 and hours<15:
        speak('Good Afternoon sir')     
        print('Good Afternoon Sir')
    if hours>=15 and hours<24:
        speak('Good evening Sir') 
        print('Good evening Sir')  
        print()
        
    speak('I am your Personal Assistant') 
    print('I am Your Personal Assistant')
    print()    
     
 
#function 2 which ask your details 
def ask():
    speak('what is your name')
    print('What is Your Name')  
    print()
    name=takecommand()
    
    speak('welcome'+name+'sir')
    print('welcome',name,'sir')
    speak('may i can help you'+name+'sir')
    print('May I Can Help You',name,'sir')
     
    



#function which convert text to speech
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("lisetning....")
        r.pause_threshold=1
        try:
            audio=r.listen(source,timeout=30,phrase_time_limit=10)
            print("voice reconizing...")
            text=r.recognize_google(audio,language='en-in')
          
        except Exception as e:
           
           speak('Soory sir i am not geeting your voice')
           exit() 
        return text
    
    
    
    
    

    
#function home where handle all functions
def home():
    greet()
    ask()
   
    while(True):
        work=takecommand().lower()
        
        if 'how are you' in work:
            speak('i am fine')
            speak('what Abput you  How are You sir')
            print('what Abput you  How are You sir')
       
        elif 'Who are you' in work:
            speak('i am a robotic chatboot builted for your help')  
            print('i am a robotic chatboot builted for your help')  
               
        
        elif 'i am good' in work or 'i am fine' in work:
            speak('i happy you are good well')
            print(' i happy you are good well ')
           
        elif 'what is today date' in work:
            today=date.today()
            speak(today)
            print(today)    
            
         
        elif 'what is current time' in work:
            times=time.localtime()    
            current_time = time.strftime("%H:%M:%S",times)
            speak('Current time is.. '+current_time)
            print('Current Time:',current_time) 
        
        
            
        elif 'i am not good' in work or 'i am sad' in work:
            speak('what happend sir please tell me i am always with you')    
            print('what happend sir please tell me i am always with you')
       
       
        elif 'i love you' in work or 'love you' in work:
            speak('Oh my god  thank you sir') 
            print('Oh my god  thank you sir')
         
        
         
        
         
       
        elif 'what is your name' in work:
            speak('i have no any name but peopple call me chatboot')
            print('i have no any namebut peopple call me chatboot')
            
      
        elif('my mood is off today') in work:
            speak('i love you sir let go for enjoy')
            print('i love you sir let go for enjoy')
       
       
        elif('what are doing') in work:
            speak('nothing i am free ')
            print('nothing i am free ')
            
        elif('how to make software developer') in work:
            speak('learn programing languagae and computer fundamental then you can make software developer')
            print('learn programing languagae and computer fundamental then you can make software developer')
            
            
        
        elif('can you help me') in work:
            speak('sure sir i will help you please tell me ')
            print('sure sir i will help you please tell me ')
        
       
        elif('i need some money') in work:
            speak('sorry i have no money you can go and work then you got some money')
            print('sorry i have no money you can go and work then you got some money')
            
       
        elif(' i need a job') in work:
            speak('call your firend or search on internet then you can got a job')
            print('call your firend or search on internet then you can got a job')
        
        
        elif('i have a tention') in work or ' i have a probelm' in work:
            speak('i will give my best please tell me what is your problem')    
            print('i will give my best please tell me what is your problem')    
                    
            
          #windows appp
          #1.Open notepad and close noepad
        elif 'open notepad' in work:
            path="c:\\windows\\system32\\notepad.exe"
            os.startfile(path)
        elif 'close notepad' in work :
            os.system("TASKKILL /F /IM notepad.exe")  
            
              
         #2.Open powerpoint and close powerpoint
        elif 'open powerpoint' in work or 'please open powerpoint' in work:
            path="C:\\Program Files (x86)\\Microsoft Office\\Office15\\POWERPNT.exe"
            os.startfile(path)
        elif 'close powerpoint' in work :
            os.system("TASKKILL /F /IM POWERPNT.exe") 
            
            
            
            
          #3.Open excel and close excel
        elif 'open excel' in work or 'please open excel' in work:
            path="C:\\Program Files (x86)\\Microsoft Office\\Office15\\EXCEL.exe"
            os.startfile(path)
        elif 'close excel' in work :
            os.system("TASKKILL /F /IM EXCEL.exe")  
              
        # 4.open ms word and close ms word
        elif 'open msword' in work or 'open word' in work:
            path="C:\\Program Files (x86)\\Microsoft Office\\Office15\\WINWORD.exe"
            os.startfile(path)
        elif 'close word' in work or 'close ms word' in work:
            
            os.system("TASKKILL /F /IM WINWORD.exe")  
            
        # 5.open sublime text editor and close sublime text editor    
        elif 'open sublime text' in work or 'open sublime text' in work:
            path="C:\\Program Files (x86)\\Sublime Text 3\\sublime_text.exe"
            os.startfile(path)
        elif 'close sublime' in work or 'close sublime text' in work:
            
            os.system("TASKKILL /F /IM sublime_text.exe")  
              
        # 6.open c drive
        elif 'open c drive' in work or 'c drive' in work:
            path="C:\\"
            os.startfile(path)
        
            
        # 7.open G drive   
        elif 'open G drive' in work or 'G drive' in work:
            path="G:\\"
            os.startfile(path)
        
            
        # 7.open google chrome and close chrome    
        elif 'open chrome' in work or 'open google chrome' in work:
            url="google.com"
            chromePath="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chromePath).open(url)
            
         # 7.open you tube chrome and close you tube   
        elif 'open youtube' in work or 'please open youtube' in work:
            url="youtube.com"
            chromePath="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chromePath).open(url)
           
       
        elif 'close chrome' in work or 'close google chrome' in work or 'close youtube' in work:
            
            os.system("TASKKILL /F /IM chrome.exe")    
       
       
       #exit command
        elif 'You can go ' in work or 'get out' in work:
            speak('Bye sir see you Again')
            print('Bye sir see you Again')
            exit()
        
        #also exit command
        elif 'bye' in work or 'i call you later' in work:
            speak('by sir')
            print('by sir see you again')
            exit() 
       
         #if voice is not catched   
        else:
            speak('i am unable to read your voice please speak again')
    
 
#home function call starting point of our program
home()
         

    
        