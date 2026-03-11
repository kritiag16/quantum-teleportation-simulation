#comparison of fidelities for 100 random states
import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, state_fidelity, partial_trace

num_trials = 100

fidelities = []

for i in range(num_trials):
    
    theta = np.random.uniform(0, np.pi)
    phi = np.random.uniform(0, 2*np.pi)
    
    alice_qc = QuantumCircuit(1)
    alice_qc.ry(theta,0)
    alice_qc.rz(phi,0)

    alice_state = Statevector.from_instruction(alice_qc)
    
    qc = QuantumCircuit(3)

    qc.ry(theta,0)
    qc.rz(phi,0)
    
    qc.h(1)
    qc.cx(1,2)

    qc.cx(0,1)
    qc.h(0)

    qc.cx(1,2)
    qc.cz(0,2)

    state = Statevector.from_instruction(qc)

    bob_state = partial_trace(state,[0,1])

    F = state_fidelity(alice_state, bob_state)

    fidelities.append(F)
    
plt.figure(figsize=(8,5))

plt.plot(fidelities, marker='o')

plt.xlabel("Experiment Number")
plt.ylabel("Teleportation Fidelity")
plt.title("Teleportation Fidelity Across Random Quantum States")

plt.ylim(0.9,1.01)

plt.grid(True)

plt.show()
