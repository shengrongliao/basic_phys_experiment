import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read data from a document file (e.g., 'data.txt')
data = np.loadtxt('NBCO/down.txt')

# Separate columns into T and R

T = data[:, 0]
rho = data[:, 1] * 0.0057877
T_left = T[450:]
rho_left = rho[450:]

slope, intercept, r_value, p_value, std_err = linregress(T_left, rho_left)
r_squared = r_value**2 

T_fit = np.linspace(12, 43)
rho_fit = slope * T_fit + intercept
print(intercept / slope)

# plt.figure(figsize=(8, 6))
plt.plot(T, rho, 'o', color='green', markersize=3)
plt.plot(T_fit, rho_fit, 'r--', label=f'y = {slope:.6f} * x {intercept:.5f}\n$R^2$ = {r_squared:.3f}')


plt.xlabel('T(K)')
plt.ylabel('Resistivity(Ohm•m)')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.grid(True)
plt.legend()
plt.show()