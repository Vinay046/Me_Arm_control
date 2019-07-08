import tkinter as tk
import itertools
import serial

#ser = serial.Serial('COM3',9600)
global button_state 

def toggle(icycle=itertools.cycle(['Release','Grab'])):
    state = next(icycle)
    button1['text'] = str(state)
    message = "@"+str(w1.get())+","+str(w2.get())+","+str(w3.get())+","+button1['text']+"!"
    #ser.write(message.encode())
    print(message)

def show_values(self):
    message = "@"+str(w1.get())+","+str(w2.get())+","+str(w3.get())+button1['text']+"!"
    #ser.write(message.encode())
    print(message)

master = tk.Tk()

master.geometry("700x250")
master.resizable(0,0)

master.title("Servo Angle Control")

w1 = tk.Scale(master, from_=0, to=180,length = 600,tickinterval=90, orient=tk.HORIZONTAL,command = show_values)
w1.set(0)
w1.pack()

w2 = tk.Scale(master, from_=0, to=180,length = 600,tickinterval=90, orient=tk.HORIZONTAL,command = show_values)
w2.set(0)
w2.pack()

w3 = tk.Scale(master, from_=0, to=180,length = 600,tickinterval=90, orient=tk.HORIZONTAL,command = show_values)
w3.set(0)
w3.pack()

button1 = tk.Button(master,text = 'Grab', command=toggle)
button1.pack()

master.mainloop()