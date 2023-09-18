import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import configparser
import os

# Read configuration from the 'config.ini' file
config = configparser.ConfigParser()
config.read('config.ini')

# Extract element symbol from configuration
element_symbol = config.get('element', 'symbol')

# Extract lattice parameter a from configuration
a_string = config.get('lattice_parameter', 'a')
a = float(a_string)

# Extract cubic structure
cubic_structure = config.get('cubic_structure', 'type').lower()

# Extract the number of repetitions along each axis
Nx_string = config.get('repetitions', 'Nx')
Ny_string = config.get('repetitions', 'Ny')
Nz_string = config.get('repetitions', 'Nz')
Nx = int(Nx_string)
Ny = int(Ny_string)
Nz = int(Nz_string)

# Check if the 'cubic_structure_positions.txt' file exists
if not os.path.isfile('cubic_structure_positions.txt'):
    raise FileNotFoundError("Error: 'cubic_structure_positions.txt' file not found. Run create_cubic_structure.py first.")

# Read atomic positions from the file
cubic_positions = np.loadtxt('cubic_structure_positions.txt')
cubic_positions /= a  # renormalize the cubic structure to the lattice parameter

# Initialize variables to store selected atom indices and their colors
atom_colors = ['r'] * len(cubic_positions)  # Initialize all atoms as red

def plot_cubic_structure():
    """
    Create a 3D plot of the cubic structure.
    """
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot of atom positions with colors
    sc = ax.scatter(cubic_positions[:, 0], cubic_positions[:, 1], cubic_positions[:, 2], c=atom_colors, marker='o', s=100)

    # Set axis labels
    ax.set_xlabel('a (au)')
    ax.set_ylabel('b (au)')
    ax.set_zlabel('c (au)')

    # Set plot limits
    ax.set_xlim(0, np.max(cubic_positions[:, 0]))
    ax.set_ylim(0, np.max(cubic_positions[:, 1]))
    ax.set_zlim(0, np.max(cubic_positions[:, 2]))

    # Title with element symbol
    plot_title = f'{element_symbol} {cubic_structure} lattice with a = {a} Å'
    plt.title(plot_title)

    # Display the plot
    plt.show()

def save_cubic_structure_plot(filename: str):
    """
    Save the cubic structure plot to a file.

    Parameters:
    ----------
    filename (str): The name of the file to save the plot as.
    """
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Scatter plot of atom positions with colors
    sc = ax.scatter(cubic_positions[:, 0], cubic_positions[:, 1], cubic_positions[:, 2], c=atom_colors, marker='o', s=100)

    # Set axis labels
    ax.set_xlabel('a (au)')
    ax.set_ylabel('b (au)')
    ax.set_zlabel('c (au)')

    # Set plot limits
    ax.set_xlim(0, np.max(cubic_positions[:, 0]))
    ax.set_ylim(0, np.max(cubic_positions[:, 1]))
    ax.set_zlim(0, np.max(cubic_positions[:, 2]))

    # Title with element symbol
    plot_title = f'{element_symbol} {cubic_structure} lattice with a = {a} Å'
    plt.title(plot_title)

    # Save the plot as an image file
    plt.savefig(filename)

# Call the functions
save_cubic_structure_plot('cubic_structure_plot.png')

# Call the functions
plot_cubic_structure()
filename = f'{element_symbol}_{cubic_structure}_a{a}__Nx{Nx}_Ny{Ny}_Nz{Nz}'
save_cubic_structure_plot(filename)
