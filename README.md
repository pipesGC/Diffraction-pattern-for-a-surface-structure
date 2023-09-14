# Diffraction-pattern-for-a-surface-structure
## Idea
Draw the non-reconstructed surface structure of a crystal. Consider the adsorption of an element, draw the reconstructed unit cell, check for symmetry conditions and draw the diffraction pattern in the reciprocal space. Evaluate the intensity of the GIXD in (h,k,l).
## Current version
Draw the crystal structure for cubic systems: simple cubic (sc), body-centered cubic (bcc) and face-centered cubic (fcc). In the `config.ini` file it is possible to specify the type of structure, the number of repetitions of the unit cell along each axis, the lattice parameter and the element. Then, by exectuting `main.py` the atomic coordinates will be first evaluated through the `create_cubic_structure.py` module and saved in a txt file, then the `plot_cubic_strucutre.py` module will plot the whole structure. 
**Note:** if the number of repetitions along one axis is set equal to 0, it will raise an error and the excecution will stop.
