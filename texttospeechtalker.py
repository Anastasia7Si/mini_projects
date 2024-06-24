"""Преобразование текста в речь.
Пример программы, использующей возможности преображования текста в речь
модуля pyttsx3."""

import sys

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, open a command prompt and run:')
    print('pip install pyttsx3.')
    print('On macOS and Linux, open a terminal and run:')
    print('pip3 install pyttsx3.')
    sys.exit()


tts = pyttsx3.init()

print('Text To Speech Talker.')
print('Text-to-speech using pyttsx3 module, which it turn uses.')
print('the NSSpeechSynthesizer (on macOS), SAPI5 (in Windows), or.')
print('aSpeak (on Lunix) speech engines.\n')
print('Enter the text to speak, or QUIT to quit.')
while True:
    text = input('> ')
    if text.upper == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    tts.say(text)
    tts.runAndWait()
