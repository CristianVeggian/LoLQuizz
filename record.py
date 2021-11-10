
from time import strptime
import PySimpleGUI as sg
from random import randint

win_w = 500
win_h = 75


def pontuacao_table(pontuacoes):

    layout = [[sg.Text('Tempo\t\t\tPontos\t\t\tNome', pad=(win_w/4, 0), font='Arial 14', text_color='#e4b974', background_color='#0a1e26')]]
    for i in pontuacoes:
        pessoa = i.split('#')
        layout.append([sg.Text(pessoa[1]+'\t\t\t'+pessoa[2].replace('\n','')+'\t\t\t' + pessoa[0], pad = (win_w/4, 0), font='Arial 12', text_color='#e4b974', background_color='#0a1e26')])
    layout.append([sg.Image('images/back.png', enable_events=True, key='-BACK-')])

    window = sg.Window('Maiores Pontuações', layout, background_color='#0a1e26')

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED or event == '-BACK-':
            window.close()
            break


def ver_recorde():

    layout_record = [[sg.Image('images/titulo.png', enable_events=True, key='-1-')],
                [sg.Image('images/ultimate.png', enable_events=True, key='-2-')],
                [sg.Image('images/passiva.png', enable_events=True, key='-3-')],
                [sg.Image('images/skills.png', enable_events=True, key='-4-')],
                [sg.Image('images/splasharts.png', enable_events=True, key='-5-')],
                [sg.Image('images/back.png', enable_events=True, key='-BACK-')]]

    table = sg.Window('LoL Quiz: Recordes', layout_record, background_color='#0a1e26')

    while True:
        event, values= table.read()

        if event == sg.WIN_CLOSED or event == '-BACK-':
            table.close()
            break
        if event == '-1-':
            arquivo= open('records/recordesTitulo.txt', 'r', encoding='utf-8')
            pontuacoes = []
            for line in arquivo:
                pontuacoes.append(line)
                if len(pontuacoes) == 10:
                    break
            pontuacao_table(pontuacoes)
        elif event == '-2-':
            arquivo= open('records/recordesUltimate.txt', 'r', encoding='utf-8')
            pontuacoes = []
            for line in arquivo:
                pontuacoes.append(line)
                if len(pontuacoes) == 10:
                    break
            pontuacao_table(pontuacoes)
        elif event == '-3-':
            arquivo= open('records/recordesPassiva.txt', 'r', encoding='utf-8')
            pontuacoes = []
            for line in arquivo:
                pontuacoes.append(line)
                if len(pontuacoes) == 10:
                    break
            pontuacao_table(pontuacoes)
        elif event == '-4-':
            arquivo= open('records/recordesSkills.txt', 'r', encoding='utf-8')
            pontuacoes = []
            for line in arquivo:
                pontuacoes.append(line)
                if len(pontuacoes) == 10:
                    break
            pontuacao_table(pontuacoes)
        elif event == '-5-':
            arquivo= open('records/recordesImagem.txt', 'r', encoding='utf-8')
            pontuacoes = []
            for line in arquivo:
                pontuacoes.append(line)
                if len(pontuacoes) == 10:
                    break
            pontuacao_table(pontuacoes)