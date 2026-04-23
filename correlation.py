import numpy as np
import matplotlib.pyplot as plt

def correlation(x,y):
    N=len(x)
    result=[]
    for k in range(-N+1,N):
        sum=0
        for n in range(N):
            if 0<=n-k<N:
                sum+=x[n]*y[n-k]
        result.append(sum)
    return np.array(result)
fs=1000
t=np.arange(0,1,1/fs)

a=np.sin(2*np.pi*10*t)
b=np.sign(np.sin(2*np.pi*10*t))
c=np.sin(2*np.pi*20*t)

auto_a=correlation(a,a)
cross_ab=correlation(a,b)
cross_ac=correlation(a,c)  

lags=np.arange(-len(a)+1,len(a))

plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.stem(lags,auto_a)
plt.title("Auto_correlation of 10Hz sine(a)")
plt.xlabel("lag")
plt.ylabel("correlation")
plt.grid()

plt.subplot(3,1,2)
plt.stem(lags,cross_ab)
plt.title("Crross correlation of a and b")
plt.xlabel("lags")
plt.ylabel("Correlation")
plt.grid()

plt.subplot(3,1,3)
plt.stem(lags,cross_ac)
plt.title("Cross correlation of a and c")
plt.xlabel("lags")
plt.ylabel("Correlation")
plt.grid()

plt.tight_layout()
plt.show()

             