# Import Speech-to-Text Library
import speech_recognition as sr

# Initialise Speech-to-Text Object
r = sr.Recognizer()

# Define Microphone as Audio Input
with sr.Microphone() as source:
    # Set energy threshold level to recognize noise as speech
    r.adjust_for_ambient_noise(source)

    # Listen to user's input
    audio = r.listen(source)

# Convert Speech-to-Text
voice_input = r.recognize_google(audio)

# Use Recgonized Text
if '' in voice_input:
    print('Voice Command not recognized, Please try again.')
else:
    print(f'User Command: {voice_input}')
