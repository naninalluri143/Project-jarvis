import datetime
import os
from Speak import Say
#time function
def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()
    
    elif "date" in query:
        Date()
    
    elif "day" in query:
        Day()
    


def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is", "").replace("wikipedia", "")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)
    
    elif "google" in tag:
        query = str(query).replace("google", "")
        query = query.replace("search", "")
        import pywhatkit
        pywhatkit.search(query)

    elif "github" in tag:
        query = str(query)
        query = query.replace("open", "")
        import webbrowser
        webbrowser.open('https://github.com/')
    
    elif "w3 schools" in tag:
        query = str(query)
        query = query.replace("open", "")
        import webbrowser
        webbrowser.open('https://www.w3schools.com/')
    
    elif "songs" in tag:
        query = str(query).replace("play", "")
        import playsound
        playsound.playsound('ironman.mp3')
    
    elif "any desk" in tag:
        query = str(query).replace("open", "")
        os.startfile("C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe")
        Say(result)
    
    elif "zoom" in tag:
        query = str(query).replace("open", "")
        os.startfile("C:\\Users\\ASUS\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
        Say(result)
    
    elif "vpn" in tag:
        query = str(query).replace("open", "")
        os.startfile("C:\\Program Files (x86)\\Proton Technologies\\ProtonVPN\\ProtonVPN.exe")
        