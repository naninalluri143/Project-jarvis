import pyttsx3 #text-to-speech

def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate',170)
    print("   ")
    print(f"A.I :{Text}")
    engine.say(text = Text)
    engine.runAndWait()
    print("   ")

Say("Hello")