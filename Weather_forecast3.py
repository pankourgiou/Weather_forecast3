import numpy as np
import matplotlib.pyplot as plt

# Generate some sample temperature data
time = np.array([0, 1, 2, 3, 4, 5])  # Time in hours
temperature = np.array([20, 21, 22, 23, 24, 25])  # Temperature in degrees Celsius

# Plot the temperature data
plt.plot(time, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.show()

# Use numerical differentiation to estimate the rate of change in temperature
dt = time[1] - time[0]  # Time step
d_temperature = np.diff(temperature) / dt  # Numerical differentiation

# Plot the rate of change in temperature
plt.plot(time[1:], d_temperature, marker='o', linestyle='-', color='r')
plt.xlabel('Time (hours)')
plt.ylabel('Rate of Change in Temperature (°C/h)')
plt.title('Rate of Change in Temperature Over Time')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate some sample temperature data
time = np.array([0, 1, 2, 3, 4, 5])  # Time in hours
temperature = np.array([18, 20, 25, 24, 16, 17])  # Temperature in degrees Celsius

# Plot the temperature data
plt.plot(time, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.show()

# Use numerical differentiation to estimate the rate of change in temperature
dt = time[1] - time[0]  # Time step
d_temperature = np.diff(temperature) / dt  # Numerical differentiation

# Plot the rate of change in temperature
plt.plot(time[1:], d_temperature, marker='o', linestyle='-', color='r')
plt.xlabel('Time (hours)')
plt.ylabel('Rate of Change in Temperature (°C/h)')
plt.title('Rate of Change in Temperature Over Time')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate some sample temperature data
time = np.array([0, 1, 2, 3, 4, 5])  # Time in hours
temperature = np.array([16, 17, 18, 19, 20, 21])  # Temperature in degrees Celsius

# Plot the temperature data
plt.plot(time, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.show()

# Use numerical differentiation to estimate the rate of change in temperature
dt = time[1] - time[0]  # Time step
d_temperature = np.diff(temperature) / dt  # Numerical differentiation

# Plot the rate of change in temperature
plt.plot(time[1:], d_temperature, marker='o', linestyle='-', color='r')
plt.xlabel('Time (hours)')
plt.ylabel('Rate of Change in Temperature (°C/h)')
plt.title('Rate of Change in Temperature Over Time')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate some sample temperature data
time = np.array([0, 1, 2, 3, 4, 5])  # Time in hours
temperature = np.array([22,17, 19, 22, 22, 19])  # Temperature in degrees Celsius

# Plot the temperature data
plt.plot(time, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.show()

# Use numerical differentiation to estimate the rate of change in temperature
dt = time[1] - time[0]  # Time step
d_temperature = np.diff(temperature) / dt  # Numerical differentiation

# Plot the rate of change in temperature
plt.plot(time[1:], d_temperature, marker='o', linestyle='-', color='r')
plt.xlabel('Time (hours)')
plt.ylabel('Rate of Change in Temperature (°C/h)')
plt.title('Rate of Change in Temperature Over Time')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Generate some sample temperature data
time = np.array([0, 1, 2, 3, 4, 5])  # Time in hours
temperature = np.array([15, 16, 17, 18, 19, 22])  # Temperature in degrees Celsius

# Plot the temperature data
plt.plot(time, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.grid(True)
plt.show()

# Use numerical differentiation to estimate the rate of change in temperature
dt = time[1] - time[0]  # Time step
d_temperature = np.diff(temperature) / dt  # Numerical differentiation

# Plot the rate of change in temperature
plt.plot(time[1:], d_temperature, marker='o', linestyle='-', color='r')
plt.xlabel('Time (hours)')
plt.ylabel('Rate of Change in Temperature (°C/h)')
plt.title('Rate of Change in Temperature Over Time')
plt.grid(True)
plt.show()
