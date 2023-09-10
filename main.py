import subprocess

# Run create_cubic_structure.py to generate the cubic structure
print("Generating the cubic structure...")
subprocess.run(["python", "create_cubic_structure.py"])

# Run plot_cubic_structure.py to plot the cubic structure
print("Plotting the cubic structure...")
subprocess.run(["python", "plot_cubic_structure.py"])

print("Done.")