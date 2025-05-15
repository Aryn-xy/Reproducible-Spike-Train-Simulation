import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
duration = 1 
firing_rate = 10 
n_spikes = np.random.poisson(firing_rate * duration)
#Spike times
spike_times = np.sort(np.random.rand(n_spikes) * duration)
print("Spike times:", spike_times)

# Ploting raster plot
plt.eventplot(spike_times, colors='black')
plt.xlabel("Time (s)")
plt.title("Simulated Spike Train")
plt.show()

#Calculating ISI
isi = np.diff(spike_times)
plt.hist(isi, bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Inter-Spike Interval (s)")
plt.title("ISI Histogram")
plt.show()

# Calculate firing rate
firing_rate = len(spike_times) / duration
print(f"Firing Rate: {firing_rate:.2f} Hz")
