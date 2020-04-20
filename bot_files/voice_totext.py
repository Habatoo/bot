import speech_recognition as sr
import os
import sys

def myCommand():
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Bot: Говори...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='ru-RU').lower()
        print('User: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Bot: Не понял...')
        try:
            command = myCommand()
        except:
            command = 'стоп голос'
    return command

def assistant(command):
    "if statements for executing commands"
    if 'стоп голос' in command:
        print('Bot: Отлично, стоп голос!')
        return 'стоп голос'
    else:
        return command

if __name__ == '__main__':
    while True:
        assistant(myCommand())
