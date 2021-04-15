#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmath

rho0 = 1.2
c0 = 343
global k
k = 0.9 #wavenumber

def p_hat(x_coord):
    return 0.5*cmath.exp(-1j*k*x_coord)


x = 1

#exact solution
v_hat_exact = p_hat(x)/(rho0*c0)
print("v_hat_exact =", v_hat_exact)


omega = k*c0 #angular frequency

dx = 0.1 #=0.5
#forward difference
v_hat_forward = -1/(1j*omega*rho0) * (p_hat(x+dx)-p_hat(x))/dx
print("v_hat_forwd =", v_hat_forward)
#backward difference
v_hat_backward = -1/(1j*omega*rho0) * (p_hat(x)-p_hat(x-dx))/dx
print("v_hat_backd =", v_hat_backward)
#central difference
v_hat_central = -1/(1j*omega*rho0) * (p_hat(x+dx)-p_hat(x-dx))/(2*dx)
print("v_hat_centd =", v_hat_central)