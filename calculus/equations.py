import numpy as np
import scipy as sp

#Differential equations

from scipy.integrate import odeint
from scipy.integrate import solve_ivp

def DSolve(dSdx, x, S0, solver = 'odeint', method = None, rtol = 1e-3, atol = 1e-6):

    if solver == 'odeint':
        basic = odeint(dSdx, y0 = S0, t = x, tfirst= True).T
        return basic

    elif solver == 'ivp':
        if method == None:
            ivp = solve_ivp(dSdx, t_span=(0, max(x)), y0 = S0, t_eval = x).y
        else:
            ivp = solve_ivp(dSdx, t_span=(0, max(x)), y0 = S0, t_eval = x, method = method, rtol =rtol, atol=atol).y   
        return ivp

    else:
        print("Error: this is not a solver")

#method = 'DOP853', rtol =1e-10, atol=1e-13 