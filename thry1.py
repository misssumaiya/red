import numpy as np
import matplotlib.pyplot as plt

fs=1500
f_base=250

#Continuous time signal
t=np.linspace(0,0.01,100)
x_t=np.cos(2*np.pi*f_base*t)

#discrete time signal
n=np.arange(0,30)
x_n=np.cos(2*np.pi*f_base/fs*n)

plt.figure(figsize=(10,5))

plt.subplot(2,1,1)
plt.plot(t,x_t)
plt.title("Continuous signal")
plt.grid()

plt.subplot(2,1,2)
plt.stem(n,x_n)
plt.title("discrete time signal")
plt.grid()

plt.tight_layout()
plt.show()
#continuous to discrete time signal
#Alias frequency calculation

k_range=range(-5,6)
f_values=[]
for k in k_range:
    f1=f_base+k*fs
    f_values.append(f1)
print("All possible f0")
for i in f_values:
    print(i)
    
index=np.arange(len(f_values))
plt.plot(3,1,3)
plt.stem(index,f_values)
plt.title("All possible value f0 values(Aliasing)")
plt.xlabel("index (k)")
plt.ylabel("Frequncy Hz")
plt.show()
    