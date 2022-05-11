import speech_recognition as sr
import pyttsx3
import datetime

nome = 'ok sexta-feira'

#Cria um reconhecedor
audio = sr.Recognizer()
#Cria sintetizador de voz
maquina = pyttsx3.init()


#Abri o microfone para captura
with sr.Microphone() as source:
        while True:
            comando = ouvindo()            

            if nome == comando:
                maquina.say('Sim, mestre. O que posso fazer?')
                maquina.runAndWait()
                comando = ouvindo()
                if 'horas' in comando:
                    horario()
                elif 'agenda' in comando:
                    ler_agenda()
                elif 'Cadastrar evento' in comando:
                    adicionar_agenda()




                


def ouvindo():
    voz = audio.listen(source)        #Define o microfone como fonte de audio
    comando = audio.recognize_google(voz, language='pt')
    comando = comando.lower()
    print(comando)
    return comando

def horario(comando):
    hora = datetime.datetime.now().strftime('%H:%M')
    maquina.say('Agora são' + hora)
    maquina.runAndWait()

def ler_agenda(comando):
    with open('agenda.txt', 'r') as txt:
        agenda = txt.read()
        maquina.say(agenda)
        maquina.runAndWait()


def adicionar_agenda(comando):
    maquina.say('Ok, qual evento devo cadastrar?')
    maquina.runAndWait()
    agenda = ouvindo()
    with open('agenda.txt', 'r') as txt:
        txt.write(agenda)
        maquina.say('Agenda atualizada')