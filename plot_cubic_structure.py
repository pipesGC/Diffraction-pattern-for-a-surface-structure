import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import configparser

# Read configuration from the 'config.ini' file
config = configparser.ConfigParser()
config.read('config.ini')

# Extract element symbol from configuration
element_symbol = config.get('element', 'symbol')

# Extract lattice parameter a from configuration
a_string = config.get('lattice_parameter', 'a')
a = np.float(a_string)

# Extract cubic structure
cubic_structure = config.get('cubic_structure', 'type').lower()

# Read atomic positions from the file
cubic_positions = np.loadtxt('cubic_structure_positions.txt')
cubic_positions /= a # renormalize the cubic structure to the lattice parameter 

# Plot a cubic structure
def plot_cubic_structure(atomic_positions, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(atomic_positions[:, 0], atomic_positions[:, 1], atomic_positions[:, 2], c='r', marker='o', s=100)
    ax.set_xlabel('a (au)')
    ax.set_ylabel('b (au)')
    ax.set_zlabel('c (au)')
    ax.set_xlim(0, np.max(atomic_positions[:, 0]))
    ax.set_ylim(0, np.max(atomic_positions[:, 1]))
    ax.set_zlim(0, np.max(atomic_positions[:, 2]))
    plt.title(title)
    plt.show()

# Add the element symbol to the plot title
plot_title = f'{element_symbol} {cubic_structure} lattice with a = {a} Å'
plot_cubic_structure(cubic_positions, plot_title)
