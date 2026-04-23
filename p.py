import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3,4])
h=np.array([1,1,-1])
M=len(x)
N=len(h)
L=M+N-1
y_conv=np.zeros(L)
def convolution(x,h):
    for n in range(L):
        for k in range(M):
            if 0<=n-k<N:
                y_conv[n]+=x[k]*h[n-k]
    return y_conv
value=convolution(x,h)
print(value)

def dft(x):
    
    L=len(x)
    X=np.zeros(L,dtype=complex)
    for k in range(L):
        for n in range(L):
            X[k]+=x[n]*np.exp(-2j*np.pi*n*k/L)        
    return X
value2=dft(x)
print(value2)
value3=dft(h)
print(value3)    
def idft(x):
    L=len(x)
    X=np.zeros(L,dtype=complex)
    for n in range(L):
        for k in range(L):
            X[n]+=x[k]*np.exp(2j*np.pi*k*n/L)
        X[n]=X[n]/L
    return X
value4=idft(x)
print(value4)
value5=idft(h)
print(value5)
x_pad=np.zeros(L)
h_pad=np.zeros(L)
x_pad[:M]=x
h_pad[:N]=h

X=dft(x_pad)
H=dft(h_pad)
Y=X*H
val=idft(Y)
print(val)

plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.stem(val)
plt.title("convolution in fq domain")
plt.grid()

plt.subplot(2,1,2)
plt.stem(y_conv)
plt.title("convolution in time domain")
plt.grid()

plt.tight_layout()
plt.show()

           
            

            
            
    
    