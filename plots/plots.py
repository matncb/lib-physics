import matplotlib.pyplot as plt
import numpy as np
import scienceplots

plt.style.use(['science', 'notebook', 'grid'])

def Plot(x, y, x_label, y_label):
    plt.figure(figsize = (10, 3))
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

def PlotData(x, y, x_label, y_label):
    plt.figure(figsize = (10, 3))
    plt.plot(x, y, 'o', ms= 5)
    plt.xlabel(x_label)
    plt.ylabel(y_label)