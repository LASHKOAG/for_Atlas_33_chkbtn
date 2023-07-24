#!/usr/bin/env python3

import serial #lib for working with serial port (usb)
import time
from tkinter import * #lib for working with GUI

#varriables
serial_speed = 9600 #variable with speed of read(write) data from(in) serial port (bytes/second)

#class for working with serial port
#note: constructor return 0, if port open successfull, else, it return -1
class Port():
    def __init__(self): #overloaded constructor (without arguments)
        try:
            self.port = serial.Serial("/dev/ttyUSB0", 9600)
            #return 0
            #self.ser_speed = 9600
        except:
            print("Error: can't open port")
            return -1

    #two methods for on/off led
    def send_high(self):
        self.port.write(b"1")#'' 

    def send_low(self):
        self.port.write(b"0")

    def send_blink_blue(self):
        self.port.write(b"2")
    
    def send_blink_white(self):
        self.port.write(b"3")

# port = Port(10, True, serial_speed) #object(Port)
#port = Port() #object(Port)


#creating and config window with name "Test"
root = Tk() #main object - "root"
root.geometry("720x480")
root.title("Test")
root.config(bg="lightblue")
root.resizable(False, False) 


class Switch(): #class with methods, which working, when user clic on buttons (tkinter), for on/of led
    
    
    def __init__(self):
        # pass
        self.port2 = Port() #object(Port)

    def switch_on_led(self):
        if blinkState_white.get()==1:
            self.blink_led_white()
        else:
            self.port2.send_high()
            print("Logs: LED on")

    def switch_off_led(self):
        self.port2.send_low()
        print("Logs: LED off")


    def blink_led_blue(self):
        print("Logs: blinkState " + str(blinkState.get()))
        if blinkState.get() == 1:
            self.port2.send_blink_blue()
            print("Logs: Blue led start blink")

    def blink_led_white(self):
        print("Logs: blinkState_white" + str(blinkState_white.get()))
        if blinkState_white.get() == 1:
            self.port2.send_blink_white()
            print("Logs: White led start blink")


switch = Switch() #object(Port)



def print_something(event):
    lbl_test.config(text="lalala")


#creating and config button with name "ON"
button_on = Button(root, text="ON", width=10, height=5, bg="green", fg="black", command=switch.switch_on_led)
button_on.place(x=180, y=150)

#creating and config button with name "OFF"
button_off = Button(root, text="OFF", width=10, height=5, bg="red", fg="black", command=switch.switch_off_led)
button_off.place(x=440, y=150)

lbl_photoresistor = Label(root, text="Photoresistor data: ", font="Arial 14", bg="lightblue" , fg="black")
lbl_photoresistor.place(x=180, y=300)

lbl_thermoresistor = Label(root, text="Thermoresistor data: ", font="Arial 14", bg="lightblue" , fg="black")
lbl_thermoresistor.place(x=180, y=350)

lbl_ultrasonic = Label(root, text="Ultrasonic data: ", font="Arial 14", bg="lightblue" , fg="black")
lbl_ultrasonic.place(x=180, y=400)

lbl_test = Label(root, text="800", font="Arial 14")
lbl_test.place(x=350, y=300)


ent = Entry(root, width=20, bd=2)
ent.pack()

#bind

button_on.bind("<Button-3>", print_something)


blinkState=IntVar()
# chkBtn_blink=Checkbutton(root, text="Run blink blue", variable=blinkState, command=switch.blink_led_blue)
chkBtn_blink=Checkbutton(root, text="Run blink blue", variable=blinkState)
chkBtn_blink.pack()

blinkState_white = IntVar()
# chkBtnWhite_blink=Checkbutton(root, text="Run blink white", variable=blinkState_white, command=switch.blink_led_white)
chkBtnWhite_blink=Checkbutton(root, text="Run blink white", variable=blinkState_white)
chkBtnWhite_blink.pack()

root.mainloop() #calling method for window no close

#ToDo class +
#button_off  x=440, y=150 +
#@ -