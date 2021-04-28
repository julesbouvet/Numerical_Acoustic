"""
Calculation of modes of a closed one-dimensional pipe (2nd order)
"""
import numpy as np
import matplotlib.pyplot as plt

l = 1. #tube length
c0 = 343. #speed of sound
N = 10 #number of nodal points

# distance between adjacent nodal points
h = l/(N-1)

x=np.linspace(0,l,N)
# constructing the system matrix
# main diagonal
A = -2.0*np.diag(np.ones(N, dtype=float))
# adjacent diagonals
A[np.arange(N-1),np.arange(1,N)] = 1.0
A[np.arange(1,N),np.arange(N-1)] = 1.0
# the first and the last row
A[0,1] = 2.0
A[N-1,N-2] = 2.0
 
 



# this is left blank for easier visual comparison with the code for the 4th order





# eigenvalues and eigenvectors
eigenval,eigenvec = np.linalg.eig(1/(h*h) * A)
# eigenfrequencies
f_m = c0/2/np.pi * np.sqrt(abs(eigenval))

# sorting according to the increasing frequency
ind = np.argsort(f_m) #argsort gives the ordered indices
eigenvec = eigenvec[:,ind]
eigenval = eigenval[ind]
f_sort = f_m[ind]

print(f_sort[1:6])
# displaying the modes - linear
plt.figure(1)
for i in range(1,6):
    plt.plot(x,eigenvec[:,i], label="mode {}".format(i))
plt.xlim([0,1])
plt.grid()
plt.legend(loc='lower right', ncol=2)
plt.show()

# displaying the modes - logarithmic
plt.figure(2)
for i in range(1,6):
    plt.plot(x,20*np.log10(abs(eigenvec[:,i])), label="mode {}".format(i))
plt.xlim([0,1])
plt.grid()
plt.legend(loc='lower right', ncol=2)
plt.show()