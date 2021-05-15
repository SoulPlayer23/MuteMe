import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

keywords = ["Venkatesh"]
#Assigning microphone as source
with m:
    print("Speak anything : ")
    #Listening to audio from microphone
    audio = r.listen(m, timeout = 5)
    #Converting audio to text
    text = r.recognize_google(audio)
    print("You said:", text)
    for i in keywords:
        if i in text:
            print("triggered")
    