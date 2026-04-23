import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3],dtype=float)
h=np.array([1,2,1],dtype=float)

M=len(x)
N=len(h)
L=M+N-1

y_conv=np.zeros(L)

for n in range(L):
    for k in range(M):
        if 0<=n-k<N:
            y_conv[n]+=x[k]*h[n-k]
            
def dft(signal):
    L=len(signal)
    X=np.zeros(L,dtype=complex)
    for k in range(L):
        for n in range(L):
            X[k]+=signal[n]*np.exp(-2j*np.pi*k*n/L)
    return X
def idft(signal):
    L=len(signal)
    X=np.zeros(L,dtype=complex)
    for n in range(L):
        for k in range(L):
            X[n]+=signal[k]*np.exp(2j*np.pi*k*n/L)
        X[n]=X[n]/L
    return X
x_pad=np.zeros(L)
h_pad=np.zeros(L)
x_pad[:M]=x
h_pad[:N]=h

X=dft(x_pad)
H=dft(h_pad)

Y=X*H
y_freq=idft(Y)

print("Time domain convolution")
print(y_conv)

print("frequency domain")
print(np.real(y_freq))

plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.stem(y_conv)
plt.title("Time convolution x[n]*h[n]")
plt.grid()

plt.subplot(2,1,2)
plt.stem(np.real(y_freq))
plt.title("Frequency domain X[k].H[k]")
plt.grid()

plt.tight_layout()
plt.show()                            