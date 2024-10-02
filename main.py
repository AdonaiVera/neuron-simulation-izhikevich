import numpy as np
import matplotlib.pyplot as plt
from methods.izhikevich import IzhikevichNeuron
from methods.utils import plot_membrane_potentials, plot_spike_rate_vs_input

# Step size (τ = 0.25 ms)
dt = 0.25
steps_per_time_unit = int(1 / dt)  # 4 micro-steps per actual step

# Total time (1,001 steps at τ = 0.25 results in 4,001 data points)
T = 1000
n_steps = int(T * steps_per_time_unit + 1)  # 4,001 data points

# External input current (I values)
I_values = [1, 10, 20, 30, 40]

# Initialize neuron model with RS parameters
neuron = IzhikevichNeuron()

# Function to run the simulation for given I and return the membrane potential history
def run_simulation(I, T, n_steps, dt):
    neuron.reset()  # Reset neuron to its initial state
    v_history = []
    
    for t in range(n_steps):
        neuron.step(I, dt)
        v_history.append(neuron.v)
    
    return v_history

# Run simulations for I = 1, 10, 20, 30, 40 and store membrane potential histories
membrane_potentials = []
for I in I_values:
    membrane_potentials.append(run_simulation(I, T, n_steps, dt))

# Plot the 5 membrane potential time-series in a single figure with stacked graphs
plot_membrane_potentials(membrane_potentials, I_values, dt, T)

# Spike rate (R) vs Input current (I) plot
I_range = np.arange(0, 41, 1)
spike_rates = []

# Simulate for each I from 0 to 40 and calculate the spike rate
for I in I_range:
    v_history = run_simulation(I, T, n_steps, dt)
    spike_rate = sum(np.array(neuron.spike_ts)[int(200 * steps_per_time_unit):]) / 800  # Count spikes, ignore first 200 steps
    spike_rates.append(spike_rate)

# Plot R vs I
plot_spike_rate_vs_input(I_range, spike_rates)
