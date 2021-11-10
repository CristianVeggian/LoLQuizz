import csv
from time import strptime
import PySimpleGUI as sg
import datetime,
from random import randint
from PIL import Image
import os

win_w = 400
win_h = 300

def image_window(campeao, i):

    img = Image.open('images\\champs\\' + campeao[0]+'_0.png')
    x = randint(0, img.size[0]-150)
    y = randint(0, img.size[1]-150)

    area = (x, y, x+150, y + 150)

    cropped_img = img.crop(area)
    cropped_img.save('images\\champs\\temp.png')

    layout = [  [sg.Image('images\\champs\\temp.png', key='-champion-', pad = (0, 30))],
                [sg.Text(str(i) + '/157'), sg.InputText()],
                [sg.Submit(),sg.Cancel()]]

    window = sg.Window('Pedaço da Imagem', layout, size=(win_w, win_h), element_justification='c')

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            os.remove('images\\champs\\temp.png')
            return -1
        if event == 'Submit':
            os.remove('images\\champs\\temp.png')
            window.close()
            remover = "'- "
            txt2 = campeao[0]
            txt1 = values[0]
            for char in remover:
                txt2 = txt2.replace(char, '')
                txt1 = txt1.replace(char, '')
            if values[0] == None or txt1.lower() != txt2.lower():
                sg.popup_no_buttons(title='Errou! A resposta era '+ campeao[0], keep_on_top=True, image="images\\champs\\" + campeao[0]+"_0.png", auto_close=True, auto_close_duration=2)
                return 0
            else:
                sg.popup_no_buttons(title='Acertou! Boa!', keep_on_top=True, image="images\\champs\\" + campeao[0]+"_0.png", auto_close=True, auto_close_duration=2)
                return 1

def title_window(campeao, i):

    layout = [  [sg.Text(campeao[1])],
                [sg.Text(str(i) + '/157'), sg.InputText()],
                [sg.Submit(),sg.Cancel()]]

    window = sg.Window('Título do Campeão', layout, size=(win_w, win_h), element_justification='c')

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            return -1
        if event == 'Submit':
            window.close()
            remover = "'- "
            txt2 = campeao[0]
            txt1 = values[0]
            for char in remover:
                txt2 = txt2.replace(char, '')
                txt1 = txt1.replace(char, '')
            if values[0] == None or txt1.lower() != txt2.lower():
                sg.popup_no_buttons('Errou! A resposta era '+ campeao[0], no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=2)
                return 0
            else:
                sg.popup_no_buttons('Acertou! Boa!', no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=2)
                return 1

def ultimate_window(campeao, i):

    layout = [  [sg.Text(campeao[6])],
                [sg.Text(str(i) + '/157'), sg.InputText()],
                [sg.Submit(),sg.Cancel()]]

    window = sg.Window('Título do Campeão', layout, size=(win_w, win_h), element_justification='c')

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            return -1
        if event == 'Submit':
            window.close()
            remover = "'- "
            txt2 = campeao[0]
            txt1 = values[0]
            for char in remover:
                txt2 = txt2.replace(char, '')
                txt1 = txt1.replace(char, '')
            if values[0] == None or txt1.lower() != txt2.lower():
                sg.popup_no_buttons('Errou! A resposta era '+ campeao[0], no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=2)
                return 0
            else:
                sg.popup_no_buttons('Acertou! Boa!', no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=2)
                return 1

def passive_window(campeao, i):

    layout = [  [sg.Text(campeao[2])],
                [sg.Text(str(i) + '/157'), sg.InputText()],
                [sg.Submit(),sg.Cancel()]]

    window = sg.Window('Título do Campeão', layout, size=(win_w, win_h), element_justification='c')

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            return -1
        if event == 'Submit':
            window.close()
            remover = "'- "
            txt2 = campeao[0]
            txt1 = values[0]
            for char in remover:
                txt2 = txt2.replace(char, '')
                txt1 = txt1.replace(char, '')
            if values[0] == None or txt1.lower() != txt2.lower():
                sg.popup_no_buttons('Errou! A resposta era '+ campeao[0], no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=2)
                return 0
            else:
                sg.popup_no_buttons('Acertou! Boa!', no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=2)
                return 1

def skills_window(campeao, i):

    layout = [  [sg.Text(campeao[3], key='-skill1-')],
                [sg.Text(campeao[4], key='-skill2-', visible=False)],
                [sg.Text(campeao[5], key='-skill3-', visible=False)],
                [sg.Text(str(i) + '/157'), sg.InputText()],
                [sg.Submit(),sg.Cancel()]]

    window = sg.Window('Habilidades do Campeão', layout, size=(win_w, win_h), element_justification='c')

    contador = 0

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            return -1
        if event == 'Submit':
            remover = "'- "
            txt2 = campeao[0]
            txt1 = values[0]
            for char in remover:
                txt2 = txt2.replace(char, '')
                txt1 = txt1.replace(char, '')
            if values[0] == None or txt1.lower() != txt2.lower():
                if contador == 0:
                    contador += 1
                    window['-skill2-'].Update(visible = True)
                elif contador == 1:
                    contador += 1
                    window['-skill3-'].Update(visible = True)  
                else:
                    sg.popup_no_buttons('Errou! A resposta era '+ campeao[0], no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=2)
                    window.close()
                    return 0
            else:
                sg.popup_no_buttons('Acertou! Boa!', no_titlebar=True, keep_on_top=True, auto_close=True, auto_close_duration=2)
                window.close()
                return 1

def org1(e):
    tempo = datetime.datetime.strptime(e[1], "%H:%M:%S.%f")
    segundos = tempo.hour * 3600 + tempo.minute * 60 + tempo.second + tempo.microsecond/100000
    valoracao = (1/segundos)*0.4 + e[2]*0.6
    return valoracao

def gravaRecorde(arquivo, nome, tempo, pontos):
    arquivo_aberto = open(arquivo, 'r', encoding='utf-8')
    pontuacoes = [[nome, str(tempo), pontos]]
    for linha in arquivo_aberto:
        pessoa = linha.split('#')
        pontuacoes.append([pessoa[0], pessoa[1], int(pessoa[2].replace('\n', ''))])
    pontuacoes.sort(key=org1, reverse=True)
    arquivo_aberto.close()
    arquivo_aberto = open(arquivo, 'w', encoding='utf-8')
    for pessoa in pontuacoes:        
        arquivo_aberto.write(pessoa[0] + '#' + pessoa[1] + '#' + str(pessoa[2])+'\n')

def lerSkill(arquivo):
    arquivo_aberto = open(arquivo, 'r', encoding='utf-8')
    return list(csv.reader(arquivo_aberto, delimiter='#'))

arquivo = r'C:\Users\crist\Desktop\jogoLoL\jogo\skills.csv'

dados = lerSkill(arquivo)

CHAMPSIZE = len(dados)

def randomize(e):
    return randint(0, CHAMPSIZE)


def criaLista(end, start=0):
    lista = []
    for i in range(start, end):
        lista.append(i)
    lista.sort(key=randomize)
    return lista

def jogar():

    layout_game = [ [sg.Image('images/titulo.png', enable_events=True, key='-1-')],
                [sg.Image('images/ultimate.png', enable_events=True, key='-2-')],
                [sg.Image('images/passiva.png', enable_events=True, key='-3-')],
                [sg.Image('images/skills.png', enable_events=True, key='-4-')],
                [sg.Image('images/splasharts.png', enable_events=True, key='-5-')],
                [sg.Image('images/back.png', enable_events=True, key='-BACK-')]]

    game = sg.Window('LoL Quiz', layout_game, background_color='#0a1e26')
    
    while True:
        event, values = game.read()
        lista = criaLista(CHAMPSIZE)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-1-':
            game.hide()
            pontos = 0
            jogador = sg.popup_get_text(
                'Insira o seu nome:', title='Cadastro da Pontuação', font='Arial 12', text_color='#e4b974', background_color='#0a1e26')
            tempo1 = datetime.datetime.now()
            if jogador == None:
                break
            for i in range(0, CHAMPSIZE):
                campeao = dados[lista[i]]
                aux = title_window(campeao, i)
                if aux == -1:
                    break
                else:
                    pontos = aux
            if aux == -1:
                break
            tempoDelta = datetime.timedelta(seconds=CHAMPSIZE)
            tempo2 = datetime.datetime.now()
            tempo = tempo2-tempoDelta-tempo1
            gravaRecorde('records\\recordesTitulo.txt', jogador, tempo, pontos)
            game.UnHide()
        elif event == '-2-':
            game.hide()
            pontos = 0
            jogador = sg.popup_get_text(
                'Insira o seu nome:', title='Cadastro da Pontuação',font='Arial 12', text_color='#e4b974', background_color='#0a1e26')
            tempo1 = datetime.datetime.now()
            if jogador == None:
                break
            for i in range(0, CHAMPSIZE):
                campeao = dados[lista[i]]
                aux = ultimate_window(campeao, i)
                if aux == -1:
                    break
                else:
                    pontos = aux
            if aux == -1:
                break
            tempoDelta = datetime.timedelta(seconds=CHAMPSIZE)
            tempo2 = datetime.datetime.now()
            tempo = tempo2-tempoDelta-tempo1
            gravaRecorde('records\\recordesUltimate.txt', jogador, tempo, pontos)
            game.UnHide()
        elif event == '-3-':
            game.hide()
            pontos = 0
            jogador = sg.popup_get_text(
                'Insira o seu nome:', title='Cadastro da Pontuação',font='Arial 12', text_color='#e4b974', background_color='#0a1e26')
            tempo1 = datetime.datetime.now()
            if jogador == None:
                break
            for i in range(0, CHAMPSIZE):
                campeao = dados[lista[i]]
                aux = passive_window(campeao, i)
                if aux == -1:
                    break
                else:
                    pontos = aux
            if aux == -1:
                break
            tempoDelta = datetime.timedelta(seconds=CHAMPSIZE)
            tempo2 = datetime.datetime.now()
            tempo = tempo2-tempoDelta-tempo1
            gravaRecorde('records\\recordesPassiva.txt', jogador, tempo, pontos)
            game.UnHide()
        elif event == '-4-':
            game.hide()
            pontos = 0
            jogador = sg.popup_get_text(
                'Insira o seu nome:', title='Cadastro da Pontuação',font='Arial 12', text_color='#e4b974', background_color='#0a1e26')
            tempo1 = datetime.datetime.now()
            if jogador == None:
                break
            for i in range(0, CHAMPSIZE):
                campeao = dados[lista[i]]
                aux = skills_window(campeao, i)
                if aux == -1:
                    break    
            if aux == -1:
                break
            tempoDelta = datetime.timedelta(seconds=CHAMPSIZE)
            tempo2 = datetime.datetime.now()
            tempo = tempo2-tempoDelta-tempo1
            gravaRecorde('records\\recordesSkills.txt', jogador, tempo, pontos)
            game.UnHide()
        elif event == '-5-':
            game.hide()
            pontos = 0
            jogador = sg.popup_get_text(
                'Insira o seu nome:', title='Cadastro da Pontuação', font='Arial 12', text_color='#e4b974', background_color='#0a1e26')
            tempo1 = datetime.datetime.now()
            if jogador == None:
                break
            for i in range(0, CHAMPSIZE):
                campeao = dados[lista[i]]
                aux = image_window(campeao, i)
                if aux == -1:
                    break
                pontos += aux
                
            tempoDelta = datetime.timedelta(seconds=CHAMPSIZE)
            tempo2 = datetime.datetime.now()
            tempo = tempo2-tempoDelta-tempo1
            gravaRecorde('records\\recordesImagem.txt', jogador, tempo, pontos)
            game.UnHide()
        elif event == '-BACK-':
            game.close()