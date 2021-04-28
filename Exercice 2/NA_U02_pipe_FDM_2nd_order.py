"""
Calculation of modes of a closed one-dimensional pipe (2nd order)
"""
from pylab import *

l = 1. #tube length
c0 = 343. #speed of sound
N = 10 #number of nodal points

# distance between adjacent nodal points
h = l/(N-1)

x=linspace(0,l,N)
# constructing the system matrix
# main diagonal
A = -2.0*diag(ones(N,dtype=float))
# adjacent diagonals
A[arange(N-1),arange(1,N)] = 1.0
A[arange(1,N),arange(N-1)] = 1.0
# the first and the last row
A[0,1] = 2.0
A[N-1,N-2] = 2.0
 
 



# this is left blank for easier visual comparison with the code for the 4th order





# eigenvalues and eigenvectors
eigenval,eigenvec = eig(1/(h*h) * A)
# eigenfrequencies
f_m = c0/2/pi * sqrt(abs(eigenval))

# sorting according to the increasing frequency
ind = argsort(f_m) #argsort gives the ordered indices
eigenvec = eigenvec[:,ind]
eigenval = eigenval[ind]
f_sort = f_m[ind]

print(f_sort[1:6])
# displaying the modes - linear
plt.figure(1)
for i in range(1,6):
    plot(x,eigenvec[:,i], label="mode {}".format(i))
xlim([0,1])
grid()
legend(loc='lower right', ncol=2)
show()

# displaying the modes - logarithmic
plt.figure(2)
for i in range(1,6):
    plot(x,20*log10(abs(eigenvec[:,i])), label="mode {}".format(i))
xlim([0,1])
grid()
legend(loc='lower right', ncol=2)
show()