import speech_recognition as sr
import pyttsx3


#Cria um reconhecedor
audio = sr.Recognizer()
#Cria sintetizador de voz
maquina = pyttsx3.init()



try:
    #Abri o microfone para captura
    with sr.Microphone() as source:
        while True:
            voz = audio.listen(source)        #Define o microfone como fonte de audio
            comando = audio.recognize_google(voz, language='pt')
            comando = comando.lower()

            if 'ok sexta-feira' in comando:
                print(comando)
                maquina.say('Olá, como posso ajudar?')
                maquina.runAndWait()



except:
    print("Desculpe, não consegui entender.")
