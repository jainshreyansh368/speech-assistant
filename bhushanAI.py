import pyttsx3
import datetime
import webbrowser
import wikipedia
import os
import smtplib
import sys
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0])
engine.setProperty('voice',voices[0].id)

def wish():
    #print('Enter your name')
    #name = input()
    print("I am Bhushan Lal. How may I help you ?")
    hour = int(datetime.datetime.now().hour)
    if(hour <= 12 and hour >= 0):
        speak('Good Morning ' )
    elif (hour >12 and hour < 17):
        speak('Good afternoon ')
    elif (hour >=17 and hour<20):
        speak('Good evening ')
    else:
        speak('Good night')
    speak("I am Bhushan Lal. How may I help you ?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)
        print("Say that again....")
        return "None"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('bhushanlal666666@gmail.com','Bhushan@123')
    server.sendmail('bhushanlal666666@gmail.com',to,content)
    server.close()
 

def createEmail():

    speak("Enter email id of the recipient")
    print("Enter email-id of recipient")
    to = input()
    if '@' not in to:
        speak("Please enter valid email address")
        print("Please enter valid email address")
        createEmail()
    else:
        speak("What you want to send?")
        content = takecommand()
        print("Do you want to sent it or change it (y/n)?")
        speak("Do you want to sent it or change it?")
        c = input()
        if c == 'y':
            sendEmail(to,content)
            print("Email Sent Succesfully.")
            speak("Email sent succesfully")
            
        elif c == 'n':
            speak("Sending email cancelled")


if __name__ == "__main__":
    while True:
        
        wish()
        query = takecommand().lower()

        if 'open youtube' in query:
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open("youtube.com")

        intro = ["who are you","tell me about yourself","tell me about you"]

        if any (x in query for x in intro):
            speak("I am Bhushan Lal. Mr. Vaibhav Ghai's personal assistant and i am the future of Artificaial intelligence")

        elif 'search' in query:
            speak("Search results may take a while ")
            query = query.replace("search","")
            print(query)
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak("According to wikipedia")
            speak(results)

        elif 'tell me a joke' in query:
            speak("Here is a joke. There was an ant and an elephant"+
                  "Ant said whenever elephant will cross me i will beat him"+
                  "with my legs.")

        elif 'education' in query:
            path = "F:\\EDUCATION"
            os.startfile(path)
            print("Bringing Education")
            speak("Education is on your way")

        elif 'movies' in query:
            path = "F:\\Movie"
            os.startfile(path)
            print("Showing movies...")
            speak("Your carnival is here")

        elif 'code' in query:
            path = "G:\\CodeBlocks\\codeblocks.exe"
            os.startfile(path)
            print("opening codeblocks...")
            speak("opening codeblocks")


        elif 'show my emails' in query:
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open("gmail.com")
            print("Opening emails...")
            speak("Emails are on your way")

        elif 'send email' in query:
            try:
                createEmail()
            
            except exception as e:
                speak("An error occured while sending the mail")
                print("Error occured")
        elif 'weather' in query:
            chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open("google.com/search?q=weather+in+my+area")
            speak("I found this on web ")

        list = ["bye","goodbye","exit","quit","close","go","see you","stop","silence","silent"]
        if any(x in query for x in list):
            speak("Good Bye ! It was a nice meeting you ")
            sys.exit()

        elif 'f drive' in query:
            path = "F:\\"
            os.startfile(path)
            print("Opening F drive...")
            speak("Opening f drive")
            
        




      






 


