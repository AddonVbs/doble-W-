import keyboard as ky
from colorama import Fore, Back, Style
lock = False 
while True:

    def on_press_w(event):
        if lock == True:
            ky.press("ctrl")  

    def on_release_w(event):
        if lock == True:
            ky.release("ctrl")  


    ky.on_press_key("w", on_press_w)
    ky.on_release_key("w", on_release_w)

    while True:
        ky.wait("alt")  

        lock = not lock  
        if lock:
            print(Fore.GREEN+"Автобег включен")

        else:
            print(Fore.RED+"Автобег выключен")  