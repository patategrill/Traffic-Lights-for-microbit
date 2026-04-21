from microbit import *
import radio 

radio.on()
radio.config(group=17)
display.clear()
#define constant diamond
diamond = Image('00900:'
                '09990:'
                '90909:'
                '09990:'
                '00900:')
#define constant complete_diamond
complete_diamond = Image('00900:'
                        '09990:'
                        '99999:'
                        '09990:'
                        '00900:')
def feu_vert():
    for _ in range(9):
         sleep(1000)
         display.show(Image.ARROW_N)
    sleep(1000)
    display.show(diamond)
    sleep(1000)
    display.show(complete_diamond)

def feu_rouge():
    for i in range(5,-1,-1):
          display.show(Image.NO)
          sleep(1000)
          display.show(i)
          sleep(1000)

def init() :
        feu_vert()
        feu_rouge()
        
while True :
    message = radio.receive()
    if message == "init":
        init()
    sleep(10)
