import numpy as np
import matplotlib.pyplot as plt
f=10
fs=100
t=np.arange(0,1,1/fs)
x=np.cos(2*np.pi*f*t)

def dft(x):
    L=len(x)
    X=np.zeros(L,dtype=complex)
    for k in range(L):
        for n in range(L):
            X[k]+=x[n]*np.exp(-2j*np.pi*k*n/L)
    return X
val=dft(x)
mag1=np.abs(val)
print(val) 
    
plt.figure()
plt.stem(mag1)
plt.show()   

t1=np.arange(0,0.95,1/fs)
x1=np.sin(2*np.pi*f*t1)
val2=dft(t1)
mag2=np.abs(val2)
plt.figure()
plt.stem(mag2)
plt.show()


def hamming(l):
    w=np.zeros(l)
    for n in range(l):
        w[n]=0.54-0.56*np.cos((2*np.pi*n)/(l-1))
    return w
N=len(x1)
hh=hamming(N)
ww = hh*x1
result=dft(ww)
mag3=np.abs(result)
print(result)   
plt.figure()
plt.stem(mag3)
plt.show()
        