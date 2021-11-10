import PySimpleGUI as sg
from game import jogar
from record import ver_recorde

win_w = 500
win_h = 75

sg.set_options(background_color='#0a1e26',
       text_element_background_color='#0a1e26',
       text_color='#e4b974',
       element_background_color='#0a1e26',
       input_elements_background_color='#F7F3EC',
       button_color=('white','#e4b974'))

layout_menu = [[sg.Image('images/play.png', enable_events=True, key='-PLAY-'), sg.Image('images/recordes.png', enable_events=True, key='-RECORDS-', pad=((win_w/4,0),0))]]

menu = sg.Window('LoL Quiz', layout_menu, background_color='#0a1e26', size=(win_w,win_h))

while True:
    event, values = menu.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-PLAY-':
        menu.hide()
        jogar()
        menu.UnHide()
    elif event == '-RECORDS-':
        menu.hide()
        ver_recorde()
        menu.UnHide()
