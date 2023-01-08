from pypresence import Presence
import time
import os

clientID = input('Введите ваш Client ID: ')
RPC = Presence(clientID)

pid = os.getpid()
details = input('Введите название Rich Presence: ')
state = input('Введите описание Rich Presence: ')
labelofbutton = input('Введите название кнопки Rich Presence: ')
urlofbutton = input('Куда ведет ваша кнопка: ')

RPC.connect()

RPC.update(pid, state, details, buttons=[{"label": labelofbutton, "url": urlofbutton}])

while True:
    time.sleep(15)