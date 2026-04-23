import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,3],dtype=float)
h=np.array([1,1],dtype=float)

N=len(x)
M=len(h)
L=N+M-1

y_conv=np.zeros(L)

for n in range(L):
    for k in range(N):
        if 0<=n-k<M:
            y_conv[n]+=x[k]*h[n-k]


def DFT(signal):
    L=len(signal)
    X=np.zeros(L,dtype=complex)

    for k in range(L):
        for n in range (L):
            X[k]+=signal[n]*np.exp(-2j*np.pi*k*n/L)
    
    return X

def IDFT(X):
    L=len(X)
    x=np.zeros(L,dtype=complex)


    for n in range(L):
        for k in range(L):
            x[n]+=X[k]*np.exp(2j*np.pi*k*n/L)
        x[n]=x[n]/L
    return x 

x_pad=np.zeros(L)
h_pad=np.zeros(L)

x_pad[:N]=x
h_pad[:M]=h

X=DFT(x_pad)
H=DFT(h_pad)

Y=X*H
y_freq=IDFT(Y)

print("Time domain convolution: ")
print(y_conv)

print("\nFrequency domain result: ")
print(np.real(y_freq))

plt.figure(figsize=(8,8))

plt.subplot(2,1,1)
plt.stem(y_conv)
plt.title("Time Domain Convolution x[n]*h[n]")

plt.subplot(2,1,2)
plt.stem(np.real(y_freq))
plt.title("Frequency Domain Result (IDFT of X[k]·H[k])")

plt.tight_layout()
plt.show()