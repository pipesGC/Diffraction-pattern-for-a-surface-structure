import numpy as np
from hypothesis import given, settings
from hypothesis import strategies as st
from create_cubic_structure import generate_cubic_structure, generate_simple_cubic, generate_body_centered_cubic, generate_face_centered_cubic


# generating the variables Nx, Ny and Nz such that they are greater than 0
@given(Nx = st.integers(min_value = 1, max_value = 20), Ny = st.integers(min_value = 1, max_value = 20), Nz = st.integers(min_value = 1, max_value = 20))
@settings(deadline=400)  # Increase the deadline to 400ms
def test_generate_simple_cubic(Nx, Ny, Nz):
    """
    positive test that checks if the function generating
    the atomic coordinates for the simple cubic structure 
    returns an array    
    """
    #Nx, Ny, Nz = 2,2,2
    atomic_positions = generate_simple_cubic(Nx, Ny, Nz)
    assert isinstance(atomic_positions, np.ndarray)


# Test the generate_simple_cubic function
@given(Nx=st.integers(min_value=1, max_value=20), Ny=st.integers(min_value=1, max_value=20), Nz=st.integers(min_value=1, max_value=20))
@settings(deadline=400)  # Increase the deadline to 400ms
def test_count_atoms_sc(Nx, Ny, Nz):
    # Generate atomic positions for SC
    atomic_positions = generate_simple_cubic(Nx, Ny, Nz)
    
    # Calculate the expected number of atomic coordinates for SC
    expected_count = (Nx + 1)*(Ny + 1)*(Nz + 1)
    
    # Check if the number of coordinates matches the expected count
    
    assert len(atomic_positions) == expected_count  

# Test the generate_body_centered_cubic function
@given(Nx=st.integers(min_value=1, max_value=20), Ny=st.integers(min_value=1, max_value=20), Nz=st.integers(min_value=1, max_value=20))
@settings(deadline=400)  # Increase the deadline to 400ms
def test_count_atoms_sc(Nx, Ny, Nz):
    # Generate atomic positions for BCC
    atomic_positions = generate_body_centered_cubic(Nx, Ny, Nz)
    
    # Calculate the expected number of atomic coordinates for BCC
    expected_count = (Nx + 1)*(Ny + 1)*(Nz + 1) + Nx * Ny * Nz
    
    # Check if the number of coordinates matches the expected count
    
    assert len(atomic_positions) == expected_count 