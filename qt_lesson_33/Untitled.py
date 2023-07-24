#!/usr/bin/env python3

#lib for working with serial port (usb)
import serial 

import time

#lib for working with GUI
from tkinter import * 

#class for working with serial port
#note: constructor return -1, if it can't open port
class Port():
    #variables of class
    serial_speed = 9600 #variable with speed of read(write) data from(in) serial port (bytes/second)
    error_message = "Error: can't open port" #message, for situations, when program can't open port
    usb_path = "/dev/ttyUSB0" #path to usb in fs (linux)
    values_for_send = [b'0', b'1']

    def __init__(self): #overloaded constructor (without arguments)
        try:
            self.port = serial.Serial(self.usb_path, self.serial_speed)
        except:
            print(self.error_message)
            return -1


    def __init__(self, _timeout): #overloaded constructor (with timeout for opening)
        try:
            self.port = serial.Serial(self.usb_path, self.serial_speed, timeout=_timeout)
        except:
            print(self.error_message)
            return -1


    def __init__(self, _timeout, _error_msg_on): #overloaded constructor (with timeout for opening and switch for on/off error message)
        try:
            self.port = serial.Serial(self.usb_path, self.serial_speed, timeout=_timeout)
        except:
            if (_error_msg_on == True):
                print(self.error_message)
                return -1

    
    def __init__(self, _timeout, _error_msg_on, _speed): #overloaded constructor (with timeout for opening, switch for on/off error message and speed (b/s))
        try:
            self.port = serial.Serial(self.usb_path, _speed, timeout=_timeout)
        except:
            if (_error_msg_on == True):
                print(self.error_message)
                return -1

    #two methods for on/off led
    def send_high(self):
        self.port.write(self.values_for_send[1])

    def send_low(self):
        self.port.write(self.values_for_send[0])


class Switch(): #class with methods, which working, when user clic on buttons (tkinter), for on/of led
    log_for_on = "LED on"
    log_for_off = "LED off"
    delay = 2 #time for open port

    def __init__(self):
        self.my_port = Port(self.delay, True, 9600)

    def switch_on_led(self):
        self.my_port.send_high()
        print("Logs: " + self.log_for_on)

    def switch_off_led(self):
        self.my_port.send_low()
        print("Logs: " + self.log_for_off)


#class for creating and config window with name "Test"
class Window():
    switch = Switch() #object(Switch)


    #variables for creating
    window_size = "720x480"
    window_name = "Test"
    window_background = "lightblue"
    window_resizable_x = False
    window_resizable_y = False

    #button "on"
    button_on_text = "ON"
    button_on_width = 10
    button_on_heigh = 5
    button_on_background = "green"
    button_on_fontground = "black"
    button_on_x = 180
    button_on_y = 150

    #button "off"
    button_off_text = "OFF"
    button_off_width = 10
    button_off_heigh = 5
    button_off_background = "red"
    button_off_fontground = "black"
    button_off_x = 440
    button_off_y = 150


    def __init__(self):
        root = Tk() #main object - "root"self
        root.geometry(self.window_size)
        root.title(self.window_name)
        root.config(bg=self.window_background)
        root.resizable(self.window_resizable_x, self.window_resizable_y)
    
        #creating and config button with name "ON"
        button_on = Button(root, text=self.button_on_text, width=self.button_on_width, height=self.button_on_heigh, bg=self.button_on_background, fg=self.button_on_fontground, command=self.switch.switch_on_led)
        button_on.place(x=self.button_on_x, y=self.button_on_y)

        #creating and config button with name "OFF"
        button_off = Button(root, text=self.button_off_text, width=self.button_off_width, height=self.button_off_heigh, bg=self.button_off_background, fg=self.button_off_fontground, command=self.switch.switch_off_led)
        button_off.place(x=self.button_off_x, y=self.button_off_y)

        root.mainloop() #calling method for window no close





window = Window()

#constructor with object other class
# 4 construstor? but no 1 ?