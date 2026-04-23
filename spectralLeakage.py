import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N=len(x)
    X=np.zeros(N,dtype=complex)
    
    for k in range(N):
        for n in range(N):
            X[k]+=x[n]*np.exp(-1j*2*np.pi*k*n/N)
    return X   
def hamming_window(N):
    w=np.zeros(N)
    for n in range(N):
        w[n]=0.54-0.46*np.cos((2*np.pi*n)/(N-1))
    return w
fs=100
f=10
t1=np.arange(0,1,1/fs)
x1=np.sin(2*np.pi*f*t1)

X1=dft(x1)
N1=len(X1)
k1=np.arange(N1)
freq1=k1*fs/N1

t2=np.arange(0,0.95,1/fs)
x2=np.sin(2*np.pi*f*t2)

X2=dft(x2)
N2=len(X2)
k2=np.arange(N2)
freq2=k2*fs/N2

w=hamming_window(N2)
x2_windowed=x2*w
X2_win=dft(x2_windowed)

mag1=np.abs(X1)
mag2=np.abs(X2)
mag3_win=np.abs(X2_win) 

plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.stem(freq1,mag1)
plt.title("DFT 1s Signal spectrum(Clean signal)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()

plt.subplot(3,1,2)
plt.stem(freq2,mag2)
plt.title("DFT 0.95s signal(spectral leakage)") 
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()

plt.subplot(3,1,3)
plt.stem(freq2,mag3_win)
plt.title("DFT after hamming window(Reduced leakage)")
plt.xlabel("frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid()

plt.tight_layout()
plt.show()      
