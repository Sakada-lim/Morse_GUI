from tkinter import * 
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

BRate=0.25

## hardware
blue = LED(4)

## MORSE CODE BLINKER ##
def morse_dash():
    blue.on()
    time.sleep(4*BRate)
    blue.off()
    time.sleep(BRate)

def morse_pause():
    time.sleep(BRate)

def morse_dot():
    blue.on()
    time.sleep(BRate)
    blue.off()
    time.sleep(BRate)
    


## MORSE CODE TRANSLATION ## 

def convertToMorseCode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += CODE[character] + " " 
    return encodedSentence
    
## MORSE CODE LIBRARY ##
CODE = {' ': '_', 
"'": '.----.', 
'(': '-.--.-', 
')': '-.--.-', 
',': '--..--', 
'-': '-....-', 
'.': '.-.-.-', 
'/': '-..-.', 
'0': '-----', 
'1': '.----', 
'2': '..---', 
'3': '...--', 
'4': '....-', 
'5': '.....', 
'6': '-....', 
'7': '--...', 
'8': '---..', 
'9': '----.', 
':': '---...', 
';': '-.-.-.', 
'?': '..--..', 
'A': '.-', 
'B': '-...', 
'C': '-.-.', 
'D': '-..', 
'E': '.', 
'F': '..-.', 
'G': '--.', 
'H': '....', 
'I': '..', 
'J': '.---', 
'K': '-.-', 
'L': '.-..', 
'M': '--', 
'N': '-.', 
'O': '---', 
'P': '.--.', 
'Q': '--.-', 
'R': '.-.', 
'S': '...', 
'T': '-', 
'U': '..-', 
'V': '...-', 
'W': '.--', 
'X': '-..-', 
'Y': '-.--', 
'Z': '--..', 
'_': '..--.-'}

## GUI DEFINITIONS ##

win = Tk()
## GUI FUNCTION##
def get_morse_code():
    x1 = entry.get()
    encodedSentence = convertToMorseCode(x1)
    label = Label(win, text =encodedSentence)
    label.pack()
    for i in encodedSentence:
        if i == ".":
            morse_dot()
        elif i == "-":
            morse_dash()
        else:
            morse_pause()
    

## WIDGET##
entry = Entry(win)
entry.pack()
button = Button(win, text = "get more code", command = get_morse_code)
button.pack()

win.mainloop()

