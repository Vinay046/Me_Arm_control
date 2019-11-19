import math

L1 =160
L2 =160
L3 =20

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