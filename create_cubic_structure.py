import numpy as np
import configparser

# Read configuration from the 'config.ini' file
config = configparser.ConfigParser()
config.read('config.ini')

# Extract configuration parameters
cubic_structure = config.get('cubic_structure', 'type').lower()
Nx_string = config.get('repetitions', 'Nx')
Ny_string = config.get('repetitions', 'Ny')
Nz_string = config.get('repetitions', 'Nz')
Nx = int(Nx_string)
Ny = int(Ny_string)
Nz = int(Nz_string)
a_string = config.get('lattice_parameter', 'a')
a = float(a_string)
element_symbol = config.get('element', 'symbol')

# Check for a specific error condition and raise an exception if met
if Nx == 0 or Ny == 0 or Nz == 0:
    raise ValueError("Error: At least one of Nx, Ny, or Nz is equal to zero.")

# Create a 3D grid of atoms for the specified cubic structure
def generate_cubic_structure(
                        structure : str,
                        Nx : int,
                        Ny : int,
                        Nz : int
):
    """
    Notes
    -----
    This function calls the right function to generate and return the cubic structure specified in config

    Parameters
    ----------
    structure (str) : type of cubic structure (sc, bcc or fcc)
    Nx (int) : number of repetitions of the structure to display the x axis
    Ny (int) : number of repetitions of the structure to display the y axis
    Nz (int) : number of repetitions of the structure to display the z axis

    """

    if structure == "sc":
        return generate_simple_cubic(Nx, Ny, Nz)
    elif structure == "bcc":
        return generate_body_centered_cubic(Nx, Ny, Nz)
    elif structure == "fcc":
        return generate_face_centered_cubic(Nx, Ny, Nz)
    else:
        raise ValueError("Invalid cubic_structure specified in config.ini")



# Create a 3D grid of atoms for the simple cubic structure
def generate_simple_cubic(
                        Nx : int,
                        Ny : int,
                        Nz : int
) -> np.ndarray:
    """
    Notes
    -----
    This function calculates the atomic positions of a simple cubic structure

    Parameters
    ----------
    Nx (int) : number of repetitions of the structure to display the x axis
    Ny (int) : number of repetitions of the structure to display the y axis
    Nz (int) : number of repetitions of the structure to display the z axis

    Returns
    -------
    atomic_positions (np.ndarray) : 3-dim array cointaining the atomic positions
    """

    atomic_positions = []
    for i in range(Nx + 1):
        for j in range(Ny + 1):
            for k in range(Nz + 1):
                atomic_positions.append([i * a, j * a, k * a])
    atomic_positions = np.array(atomic_positions)
    return atomic_positions


# Create a 3D grid of atoms for the body-centered cubic structure
def generate_body_centered_cubic(
                                Nx : int,
                                Ny : int,
                                Nz : int
) -> np.ndarray:
    """
    Notes
    -----
    This function calculates the atomic positions of a body centered cubic structure

    Parameters
    ----------
    Nx (int) : number of repetitions of the structure to display the x axis
    Ny (int) : number of repetitions of the structure to display the y axis
    Nz (int) : number of repetitions of the structure to display the z axis
    Returns
    -------
    atomic_positions (np.array) : 3-dim array cointaining the atomic positions
    """
    
    atomic_positions = []
    for i in range(Nx + 1):
        for j in range(Ny + 1):
            for k in range(Nz + 1):
                atomic_positions.append([i * a, j * a, k * a])
                
  
    for i in range(Nx ):
        for j in range(Ny):
            for k in range(Nz):
                # evaluation of the position of the central atom
                atomic_positions.append( [(i+0.5) * a, (j+0.5) * a, (k+0.5) * a])
    
    return atomic_positions

# Create a 3D grid of atoms for the face-centered cubic structure
def generate_face_centered_cubic(
                                Nx : int,
                                Ny : int,
                                Nz : int
) -> np.ndarray:
    """
    Notes
    -----
    This function calculates the atomic positions of a face centered cubic structure

    Parameters
    ----------
    Nx (int) : number of repetitions of the structure to display the x axis
    Ny (int) : number of repetitions of the structure to display the y axis
    Nz (int) : number of repetitions of the structure to display the z axis

    Returns
    -------
    atomic_positions (np.ndarray) : 3-dim array cointaining the atomic positions
    """
    atomic_positions = []

    # Evaluation of the atoms at the verteces
    for i in range(Nx + 1):
        for j in range(Ny + 1):                
            for k in range(Nz + 1):
                atomic_positions.append([i * a, j * a, k * a])

    # Evaluation of the face centeres atoms along the x direction
    for i in range(Nx + 1):
        for j in range(Ny):
            for k in range(Nz):
                atomic_positions.append([i * a, j * a + a/2, k * a + a/2])

    # Evaluation of the face centeres atoms along the y direction
    for i in range(Nx):
        for j in range(Ny + 1):
            for k in range(Nz):
                atomic_positions.append([i * a + a/2, j * a, k * a + a/2])

    # Evaluation of the face centeres atoms along the z direction
    for i in range(Nx):
        for j in range(Ny):
            for k in range(Nz + 1):
                atomic_positions.append([i * a + a/2, j * a + a/2, k * a])
    atomic_positions = np.array(atomic_positions)
    return atomic_positions

def save_atomic_coordinates(cubic_positions):    
    # Generate the filename based on the configuration parameters
    filename = f'{element_symbol}_{cubic_structure}_a{a}__Nx{Nx}_Ny{Ny}_Nz{Nz}.txt'

    # Save the atomic positions to the generated filename
    np.savetxt(filename, cubic_positions)

cubic_positions = generate_cubic_structure(cubic_structure, Nx, Ny, Nz)
save_atomic_coordinates(cubic_positions)