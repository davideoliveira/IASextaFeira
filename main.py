import speech_recognition as sr
import pyttsx3
import datetime


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
                comando = comando.replace('ok sexta-feira', '')
                print(comando)
                maquina.say('Olá, como posso ajudar?')
                maquina.runAndWait()

                if 'horas' in comando:
                    hora = datetime.datetime.now().strftime('%H:%M')
                    maquina.say('Agora são' + hora)
                    maquina.runAndWait()



except:
    print("Desculpe, não consegui entender.")


def horario(comando):
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são' + hora)
        maquina.runAndWait()