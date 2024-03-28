import speech_recognition 
import sys, os
import time

listen = speech_recognition.Recognizer()


def recognition(language_code="en-US"):

    while True:

        with speech_recognition.Microphone() as source:

            os.system('clear')

            # listen.adjust_for_ambient_noise(source=source)

            print("Recording ...")

            audio = listen.record(source=source, duration=3)

        try:

            result = listen.recognize_google(audio, language=language_code)

            result = result.capitalize()

        except Exception as err:

            os.system('clear')

            print('[ERROR] No voice detected! Please speak louder!')

            time.sleep(2)

        else:

            return result

        
def generate_image(subtitle):

    subtitle = subtitle.lower()

    image_format = ".jpg"

    letters = [char for char in subtitle if char != " "]

    image_list = list()

    for char in letters:

        image_list.append(char+image_format)

    return image_list
