import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

#Assigning microphone as source
with m:
    print("Speak anything : ")
    #Listening to audio from microphone
    audio = r.listen(m, 5)
    #Converting audio to text
    text = r.recognize_google(audio)
    print("You said:", text)
    