#recovery of teleported state at bobs end
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, state_fidelity
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import partial_trace
%matplotlib inline

theta = np.random.uniform(0, np.pi)
phi = np.random.uniform(0, 2*np.pi)

alice_qc = QuantumCircuit(1)
alice_qc.ry(theta,0)
alice_qc.rz(phi,0)

alice_state = Statevector.from_instruction(alice_qc)

print("Alice original state:")
print(alice_state)

qc = QuantumCircuit(3)

qc.ry(theta,0)
qc.rz(phi,0)

qc.h(1)
qc.cx(1,2)

qc.cx(0,1)
qc.h(0)

qc.cx(1,2)
qc.cz(0,2)

print("\nTeleportation Circuit:")
print(qc.draw())

state = Statevector.from_instruction(qc)

bob_state = partial_trace(state, [0,1])

print("\nRecovered Bob state:")
print(bob_state)

F = state_fidelity(alice_state, bob_state)

print("\nTeleportation fidelity:", F)

alice_fig = plot_bloch_multivector(alice_state)
plt.title("Alice Recovered Qubit State")
plt.show()

bob_fig = plot_bloch_multivector(bob_state)
plt.title("Bob Recovered Qubit State")
plt.show()
