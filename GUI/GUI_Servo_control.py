import tkinter as tk
def show_values():
    print (w1.get(), w2.get(), w3.get())
def grab():
	print("Grabbed the object")

master = tk.Tk()

master.geometry("700x300")
master.resizable(0,0)
master.title("Servo Angle Control")
w1 = tk.Scale(master, from_=0, to=180,length = 600,tickinterval=180, orient=tk.HORIZONTAL)
w1.set(0)
w1.pack()
w2 = tk.Scale(master, from_=0, to=180,length = 600,tickinterval=180, orient=tk.HORIZONTAL)
w2.set(0)
w2.pack()
w3 = tk.Scale(master, from_=0, to=180,length = 600,tickinterval=180, orient=tk.HORIZONTAL)
w3.set(0)
w3.pack()
label1 = tk.Label(master,text="")
label1.pack()
tk.Button(master, text='Show', command=show_values).pack()
label2 = tk.Label(master,text="")
label2.pack()
tk.Button(master, text='GRAB', command=grab).pack()
label3 = tk.Label(master,text="")
label3.pack()

master.mainloop()