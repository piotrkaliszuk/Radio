from datetime import datetime,time
from gtts import gTTS
import os
import playsound
#import pyglet

file_name = 'config.txt'
def read_file():
    with open(file_name, "r") as input_file:
        read_file = input_file.read()
        input_file.close()
        return read_file
def asystent(text):
    tts = gTTS(text = text,lang ="pl")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
def read_file():
    with open(file_name, "r") as input_file:
        read_file = input_file.read()
        input_file.close()
        return read_file
def czas(start, end, now):
    is_between = False
    is_between |= start <= now <= end
    is_between |= end < start and (start <= now or now <= end)
    #print(start,end,now)
    return is_between
#Przywitanie
asystent("Witaj Piotrze")

def fileconvert(temp):
    lista = []
    for i,j in enumerate(temp):
        if ":" in j:
            b = j.replace("-"," ")
            c = b.split()
            lista.append(c)
        else:

            if not ":" in temp[i-1] and temp[i]:
                spacja = (f'{temp[i-1]},{temp[i]}')
                x = temp[i-1]
                y = temp[i]

                d = spacja.replace(","," ")
                lista.append(d)
                lista.remove(x)
                lista.remove(y)
            lista.append(j)

            print(j)
    print(lista)
    return lista

file = read_file().split()
obrobiony = fileconvert(file)
#print(obrobiony)

new_sting = " "
while True:
    now = datetime.now().time()
    aktualny_czas = now.strftime("%H:%M")
    for i,j in enumerate(obrobiony):
        if ':' in j[0]:
            if czas(obrobiony[i][0], obrobiony[i][1], str(aktualny_czas)):
                sting = str(obrobiony[i + 1])
                if new_sting != sting:
                    asystent(sting)
                    new_sting = sting






