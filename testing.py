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
