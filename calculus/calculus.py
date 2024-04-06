import numpy as np
import scipy as sp
import sympy as smp

#Symbols
def Var(v): #string
    return smp.symbols(v, real = True)

def Func(f):
    return smp.symbols(f, cls = smp.Function)

#Limits

def Limit(expression, x, goes, dir = 0):             #infinity = oo
    if dir == 0:
        return smp.limit(expression, x, goes )
    else:
        return smp.limit(expression, x, goes, dir = dir )

#Convert text to Numerical
def Num(text, arg):                 #arg = tuple
    return smp.lambdify(arg, text)

#Derivatives

def Derive(expression, x, order =1):
    return smp.diff(expression, x, order)

from scipy.misc import derivative

def NDerive(expression_func, x, order=1):
    return derivative(expression_func, x, dx = 1e-6, n=order)

def DataDerive(y_data, x_data):
    return np.gradient(y_data ,x_data)

#Integrals

def Integrate(expression, x):
    return smp.integrate(expression, x)

from scipy.integrate import quad 

def NIntegrate(expression_func, x,  bounds):
    a, b = bounds
    integral, integral_error = quad(expression_func, a, b)

    return (integral, integral_error)

def DataIntegrate(y_data, x_data):
    return np.cumsum(y_data)* (x_data[1] - x_data[0])

#Series

def Sum(expression, n, bounds):
    a, b = bounds
    return smp.Sum(expression(n, a, b)).doit()

def NSum(expression, n, bounds):
    a, b = bounds
    return smp.Sum(expression(n, a, b)).n()