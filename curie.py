import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# Read data from a document file (e.g., 'data.txt')
data = np.loadtxt('NBCO/down.txt')

# Separate columns into T and R
T = data[:, 0]
R = 0.0160691 * data[:, 1]

# Define the step size (n-step differentiation)
n = 50  # You can adjust this to the desired step size


# Compute the derivative using a larger step size
dR_dT_long_step = (R[n:] - R[:-n]) / (T[n:] - T[:-n])

# Create a new T array that matches the length of dR/dT with the longer step
T_long_step = (T[:-n] + T[n:]) / 2

# Remove infinities and NaN values from the data
valid_indices = np.isfinite(dR_dT_long_step)
T_clean = T_long_step[valid_indices]
dR_dT_clean = dR_dT_long_step[valid_indices] * 25

# Create a figure with two subplots (Before filtering T)
plt.figure(figsize=(10, 8))

plt.plot(T, R, marker='o', linestyle='-', color='g')
plt.xlabel('T(K)')
plt.ylabel('Resistivity(Ohm•m)')
#plt.title('Plot of T vs R (Before filtering)')
plt.grid(True)


plt.plot(T_clean, dR_dT_clean, linestyle='-')
# plt.grid(True)
plt.show()