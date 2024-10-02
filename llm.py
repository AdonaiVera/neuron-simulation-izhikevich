import numpy as np
import matplotlib.pyplot as plt

# Parameters for the Izhikevich neuron model
a = 0.02
b = 0.2
c = -65
d = 8

# Time parameters
dt = 1.0  # Time step in milliseconds
T = 1000  # Total simulation time in milliseconds

# Input current range
I_range = np.arange(0, 41, 1)

# Function to simulate the Izhikevich neuron
def izhikevich_neuron(I, T, dt):
    v = -65  # Initial membrane potential
    u = b * v  # Initial recovery variable
    spikes = []

    for t in range(int(T / dt)):
        dv = (0.04 * v**2 + 5 * v + 140 - u + I) * dt
        du = (a * (b * v - u)) * dt
        v += dv
        u += du

        if v >= 30:  # Spike threshold
            spikes.append(t)
            v = c
            u += d

    return spikes

# Calculate spiking rates for different input currents
spiking_rates = []

for I in I_range:
    spikes = izhikevich_neuron(I, T, dt)
    spike_count = len([s for s in spikes if s >= 200])  # Count spikes in the last 800 time-steps
    spiking_rate = spike_count / (T - 200) * 1000  # Convert to Hz
    spiking_rates.append(spiking_rate)

# Plot spiking rate versus input current
plt.plot(I_range, spiking_rates, marker='o')
plt.xlabel('Input Current (I)')
plt.ylabel('Spiking Rate (Hz)')
plt.title('Spiking Rate vs Input Current for Izhikevich Neuron')
plt.grid(True)
plt.show()
