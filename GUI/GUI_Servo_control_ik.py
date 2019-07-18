import math
import tkinter as tk
import itertools
import serial

L1 =160
L2 =160
L3 =20

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
    
def cart2polar(x,y):
	r = math.hypot(x,y)
	if r == 0:
		return

	c=x/r
	s=y/r

	if s > 1: s = 1
	if c > 1: c = 1
	if s < -1: s = -1
	if c < -1: c = -1

	theta = math.acos(c)

	if s<0:theta = -theta

	return r,theta

def cosangle(opp, adj1, adj2, theta):	
    den = 2 * adj1 * adj2
	
    if den == 0:
        return False
    c = (adj1 * adj1 + adj2 * adj2 - opp * opp)/den
    if c > 1 or c < -1:
        return False
    theta[0] = math.acos(c)
    return True

def inverse_kin(x, y, z, angles):
    r, th0 = cart2polar(x,y)
    r -= L3 
    R, ang_P = cart2polar(r, z)
    print(r)
    parmB = [0]
    parmC = [0]
	
    if not cosangle(L2, L1, R, parmB): return False
    if not cosangle(R, L1, L2, parmC): return False
    B = parmB[0]
    C = parmC[0]
    if r < 80:
    	a0 = th0
    	a1 = math.radians(5)
    	a2 = math.radians(5)
    else:
	    a0 = th0
	    a1 = math.pi/2-(ang_P + B)
	    a2 = C - a1
	
    angles[0] = a0
    angles[1] = a1
    angles[2] = a2
	
    return True

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