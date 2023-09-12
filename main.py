import subprocess
import configparser
import os

# Read configuration from the 'config.ini' file
config = configparser.ConfigParser()
config.read('config.ini')

# Run create_cubic_structure.py to generate the cubic structure
try:
    print("Generating the cubic structure...")
    create_structure_result = subprocess.run(["python", "create_cubic_structure.py"])

    # Check the return code of create_cubic_structure.py
    if create_structure_result.returncode != 0:
        raise ValueError("Error occurred in create_cubic_structure.py")

    # Check if the 'cubic_structure_positions.txt' file exists
    if not os.path.isfile('cubic_structure_positions.txt'):
        raise FileNotFoundError("Error: 'cubic_structure_positions.txt' file not found after running create_cubic_structure.py.")

    # Run plot_cubic_structure.py to plot the cubic structure
    print("Plotting the cubic structure...")
    subprocess.run(["python", "plot_cubic_structure.py"])

    print("Done.")  
except subprocess.CalledProcessError as e:
    print(f"Error: Subprocess error occurred - {e}")
except ValueError as e:
    print(f"Error: {e}")
except FileNotFoundError as e:
    print(f"Error: {e}")
