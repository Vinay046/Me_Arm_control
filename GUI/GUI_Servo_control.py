from tkinter import *

def show_values():
    print (w1.get(), w2.get(), w3.get())
def grab():
	print("Grabbed the object")
master = Tk()
master.title("Servo Angle Control")
w1 = Scale(master, from_=0, to=180,length = 600,tickinterval=10, orient=HORIZONTAL)
w1.set(0)
w1.pack()
w2 = Scale(master, from_=0, to=180,length = 600,tickinterval=10, orient=HORIZONTAL)
w2.set(0)
w2.pack()
w3 = Scale(master, from_=0, to=180,length = 600,tickinterval=10, orient=HORIZONTAL)
w3.set(0)
w3.pack()
label1 = Label(master,text="")
label1.pack()
Button(master, text='Show', command=show_values).pack()
label2 = Label(master,text="")
label2.pack()
Button(master, text='GRAB', command=grab).pack()

mainloop()