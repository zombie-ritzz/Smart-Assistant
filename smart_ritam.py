import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os 
import smtplib
import pywhatkit as kit
engine=pyttsx3.init('sapi5')  
voices=engine.getProperty('voices') 
print(voices[2].id)
engine.setProperty('voice',voices[2].id)  

def speak(audio):
    rr=engine.getProperty('rate')
    #print(rr)
    rr=150
    
    engine.setProperty('rate',rr)
    engine.say(audio)   
    engine.runAndWait() 

def welcome():
    h=int (datetime.datetime.now().hour)  #1stdatetime is a class 2nd datetime is a constructor, now is a function and hour is a property
    if(h>=0 and h<12):
        speak("Good morning!! Have a nice day")
    elif(h>=12 and h<18):
        speak("Good Afternoon!!")
    else:
        speak("good evening")
    speak("how can i help you Ritam??")

def sendEmail(to, content):
            server = smtplib.SMTP('smtp.gmail.com',587) #smptplib is a library class smtp is a mail protocol smtp use as a constructor 587 is the port number
            server.ehlo()    #loading the mail
            server.starttls()  #transfer the mail
            SUBJECT = "testing mail"
            message='testing mail:{}\n\n{}'.format(SUBJECT,content)
            server.login('xxxx@gmail.com','#######')
            server.sendmail('xxxx@gmail.com',to,message)
            server.close()

def takeCommand():
    rec=sr.Recognizer() #recognizer is a function which recognize our voice
    #microphone is a function which records the source voice
    with sr.Microphone() as source:
        print("Listening....")
        rec.pause_threshold=0.5   #seconds of non-speaking audio before a phrase is considered complete
        audio=rec.listen(source)  #listen is a func which accepts the source voice and record it and store into audio
    try:
       # print("Trying to decode....")
        command = rec.recognize_google(audio,language="en-in")
        print("user said ",command)
    except Exception as e:
        print(e)
        #speak("unable to recognise your command, please say it again...")
        return "NONE"
    return command

    
if __name__=="__main__":
    speak("hello ritam!!i'm here for you.")
    welcome()
    #takeCommand()
    while True:
        q= takeCommand().lower()
        if 'wikipedia' in q:
            speak("Searching Wikipedia...")
            q=q.replace("wikipedia","")  #replace the wikipedia word by blank
            results=wikipedia.summary(q,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in q:
            webbrowser.open("youtube.com")
        elif 'goodbye' in q:
            speak("ok goodbye see you again")
            break
        elif "search" in q:
            results=wikipedia.summary(q,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "who is" in q:
            results=wikipedia.summary(q,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open google' in q:
            webbrowser.open("google.com")
        elif "open stackoverflow" in q:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in q:
            music_dir='D:\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "what is the time now" in q:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print("user said ",strTime)
            speak(f"Sir,the time is {strTime}")
        elif "open code" in q:
            codepath="C:\\Users\\RITAM PAL\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codepath)
        
        elif 'email to me' in q:
            try:
                print("say something...")
                speak("What should I say?")
                content = takeCommand()
                to="yyyyyyyy@gmail.com"
                sendEmail (to,content)
                speak ("Email has been sent!")
            except Exception as e:
                print (e)
                speak("Sorry!! I'm not able to sent the email")
        elif 'send message from whatsapp' in q:
            try:
                kit.sendwhatmsg("+911234567895","Hi...i'm Ritam's python assistant.",22,55)
                print("Sucessfully Sent!!")
            except Exception as e:
                print(e)
                speak("sorry!!!")
