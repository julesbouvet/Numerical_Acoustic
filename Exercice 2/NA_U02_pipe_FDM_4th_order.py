"""
Calculation of modes of a closed one-dimensional pipe (4th order)
"""
from pylab import *

l = 1. #tube length
c0 = 343. #speed of sound
N = 10 #number of nodal points

# distance between adjacent nodal points
h = l/(N-1)

x=linspace(0,l,N)
# constructing the system matrix

A= diag(-5/2*ones(N))+diag(4/3*ones(N-1),1)+diag(4/3*ones(N-1),-1)+diag(-1/12*ones(N-2),-2)+diag(-1/12*ones(N-2),2)

# the first row
A[0,0] = -2.0 
A[0,1]=2
A[0,2]=0
  
# the second row
A[1,1]=-31/12  
 
# the last row
A[N-1,N-1]=-2
A[N-1,N-2]=2
A[N-1,N-3]=0
 
# the second last row
A[N-2,N-2]=-31/12
 
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