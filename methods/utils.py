import matplotlib.pyplot as plt
import numpy as np

def plot_membrane_potentials(membrane_potentials, I_values, dt, T):
    """ Plot the membrane potential for I = 1, 10, 20, 30, 40 in stacked graphs. """
    
    time = np.arange(0, T + dt, dt)  # Time array (0 to 1,000 ms with micro-steps)
    
    plt.figure(figsize=(10, 12))
    for i, v in enumerate(membrane_potentials):
        plt.subplot(5, 1, i + 1)
        plt.plot(time, v, label=f'I = {I_values[i]}')
        plt.title(f'Membrane Potential for I = {I_values[i]}')
        plt.ylabel('Membrane Potential (mV)')
        plt.xlabel('Time (ms)')
        plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def plot_spike_rate_vs_input(I_range, spike_rates):
    """ Plot spike rate (R) vs input current (I). """
    
    plt.figure(figsize=(8, 5))
    plt.plot(I_range, spike_rates, '-o', label='Spike Rate (R)')
    plt.xlabel('Input Current (I)')
    plt.ylabel('Spike Rate (Spikes/ms)')
    plt.title('Spike Rate vs Input Current')
    plt.grid(True)
    plt.show()
