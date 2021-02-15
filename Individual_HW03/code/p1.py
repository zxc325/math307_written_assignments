# Ref. https://stackoverflow.com/questions/40852861/hide-radial-tick-labels-matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

r = 2

def calculate_theta(j):
    theta = np.pi/8 + (j * np.pi)/2
    return theta
rads = [calculate_theta(j) for j in [0, 1, 2, 3]]

for rad in rads:
    ax.plot(rad, r, 'r.')

ax.set_yticklabels([]) # hide radial labels

plt.show()