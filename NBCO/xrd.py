import pandas as pd
import matplotlib.pyplot as plt
# Load the text data into a pandas DataFrame, selecting only the required columns
data = pd.read_csv('NBCO_XRD.txt', sep=',', skipinitialspace=True, usecols=['Angle', 'PSD'])

# Display the first few rows to confirm loading is correct
print(data.head())

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data['Angle'], data['PSD'], marker='o', linestyle='-', color='b')
plt.xlabel('Angle')
plt.ylabel('PSD')
plt.title('Angle vs PSD')
plt.grid(True)
plt.show()