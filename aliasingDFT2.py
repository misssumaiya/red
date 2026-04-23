import numpy as np
import matplotlib.pyplot as plt

fs=100
N=100

n=np.arange(N)
t=n/fs

x1=np.sign(2*np.pi*30*t)
x2=np.sin(2*np.pi*70*t)

def dft(x):
    N=len(x)
    X=np.zeros(N,dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k]+=x[n]*np.exp(-1j*2*np.pi*k*k/N)
    return X
X1=dft(x1)
X2=dft(x2)

k=np.arange(N)
freq=k*fs/N

magnitude1=np.abs(X1)
magnitude2=np.abs(X2)

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.stem(freq,magnitude1)
plt.title("DFT magnitude of spectrum of 30 hz signal")
plt.xlabel("Frequency in HZ")
plt.ylabel("X(k)")
plt.grid()

plt.subplot(2,1,2)
plt.stem(freq,magnitude2)
plt.title("DFT magnitude spectrum of 70 hz signal")
plt.xlabel("frequency HZ")
plt.ylabel("x(k)")
plt.grid()

plt.tight_layout()
plt.show()
        
