import sys
import json
import webbrowser
import subprocess
import pyttsx3
import tkinter as tk
from tkinter import Label
from vosk import Model, KaldiRecognizer
import pyaudio
import threading

# Load intents from JSON file
json_file_path = r'C:\Users\dell\Desktop\366 Project\intents.json'
with open(json_file_path) as f:
    intents = json.load(f)

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Load the Vosk model
model_path = r'C:\Users\dell\Desktop\366 Project\vosk-model-en-us-0.22'
model = Model(model_path)

def recognize_speech():
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Listening...")
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result)["text"]
            print(f"You said: {text}")
            return text.lower()

def handle_intent(intent):
    for i in intents['intents']:
        for pattern in i['patterns']:
            if pattern.lower() in intent:
                print(f"Matched intent: {i['tag']} with pattern: {pattern}")
                if 'action' in i:
                    action = i['action']
                    if action == 'open_chrome':
                        webbrowser.open('http://www.google.com')
                    elif action == 'open_camera':
                        subprocess.run('start microsoft.windows.camera:', shell=True)
                    elif action == 'lock_laptop':
                        subprocess.run('rundll32.exe user32.dll,LockWorkStation')
                    elif action == 'create_file':
                        filename = 'new_file.txt'
                        with open(filename, 'w') as file:
                            file.write('')
                        speak(f"File {filename} created.")
                responses = i['responses']
                if responses:
                    speak(responses[0])
                return
    speak("Sorry, I didn't understand that.")

def update_owl_color(color):
    owl_label.config(fg=color)

def background_listening():
    while True:
        command = recognize_speech()
        if command:
            if "open up" in command:
                update_owl_color("red")  
                speak("How can I assist you?")
                while True:
                    command = recognize_speech()
                    if command:
                        if "adios" in command:
                            speak("Goodbye!")
                            update_owl_color("black")  
                            root.quit()  
                            return
                        handle_intent(command)
            elif "adios" in command:
                speak("Goodbye!")
                update_owl_color("black") 
                root.quit()  
                return

def main():
    global owl_label, root
    root = tk.Tk()
    root.title("Voice Bot")
    
  
    owl_label = Label(root, text="🦉", font=("Arial", 120, "bold"))
    owl_label.pack()
    
    listen_thread = threading.Thread(target=background_listening, daemon=True)
    listen_thread.start()

    # Start the GUI event loop
    root.mainloop()
if __name__ == "__main__":
    main()
