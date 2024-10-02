import numpy as np

class IzhikevichNeuron:
    def __init__(self, a=0.02, b=0.2, c=-65, d=8):
        """
        Initialize the neuron with the given parameters for the Izhikevich model.
        Parameters:
        - a: time scale of recovery variable
        - b: sensitivity of recovery variable
        - c: reset value of membrane potential
        - d: reset increment for recovery variable
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.v = -65  # Membrane potential
        self.u = b * self.v  # Recovery variable
        self.spike_ts = []  # To store time steps where spikes occur

    def step(self, I, dt=1):
        """
        Perform a single time step update of the neuron state.
        Parameters:
        - I: External input current
        - dt: Time step duration (default: 1 ms)
        """
        if self.v >= 30:  # Spike threshold
            self.spike_ts.append(1)  # Mark as spike
            self.v = self.c  # Reset membrane potential
            self.u += self.d  # Reset recovery variable
        else:
            self.spike_ts.append(0)  # No spike

        # Update equations
        dv = 0.04 * self.v ** 2 + 5 * self.v + 140 - self.u + I
        self.v += dv * dt
        du = self.a * (self.b * self.v - self.u)
        self.u += du * dt

    def reset(self):
        """ Reset the neuron to the initial state """
        self.v = -65
        self.u = self.b * self.v
        self.spike_ts = []

    def get_spike_rate(self, discard, total_time, dt):
        """ 
        Calculate the spike rate, ignoring the first 'discard' steps.
        - discard: the time in ms to ignore
        - total_time: the total time of the simulation
        """
        valid_spikes = self.spike_ts[int(discard / dt):int(total_time / dt)]
        return np.mean(valid_spikes) * 1000 / (total_time - discard)
