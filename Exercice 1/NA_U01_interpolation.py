# -*- coding: utf-8 -*-
"""
Comparison of linear and cubic spline interpolation methods
@author: katja
"""


import numpy as np
import matplotlib.pyplot as plt


# Construction of the discretized data
f_smp = 50  # sampling frequency
t_smp = np.linspace(0., 1., f_smp+1)  # time

f_sin = 10  # frequency of the disretized sine signal
omega_sin = 2*np.pi*f_sin  # angular frequency
y_smp = np.sin(omega_sin*t_smp)  # samples of the discrete signal

plt.figure(num=1, figsize=(6.5, 4))
t_interp_100 = np.linspace(0., 1., 100*f_smp+1)  # increasing the sampling rate by the factor of 100 for the "exact" signal
plt.plot(t_smp, y_smp, 'o', label='samples')
plt.plot(t_interp_100, np.sin(t_interp_100*omega_sin), label='exact')
plt.xlim([0, 1])
plt.ylim([-1, 1])
plt.grid()

# FFT of the discrete signal

Y_smp=np.fft.rfft(y_smp)
plt.figure(num=2, figsize=(6.5, 4))
plt.plot(np.abs(Y_smp), 'o', label='samples')
plt.xlim([0, 50])
plt.ylim([0, 25])
plt.grid()


######################################################################
# linear interpolation

n = 2  # doubling the sampling frequency (adding interpolation points)
f_smp_interp_n = n*f_smp
# new time samples
t_interp = np.linspace(0., 1., f_smp_interp_n+1)
# initializing interpolated data
y_interp = np.zeros((f_smp_interp_n+1)) 
y_interp[::n] = y_smp  # Entering known data before the interpolation (the samples to be interpolated are left as zeros)

# linear interpolation of the remaining samples
for i in range(1, f_smp_interp_n, n):
    y_interp[i] = y_interp[i-1]+(y_interp[i+1]-y_interp[i-1])/(t_interp[i+1]-t_interp[i-1])*(t_interp[i]-t_interp[i-1])

# displaying the results
plt.figure(1)   
plt.plot(t_interp, y_interp, label="linear")
plt.legend(loc='lower right', ncol=2)

# FFT of the linear interpolation
Y_interp = np.fft.rfft(y_interp)
plt.figure(2)
plt.plot(np.abs(Y_interp)/2., label="linear")  # /2 for the normalization due to the doubled number of samples
plt.legend(loc='upper right', ncol=2)


#####################################################################
# spline interpolation

from scipy.interpolate import CubicSpline
cs = CubicSpline(t_smp, y_smp, bc_type='natural')  # cubic spline interpolation
# FFT of the spline-interpolated signal with doubled number of samples
Y_interp_cs = np.fft.rfft(cs(t_interp))

t_interp_100 = np.linspace(0., 1., 100*f_smp+1)  # increasing the sampling rate by the factor of 100

# displaying the interpolated signals
plt.figure(num=3, figsize=(6.5, 4))
plt.plot(t_smp, y_smp, 'o', label='samples')
plt.plot(t_interp_100, np.sin(t_interp_100*omega_sin), label='exact')
plt.plot(t_interp, y_interp, label="linear")
plt.plot(t_interp, cs(t_interp), label="spline (2x)")
plt.plot(t_interp_100,cs(t_interp_100), label="spline (100x)")
plt.legend(loc='lower right', ncol=2)
plt.xlim([0, 1])
plt.ylim([-1, 1])
plt.grid()

# displaying the FFT
plt.figure(num=4, figsize=(6.5, 4))
plt.plot(np.abs(Y_smp), 'o', label='samples')
plt.plot(np.abs(Y_interp)/2, label="linear")
plt.plot(np.abs(Y_interp_cs)/2, label="spline (2x)")
plt.plot(np.abs(np.fft.rfft(cs(t_interp_100)))/100, label="spline (100x)")
plt.legend(loc='upper right', ncol=2)
plt.xlim([0, 50])
plt.ylim([0, 25])
plt.grid()
plt.show()
