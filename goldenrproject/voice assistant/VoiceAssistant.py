import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener=aa.Recognizer()
machine=pyttsx3.init()

def talk(text):
    machine.say(text)
    

def input_instruction():
    try:
        with aa.Microphone() as origin:
            print("Listening.....")
            Speech=listener.listen(origin)
            instruction=listener.recognize_google(Speech)
            print(instruction)
            if "jarvis" in instruction:
                instruction=instruction.replace('jarvis','')
                print(instruction)
            return instruction
    except:
        pass

        
    
    

def play_jarvis():
    instruction=input_instruction()
    print(instruction)
    
    if instruction and "play" in instruction:
        song=instruction.replace('play','')
        talk("playing" + song)
        pywhatkit.playonyt(song)  
    
    elif instruction and 'time' in instruction:
        time=datetime.datetime.now().strftime('%I:%M%P')
        talk("current time"+time)
        
    elif instruction and 'date' in instruction:
        date=datetime.datetime.now().strftime('%d /%m /%y')
        talk("Today' 's date"+date)
        
    elif instruction and 'how are you'  in instruction:
        talk('i am fine what about you')
        
    elif instruction and 'who is' in instruction:
        human=  instruction.replace('who is'," ")
        info=wikipedia.summary(human,1)
        print(info)
        talk(info)
    else:
        talk("please repeat")
        
play_jarvis()        
