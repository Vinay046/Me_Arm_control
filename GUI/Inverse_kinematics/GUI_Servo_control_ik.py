import tkinter as tk
import itertools
import serial
from inverse import *


ser = serial.Serial('COM3',9600)

angles_to_send = [0,0,0]

def toggle(icycle=itertools.cycle(['Release','Grab'])):
    state = next(icycle)
    button1['text'] = str(state)
    inverse_kin(w1.get(),w2.get(),w3.get(),angles_to_send)
    message = "@"+str(math.degrees(angles_to_send[0]))+","+str(math.degrees(angles_to_send[1])+90)+","+str(math.degrees(angles_to_send[2])+90)+","+button1['text']+"!"
    #print(message)
    ser.write(message.encode())

def show_values(self):
	inverse_kin(w1.get(),w2.get(),w3.get(),angles_to_send)
	message = "@"+str(math.degrees(angles_to_send[0]))+","+str(math.degrees(angles_to_send[1])+90)+","+str(math.degrees(angles_to_send[2])+90)+","+button1['text']+"!"
	#print(message)
	ser.write(message.encode())
    

master = tk.Tk()

master.geometry("900x250")
master.resizable(0,0)

master.title("Grabber Location control")

w1 = tk.Scale(master, from_=-320, to=320,length = 700,tickinterval=320, orient=tk.HORIZONTAL,command = show_values)
w1.set(0)
w1.pack()

w2 = tk.Scale(master, from_=0, to=320,length = 700,tickinterval=320, orient=tk.HORIZONTAL,command = show_values)
w2.set(175)
w2.pack()

w3 = tk.Scale(master, from_=-50, to=150,length = 700,tickinterval=50, orient=tk.HORIZONTAL,command = show_values)
w3.set(0)
w3.pack()

button1 = tk.Button(master,text = 'Grab', command=toggle)
button1.pack()

master.mainloop()