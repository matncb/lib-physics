import numpy as np

def Dot(A,B):
    return np.dot(A,B)

def Cross(A,B):
    return np.cross(A,B)

def Multiply(A, B):
    return A@B

def Eingen(A):
    values, vectors = np.linalg.eig(A)
    return (values, vectors.T)