import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

def dSdt(t,S):
    th,y,x,z = S
    return[y,(2*sp.constants.g*np.sin(th)-y*y*np.sin(th)*np.cos(th))/(1+(np.sin(th))*np.sin(th)),z,(sp.constants.g*np.sin(th)*np.cos(th)-y*y*np.sin(th))/(1+(np.sin(th))*np.sin(th))]

th_0 = 0.1
y_0 = 0 
x_0 = 0
z_0 = 0
S_0 = (th_0,y_0,x_0,z_0)

t = np.linspace(0,1,1000)
sol = odeint(dSdt,y0=S_0,t=t,tfirst=True)

plt.plot(t,sol.T[0])
plt.plot(t,sol.T[1])
plt.plot(t,sol.T[2])
plt.plot(t,sol.T[3])

plt.legend(["theta","omega","x","Vcart"])

plt.show()