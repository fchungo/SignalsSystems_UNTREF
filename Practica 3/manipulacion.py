import numpy as np

def desplaza(x, fs, t0):
    N = len(x)
    d = t0*fs
    x2 = np.zeros(N)

    if d > 0:
        for i in range(0,N-int(d)):
            x2[int(i+d)]=x[i]
    else:
        for i in range(0,N+int(d)):
            x2[i]=x[int(i-d)]

    return x2
    
def girodesplaza(x, fs, t0, Giro):

    N = len(x)
    d = t0*fs

    if Giro == 1:
        x = np.flipud(x)

    x2 = np.zeros(N)

    if d > 0:
        for i in range(0,N-int(d)):
            x2[int(i+d)]=x[i]
    else:
        for i in range(0,N+int(d)):
            x2[i]=x[int(i-d)]

    return x2
    
def desplazagiro(x, fs, t0, Giro):

    N = len(x)
    d = t0*fs
    x2 = np.zeros(N)

    if d > 0:
        for i in range(0,N-int(d)):
            x2[int(i+d)]=x[i]
    else:
        for i in range(0,N+int(d)):

            x2[i]=x[int(i-d)]

    if Giro == 1:
        x2 = np.flipud(x2)

    return x2