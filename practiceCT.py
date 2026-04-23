import numpy as np
import matplotlib.pyplot as plt

fs=8000
fc=1000
N=21

wc=2*np.pi*fc/fs
M=(N-1)//2
hd=np.zeros(N)
for n in range(N):
    if n==M:
        hd[n]=wc/np.pi
    else:
        hd[n]=np.sin(wc*(n-M))/(np.pi*(n-M))   
w=np.zeros(N)
for n in range(N):
    w[n]=0.54-0.46*np.cos((2*np.pi*n)/(N-1))
h=w*hd  
plt.figure()
plt.stem(h)
plt.show()

def dft(x):
    L=len(x)
    X=np.zeros(L,dtype=complex)
    for k in range(L):
        for n in range(L):
            X[k]+=x[n]*np.exp(-2j*np.pi*n*k/L)
    return X
value=dft(h)
magnitude=np.abs(value)
print(magnitude)
phase=np.angle(value)
print(phase)
        
plt.figure()
plt.stem(magnitude)
plt.show()

plt.figure()
plt.stem(phase)
plt.show()        
