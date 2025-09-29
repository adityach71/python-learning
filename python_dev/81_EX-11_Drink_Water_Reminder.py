import time
from plyer import notification
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def water_reminder():
    while True:
        notification.notify(
            title = "💧 Drink Water Reminder ",
            message = "Time to drink a glass of water!",
            timeout=5
        )

        speak("Time to drink a glass of water!")

        time.sleep(7,200)

if __name__ == "__main__":
    water_reminder()