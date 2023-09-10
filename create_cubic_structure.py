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
def generate_cubic_structure(structure, n):
    if structure == "sc":
        return generate_simple_cubic(n)
    elif structure == "bcc":
        return generate_body_centered_cubic(n)
    elif structure == "fcc":
        return generate_face_centered_cubic(n)
    else:
        raise ValueError("Invalid cubic_structure specified in config.ini")

# Create a 3D grid of atoms for the simple cubic structure
def generate_simple_cubic(n):
    atomic_positions = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                atomic_positions.append([i * a, j * a, k * a])
    return np.array(atomic_positions)

# Create a 3D grid of atoms for the body-centered cubic structure
def generate_body_centered_cubic(n):
    atomic_positions = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                atomic_positions.append([i * a, j * a, k * a])
    atomic_positions = np.array(atomic_positions)
    offset = a / 2
    atomic_positions += [offset, offset, offset]
    return atomic_positions

# Create a 3D grid of atoms for the face-centered cubic structure
def generate_face_centered_cubic(n):
    atomic_positions = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                atomic_positions.append([i * a, j * a, k * a])
                atomic_positions.append([i * a + a/2, j * a + a/2, k * a])
                atomic_positions.append([i * a + a/2, j * a, k * a + a/2])
                atomic_positions.append([i * a, j * a + a/2, k * a + a/2])
    return np.array(atomic_positions)

# Generate the specified cubic structure
cubic_positions = generate_cubic_structure(cubic_structure, n)

# Save the atomic positions to a file for further use (e.g., visualization)
np.savetxt('cubic_structure_positions.txt', cubic_positions)
