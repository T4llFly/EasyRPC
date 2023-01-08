from pypresence import Presence
import time
import PySimpleGUI as sg

layout1 = [  [sg.Text('Введите ваш Client ID, чтобы EasyRPC смог начать свою работу')],
            [sg.InputText()],
            [sg.Text(size=(15,1),  key='-OUTPUT-')],
            [sg.Button('Войти'), sg.Button('Закрыть')] ]

win1 = sg.Window('Введите ваш Client ID', layout1)

win2_active=False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == sg.WIN_CLOSED:
        break
    win1.find_element('-OUTPUT-').update(vals1[0])

    if ev1 == 'Войти'  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Добро пожаловать в EasyRPC')],
                   [sg.Button('Применить'), sg.Button('Закрыть')]]

        win2 = sg.Window('EasyRPC v0.1', layout2)
        while True:
            ev2, vals2 = win2.read()
            if ev2 == sg.WIN_CLOSED or ev2 == 'Закрыть':
                win2.close()
                win2_active = False
                break
