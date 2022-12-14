import random
import os
import pyttsx3
import speech_recognition as sr
import wavio as wv
import sounddevice as sd
from scipy.io.wavfile import write
from time import sleep
import sys
import time
freq = 44100
duration = 3
kryptonimy = {'Young':'1234','horse':'6124','Johnny':'6674','it':'0101'}

while True:
    engine = pyttsx3.init()
    engine.say("Podaj kryptonim")
    engine.runAndWait()

    recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
    sd.wait()

    write("recording0.wav", freq, recording)
    wv.write("recording1.wav", recording, freq, sampwidth=2)

    filename = 'recording1.wav'
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)

    if text in kryptonimy:
        print(f'Witaj {text}!')
        engine.runAndWait()
        mytext = "Witaj" + text
        engine.say(mytext)
        engine.runAndWait()

        engine.say("Podaj PIN")
        engine.runAndWait()

        recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
        sd.wait()

        write("recording2.wav", freq, recording)
        wv.write("recording3.wav", recording, freq, sampwidth=2)

        filename = 'recording3.wav'
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio_data = r.record(source)
            text2 = r.recognize_google(audio_data)
            print(f'Podany pin {text2}')

        if kryptonimy[text] == text2:
            print("Hasło potwierdzone")
            engine.say("Hasło potwierdzone")
            engine.runAndWait()
            print(f"Witamy w systemie {text}")
            engine.say("Witamy w systemie")
            engine.runAndWait()
            string = """ 
            Loading...
            Downloading...
            Please wait...
            Logging in...
            Succes! (^.^)"""
            print()
            for letter in string:
                sleep(0.15)
                sys.stdout.write(letter)
                sys.stdout.flush()
            items = ['A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            nums = list(range(1, 10))
            count = 100   
            for i in range(1, 11):
                items.append(str(i))
                items.append(" " * i)
            def rain(row, column):
                for i in range(row):
                    s = ''
                    for j in range(column):
                        ri = random.randrange(len(items))
                        s += items[ri]
                    print(s)
                    time.sleep(0.3)
            while count != 0:
                count = count - 1
                nums2 = random.choice(nums)
                for i in range(10):
                    rain(1, 150)
            break
        else:
            engine.say("Złe hasło")
            engine.runAndWait()
            engine.say("Spróbuj jeszcze raz")
            engine.runAndWait()
    if text not in kryptonimy:
        print("Nieznany kryptonim!")
        engine.say("Nieznany kryptonim")
        engine.runAndWait()
        engine.say("Spróbuj jeszcze raz")
        engine.runAndWait()



