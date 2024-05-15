import datetime
import json
import speech_recognition
import pyttsx3

#All intital dictionaries and lists

#####Checking if vim commits work or not#####

#Used for only texts containing the 5W and 1H. Format = Question : answer
Questions = {'what is the time': datetime.time()}

OverKill_Codes = {"function override code 3 1 4":"Chup kar"}

#Used for setting reminders. Expected format = Reminder in string : Time to be reminded at
Reminders = {}

Misc = [] #Any other request


#Fucntions ka area

def user_input() -> str:   #Voice input from the user
    print("User input intitated")
    try:
        recogniser = speech_recognition.Recognizer()
        with speech_recognition.Microphone(device_index = 0) as mic:
            recogniser.adjust_for_ambient_noise(mic, duration = 0.3)
            audio = recogniser.listen(mic)
            text = recogniser.recoginze_google(audio)
            text = text.lower()
            print(f"You: {text}")
            if (OverKill_Codes in text):
                OverKill(text)
            elif ("stop stop stop" in text):
                print("Program ended!")
                exit
            else :
                return text
    except speech_recognition.UnkownValueError:
        user_input()
