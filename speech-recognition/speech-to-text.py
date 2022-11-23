# Python program to translate
# speech to text and text to speech


import speech_recognition as sr

r = sr.Recognizer()

while(1):

    try:
        with sr.Microphone() as source2:
            print(">>>>>>>>>>>>>> Initializing .....")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            print(">>>>>>>>>>>>>> Listing .....")

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
