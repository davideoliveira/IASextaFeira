import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser as wb
import subprocess
import os
import pywhatkit as kit


nome = 'ok sexta-feira'
dono = 'mestre'

audio = sr.Recognizer()
maquina = pyttsx3.init()

def ouvindo():
    voz = audio.listen(source)        
    comando = audio.recognize_google(voz, language='pt')
    comando = comando.lower()
    print(comando)
    return comando

def horario():
    hora = datetime.datetime.now().strftime('%H:%M')
    maquina.say('Agora são' + hora)
    maquina.runAndWait()

def ler_agenda():
    with open('agenda.txt', 'r') as txt:
        agenda = txt.read()
        maquina.say(agenda)
        maquina.runAndWait()

def adicionar_agenda():
    maquina.say('Ok, qual evento devo cadastrar?')
    maquina.runAndWait()
    agenda = ouvindo()
    with open('agenda.txt', 'a') as txt:
        txt.write(agenda)
        maquina.say('Agenda atualizada')
        maquina.runAndWait()

def altera_nome_dono():
    maquina.say('Como gostaria de ser chamado?')
    maquina.runAndWait()
    nome_dono = ouvindo()
    
    return nome_dono

def ler_nome():
    if dono == '':
        maquina.say('Eu ainda não sei seu nome')
        maquina.runAndWait()
        altera_nome_dono()
    else:
        maquina.say('seu nome é ' + dono)
        maquina.runAndWait()

def pesquisar(comando):
    comando = comando.replace('pesquisar por', '')
    wb.get('windows-default').open_new(f'https://www.google.com/search?q={comando}')

def tocar(comando):
    comando = comando.replace('tocar', '')
    kit.playonyt(comando)

def abrir(comando):
    comando = comando.replace('abrir', '')
    if 'calculadora' in comando:
        subprocess.Popen(['calc'])
    elif 'notas' in comando:
        subprocess.Popen(['notepad'])
    

def fechar(comando):
    comando = comando.replace('fechar', '')
    if 'notas' in comando:
        subprocess.run(['taskkill', '/IM', 'notepad.exe'])
    elif 'chrome' in comando:
        subprocess.run(['taskkill', '/IM', 'chrome.exe'])
    elif 'firefox' in comando:
        subprocess.run(['taskkill', '/IM', 'firefox.exe'])








with sr.Microphone() as source:
        while True:
            comando = ouvindo()            

            if nome == comando:
                maquina.say('Sim, ' + dono)
                maquina.runAndWait()
                comando = ouvindo()
                if 'horas' in comando:
                    horario()
                elif 'agenda' in comando:
                    ler_agenda()
                elif 'adicionar evento' in comando:
                    adicionar_agenda()
                elif 'alterar meu nome' in comando:
                    dono = altera_nome_dono()
                elif 'qual o meu nome' in comando:
                    maquina.say('seu nome é ' + dono)
                    maquina.runAndWait()
                elif 'pesquisar' in comando:
                    pesquisar(comando)
                elif 'tocar' in comando:
                    tocar(comando)
                elif 'abrir' in comando:
                    abrir(comando)
                elif 'fechar' in comando:
                    fechar(comando)

                else :
                    maquina.say('Desculpe, não entendi')
                    maquina.runAndWait()




                




