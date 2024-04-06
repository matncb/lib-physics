import numpy as np
import scipy as sp

#Interpolation

from scipy.interpolate import interp1d

def Interpolate(x_data, y_data, interpolation_kind):
    f = interp1d(x_data,y_data, kind = interpolation_kind)   #interpolation_kind = linear, cubic, ...
    return f

# curve fitting

from scipy.optimize import curve_fit

def Fit(x_data, y_data, f , p0):      #f(x,a,b) = a * x**2 + b*x
    parameters, error_matrix = curve_fit(f, x_data, y_data, p0 = p0) #error_matrix = covariant_matrix
    return (parameters, np.sqrt(np.diag(error_matrix)))


#Statistics

def Std(A):
    return np.std(A)

# Add noise (badly)

def Noise(A, force = 1):
    return A + force *np.random.randn(len(A))
