import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    L=len(x)
    X=np.zeros(L,dtype=complex)
    for k in range(L):
        for n in range(L):
            X[k]+=x[n]*np.exp(-2j*np.pi*n*k/L)
    return X
x1=np.array([1,2,1,0])
x2=np.array([0,1,1,2])
y=3*x1-2*x2
y1=dft(y)

X1=dft(x1)
x2=dft(x2)
Y=3*x1-2*x2
#check equality
print("are they equal?",np.allclose(y1,Y))
k=np.arange(len(Y))

plt.subplot(3,1,1)
plt.stem(np.abs(y1))
plt.title("DFT of y1")
plt.grid()

plt.subplot(3,1,2)
plt.stem(np.abs(Y))
plt.title("DFT of Y")
plt.grid()

plt.subplot(3,1,3)
plt.stem(np.abs(y1-Y))
plt.grid()

plt.tight_layout()
plt.show()
              