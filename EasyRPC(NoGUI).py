from pypresence import Presence
import time

clientID = input('Введите ваш Client ID: ')
RPC = Presence(clientID)

state = input('Введите название Rich Presence: ')
details = input('Введите описание Rich Presence: ')
labelofbutton = input('Введите название кнопки Rich Presence: ')
urlofbutton = input('Куда ведет ваша кнопка: ')

RPC.connect()

RPC.update(state, details, buttons=[{"label": labelofbutton, "url": urlofbutton}])

while True:
    time.sleep(15)