from speech_recognition import Recognizer, Microphone
import os
import time

clearConsole = lambda: os.system('cls' if os.name in ('nt','dos')else 'clear')
recognizer = Recognizer()
time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
time = time.replace(" ","/")
file = open("log.txt", "a")

# voice recording
with Microphone() as source:
    clearConsole()
    recognizer.adjust_for_ambient_noise(source)
    print("Quel est votre mot de passe?")
    recorded_audio = recognizer.listen(source)
    
# text recording
try:
    text = recognizer.recognize_google(
            recorded_audio, 
            language="fr-FR"
        )
    #checking and storing connection status
    if (text == "Roberto"):
        print ("Mot de passe correct")
        file.write('Connexion Reussi le '+time+'\n')
    else:
        print ("Mot de passe incorrect")
        file.write('Connexion Réfusé le '+time+'\n')
        
except Exception as ex:
    print(ex)