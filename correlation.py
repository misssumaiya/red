import numpy as np
import matplotlib.pyplot as plt

def correlation(x,y):
    L=len(x)
    l=len(y)
    N=L+l-1
    
    X=np.zeros(N)
    
    for k in range(-l+1,L):
        for n in range(L):
            if 0<=n-k<l:
                X[k+(l-1)]+=x[n]*y[n-k]
    return X  
x=np.array([1,2,3])
y=np.array([1,2,1])

r=correlation(x,y)

plt.figure()
plt.stem(r)
plt.title("correlation")
plt.show()          