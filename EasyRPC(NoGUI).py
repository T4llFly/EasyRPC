from pypresence import Presence
import time

clientID = input('Введите ваш Client ID: ')
RPC = Presence(clientID)

state = input()
details = input()
labelofbutton = input()
urlofbutton = input()

RPC.connect()

RPC.update(state, details, buttons=[{"label": labelofbutton, "url": urlofbutton}])

while True:
    time.sleep(15)