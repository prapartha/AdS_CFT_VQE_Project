import numpy as np
from qiskit.quantum_info import SparsePauliOp, Statevector
# from svqefinalcheck import generate_syk_hamiltonian

def test_hamiltonian_hermitian(generate_syk_hamiltonian):
    H = generate_syk_hamiltonian(n_qubits=3, J=1.0, seed=123)
    assert np.max(np.abs(np.imag(H.coeffs))) < 1e-10

def test_state_expectation(generate_syk_hamiltonian):
    H = generate_syk_hamiltonian(n_qubits=3, J=1.0, seed=42)
    s = Statevector.from_label('0'*3)
    val = float(s.expectation_value(H))
    assert np.isfinite(val)
