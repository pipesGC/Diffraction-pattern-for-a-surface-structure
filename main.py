import subprocess
import configparser
import sys

# Read configuration from the 'config.ini' file
config = configparser.ConfigParser()
config.read('config.ini')

# Extract repetition parameters from configuration
Nx = int(config.get('repetitions', 'Nx'))
Ny = int(config.get('repetitions', 'Ny'))
Nz = int(config.get('repetitions', 'Nz'))

# Check if at least one of Nx, Ny, or Nz is zero
if Nx == 0 or Ny == 0 or Nz == 0:
    print("Error: At least one of Nx, Ny, or Nz is equal to zero. Program will not proceed.")
    sys.exit(1)  # Raise an error and stop the program

# Run create_cubic_structure.py to generate the cubic structure
print("Generating the cubic structure...")
subprocess.run(["python", "create_cubic_structure.py"])

# Run plot_cubic_structure.py to plot the cubic structure
print("Plotting the cubic structure...")
subprocess.run(["python", "plot_cubic_structure.py"])

print("Done.")
