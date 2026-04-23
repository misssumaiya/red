import numpy as np
import matplotlib.pyplot as plt

fs = 8000
fc = 1000
N=21

#normalize cutoff frequency
wc=2*np.pi*fc/fs
#ideal impulse response
M=(N-1)//2
hd=np.zeros(N)

for n in range(N):
    if n==M:
        hd[n]=wc/np.pi
    else:
        hd[n]=np.sin(wc*(n-M))/(np.pi*(n-M))
#hamming window
w=np.zeros(N)
for n in range(N):
    w[n]=0.54-0.46*np.cos(2*np.pi*n/(N-1))
#final fir coefficients   
h=hd*w 
#frequency response(manual DFT)
num_points=512
H=np.zeros(num_points,dtype=complex)

for k in range(num_points):
    for n in range(N):
        H[k]+=h[n]*np.exp(-1j*2*np.pi*k*n/num_points)
#magnitude and phase
magnitude = np.abs(H)
phase=np.angle(H)

#frequency axis
freq = np.linspace(0,fs,num_points)

# plot impulse response
plt.figure()
plt.plot(range(N),h)
plt.title("Impulse response")
plt.xlabel("n")
plt.ylabel("h[n]")
plt.grid

#plot magnitude response
plt.figure()
plt.plot(freq,magnitude)
plt.title("Magnitude response")
plt.xlabel("frequency (Hz)")
plt.ylabel("H(f)")
plt.grid()

#plot phase reponse
plt.figure()
plt.plot(freq,phase)
plt.title("Phase response")
plt.xlabel("frequency (Hz)")
plt.ylabel("Phase(radians)")
plt.grid()

plt.show()                      