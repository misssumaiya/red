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
h=hd*w

num_points=512
X=np.zeros(num_points)
for k in range(num_points):
    for n in range(N):
        X[k]+=h[n]*np.exp(-2j*np.pi*k*n/num_points)
magnitude=np.abs(X)
phase=np.angle(X)

freq=np.linspace(0,fs,num_points)

plt.figure(figsize=(10,6))

plt.subplot(3,1,1)
plt.plot(range(N),h)
plt.title("Impulse reponse")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid()

plt.subplot(3,1,2)
plt.plot(freq,magnitude)
plt.title("Magnitude Response")
plt.xlabel("frequency Hz")
plt.ylabel("H(f)") 
plt.grid()

plt.subplot(3,1,3)
plt.plot(freq,phase)
plt.title("phase response")
plt.xlabel("frequency")
plt.ylabel("phase")
plt.grid()

plt.tight_layout()
plt.show()                      