import numpy as np
import matplotlib.pyplot as plt

def system_response(x):
    L=len(x)
    y=np.zeros(L,dtype=complex)
    
    for n in range(L):
        y[n]=x[n]
        
        if n-3>=0:
            y[n]+=x[n]
    return y

N=32
x=np.zeros(N)
x[0]=1
h=system_response(x)
def dft(x):
     L=len(x)
     X=np.zeros(L)
     for k in range(L):
         for n in range(L):
             X[k]+=x[n]*np.exp(-2j*np.pi*n*k/L)
     return X
H=dft(h)
mag=np.abs(H)

half=mag[:N//2]
if np.all(np.diff(half)<=0):
    print("Low pass filter")
else:
    print("Not a low pass filter")
k=np.arange(N)
plt.figure()
plt.stem(k,mag)
plt.title("magnitude response")
plt.grid()
plt.show()
 


 
                