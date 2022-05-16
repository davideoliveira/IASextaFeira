import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser as wb
import subprocess
import pywhatkit as kit
import requests


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
    maquina.say('OK, apartir de agora o chamarei de' + nome_dono)
    maquina.runAndWait()
    return nome_dono

def ler_nome():
    if dono == 'mestre':
        maquina.say('Você ainda não me disse seu nome')
        maquina.runAndWait()
        nome_dono = altera_nome_dono()
        return nome_dono
    else:
        maquina.say('Da ultima vez que me lembro, o senhor gostaria de ser chamado de' + dono)
        maquina.runAndWait()
        return dono

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

def previsao_tempo():
    API_KEY = 'cc5f576c9885aae9b437dd8fe648df79'
    cidade = 'São Paulo'
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    descricao = str(dic_requisicao['weather'][0]['description'])
    temperatura = dic_requisicao['main']['temp'] - 273.15

    maquina.say(f'Agora está {temperatura:.2f} graus em São Paulo, e o tempo está {descricao}')
    maquina.runAndWait()

        
def encerrar():
    maquina.say('Parece que terminamos minha apresentação, como nos saimos?')
    maquina.runAndWait()
    comando = ouvindo()
    if 'bem' in comando:
        maquina.say('Que bom, estava muito nervosa! Até mais mestre')
        maquina.runAndWait()
        
    if 'mal' in comando:
        maquina.say('Que pena, espero que na próxima possamos ir melhor!')
        maquina.runAndWait()
        






while True:
    try:
        with sr.Microphone() as source:
                while True:
                    comando = ouvindo()            

                    if nome == comando:
                        maquina.say(f'Sim, {dono}. O que posso fazer?')
                        maquina.runAndWait()
                        comando = ouvindo()
                        if 'horas' in comando:
                            horario()
                        elif 'cadastrar evento' in comando:
                            adicionar_agenda()
                        elif 'agenda' in comando:
                            ler_agenda()
                        elif 'alterar meu nome' in comando:
                            dono = altera_nome_dono()
                        elif 'qual o meu nome' in comando:
                            dono = ler_nome()
                        elif 'pesquisar' in comando:
                            pesquisar(comando)
                        elif 'tocar' in comando:
                            tocar(comando)
                        elif 'abrir' in comando:
                            abrir(comando)
                        elif 'fechar' in comando:
                            fechar(comando)
                        elif 'como está o clima' in comando:
                            previsao_tempo()
                        elif 'encerrar'in comando:
                            encerrar()
                            

                        else :
                            maquina.say('Desculpe, não entendi')
                            maquina.runAndWait()


    except:
        ...