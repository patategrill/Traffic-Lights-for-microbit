from microbit import *
import radio

radio.on()
radio.config(group=17)
croix = (Image( '90009:'
                '09090:'
                '00900:'
                '09090:'
                '90009'))
def feu_rouge():
    for i in range(5,-1,-1):
        """affiche le décompte du feu"""
        display.show(croix)
        sleep(1000)
        display.show(i)
        sleep(1000)

def feu_vert():
    for _ in range(9):
         sleep(1000)
         display.show(Image.ARROW_N)
    sleep(1000)
    display.show(losange)
    sleep(1000)
    display.show(losange_complet)

def init() :
        radio.send("init")
        sleep(10)
        feu_rouge()
        feu_vert()

if button_a.is_pressed(): 
    while True:
        message = radio.receive()
        if message == "go":
            init()
