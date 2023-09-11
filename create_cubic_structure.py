import numpy as np
import configparser

# Read configuration from the 'config.ini' file
config = configparser.ConfigParser()
config.read('config.ini')

# Extract configuration parameters
cubic_structure = config.get('cubic_structure', 'type').lower()
n_string = config.get('repetitions', 'n')
n = int(n_string)
a_string = config.get('lattice_parameter', 'a')
a = float(a_string)

# Create a 3D grid of atoms for the specified cubic structure
def generate_cubic_structure(
                        structure : str,
                        n : int
):
    """
    Notes
    -----
    This function calls the right function to generate the cubic structure specified in config

    Parameters
    ----------
    structure (str) : type of cubic structure (sc, bcc or fcc)
    n (int) : number of repetitions of the structure to display along each axis

    """
    if structure == "sc":
        return generate_simple_cubic(n)
    elif structure == "bcc":
        return generate_body_centered_cubic(n)
    elif structure == "fcc":
        return generate_face_centered_cubic(n)
    else:
        raise ValueError("Invalid cubic_structure specified in config.ini")

# Create a 3D grid of atoms for the simple cubic structure
def generate_simple_cubic(
                        n : int
) -> np.ndarray:
    """
    Notes
    -----
    This function calculates the atomic positions of a simple cubic structure

    Parameters
    ----------
    n (int) : number of repetions of the cubic structure along each axis

    Returns
    -------
    atomic_positions (np.ndarray) : 3-dim array cointaining the atomic positions
    """
    n += 1  # needed to evaluate each vertex
    atomic_positions = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                atomic_positions.append([i * a, j * a, k * a])
    atomic_positions = np.array(atomic_positions)
    return atomic_positions

# Create a 3D grid of atoms for the body-centered cubic structure
def generate_body_centered_cubic(
                                n : int
) -> np.ndarray:
    """
    Notes
    -----
    This function calculates the atomic positions of a body centered cubic structure

    Parameters
    ----------
    n (int) : number of repetions of the cubic structure along each axis

    Returns
    -------
    atomic_positions (np.array) : 3-dim array cointaining the atomic positions
    """
    m = n + 1  # needed to evaluate each vertex
    atomic_positions = []
    for i in range(m):
        for j in range(m):
            for k in range(m):
                atomic_positions.append([i * a, j * a, k * a])
                
  
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # evaluation of the position of the central atom
                atomic_positions.append( [(i+1) * (a/2+i), (j+1) * (a/2+j), (k+1) * (a/2+k)])
    
    return atomic_positions

# Create a 3D grid of atoms for the face-centered cubic structure
def generate_face_centered_cubic(
                                n : int
) -> np.ndarray:
    """
    Notes
    -----
    This function calculates the atomic positions of a face centered cubic structure

    Parameters
    ----------
    n (int) : number of repetions of the cubic structure along each axis

    Returns
    -------
    atomic_positions (np.ndarray) : 3-dim array cointaining the atomic positions
    """
    atomic_positions = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                atomic_positions.append([i * a, j * a, k * a])
                atomic_positions.append([i * a + a/2, j * a + a/2, k * a])
                atomic_positions.append([i * a + a/2, j * a, k * a + a/2])
                atomic_positions.append([i * a, j * a + a/2, k * a + a/2])
    atomic_positions = np.array(atomic_positions)
    return atomic_positions

# Generate the specified cubic structure
cubic_positions = generate_cubic_structure(cubic_structure, n)

# Save the atomic positions to a file for further use (e.g., visualization)
np.savetxt('cubic_structure_positions.txt', cubic_positions)
