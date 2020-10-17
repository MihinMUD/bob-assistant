from gtts import gTTS
import time
import playsound
import speech_recognition as sr
import os



def getcm():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        aoudio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(aoudio)
            print(said)
        except:
            pass
    return said.lower()
def speak(word):
    tts = gTTS(text=word,lang="en")
    filename = "Voice.mp3"
    os.remove(filename)
    tts.save(filename)
    playsound.playsound(filename)
def answer(word,answer):
    if word in text:
        print(answer)
        speak(answer)
Wake = ["ok bob","hey bob"]

while True:
    print("speak now")
    text = getcm()
    if text.count(WAKE)> 0:
        speak("How may I help you?")
        text = getcm()   
        answer("hi","Hi, I'm BOB Nice to meet you!")
        answer("good morning" , "Good morning")