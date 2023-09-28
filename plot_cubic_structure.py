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

# Extract information on the surface to visualize
plane = config.get('surface', 'plane')

def get_cubic_coordinates():
    """
    Notes
    -----
    This function checks if the file containing the cubic atomic coordinates (3D) exists and it gets them
    
    Returns
    -------
    cubic_positions (np.ndarray) : 
    """
    # Check if the 'cubic_structure_positions.txt' file exists
    filename = f'{element_symbol}_{cubic_structure}_a{a}__Nx{Nx}_Ny{Ny}_Nz{Nz}.txt'
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Error: '{filename}' file not found. Run create_cubic_structure.py first.")

    # Read atomic positions from the file
    cubic_positions = np.loadtxt(filename)
    cubic_positions /= a  # renormalize the cubic structure to the lattice parameter

    return cubic_positions

def get_surface_coordinates():
    """
    Notes
    -----
    This function checks if the file containing the surface atomic coordinates (2D) exists and it gets them
    
    Returns
    -------
    surface_positions (np.ndarray) : 
    """
    # Check if the 'cubic_structure_positions.txt' file exists
    filename = f'{element_symbol}({plane})_{cubic_structure}_a{a}__Nx{Nx}_Ny{Ny}_Nz{Nz}.txt'
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"Error: '{filename}' file not found. Run create_cubic_structure.py first.")

    a_surface = a/2*np.sqrt(2)
    # Read atomic positions from the file
    surface_positions = np.loadtxt(filename)
    surface_positions /= a_surface  # renormalize the cubic structure to the lattice parameter

    return surface_positions


def plot_cubic_structure(filename : str =None):
    """
    Create a 3D plot of the cubic structure.

    Parameters
    ----------
    - filename (str, optional): The name of the file to save the plot as image
    """
    cubic_positions = get_cubic_coordinates()

    # Initialize variables to store selected atom indices and their colors
    atom_colors = ['r'] * len(cubic_positions)  # Initialize all atoms as red

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

    # Display or save the plot
    if filename:
        plt.savefig(filename)
    else:
        plt.show()

def plot_surface_structure(filename : str = None):
    """
    Create and optionally save a 2D plot of the (111) surface of the cubic structure.

    Parameters
    ----------
    - filename (str, optional): The name of the file to save the plot as image
    """

    surface_positions = get_surface_coordinates()

    # Extract the x and y coordinates of the atomic positions
    x = surface_positions[:, 0]
    y = surface_positions[:, 1]

    # Create a 2D plot for the (111) surface view
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Scatter plot of atom positions with colors
    sc = ax.scatter(x, y, c='r', marker='o', s=100)

    # Set axis labels
    ax.set_xlabel('a (au)')
    ax.set_ylabel('b (au)')

    # Title for the (111) surface
    plt.title('Surface (111) View')

    # Display or save the plot
    if filename:
        plt.savefig(filename)
    else:
        plt.show()

# def save_cubic_structure_plot(filename: str):
#     """
#     Save the cubic structure plot to a file.

#     Parameters:
#     ----------
#     filename (str): The name of the file to save the plot as.
#     """
#     # Create a 3D plot
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     # Scatter plot of atom positions with colors
#     sc = ax.scatter(cubic_positions[:, 0], cubic_positions[:, 1], cubic_positions[:, 2], c=atom_colors, marker='o', s=100)

#     # Set axis labels
#     ax.set_xlabel('a (au)')
#     ax.set_ylabel('b (au)')
#     ax.set_zlabel('c (au)')

#     # Set plot limits
#     ax.set_xlim(0, np.max(cubic_positions[:, 0]))
#     ax.set_ylim(0, np.max(cubic_positions[:, 1]))
#     ax.set_zlim(0, np.max(cubic_positions[:, 2]))

#     # Title with element symbol
#     plot_title = f'{element_symbol} {cubic_structure} lattice with a = {a} Å'
#     plt.title(plot_title)

#     # Save the plot as an image file
#     plt.savefig(filename)



# Call the functions
# plot_cubic_structure()
plot_surface_structure()

# plotname = f'{element_symbol}_{cubic_structure}_a{a}__Nx{Nx}_Ny{Ny}_Nz{Nz}.png'
# save_cubic_structure_plot(plotname)
