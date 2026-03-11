import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, state_fidelity, partial_trace
from qiskit_aer.noise import NoiseModel, depolarizing_error

def teleportation_circuit(theta, phi):

    qc = QuantumCircuit(3)

    qc.ry(theta,0)
    qc.rz(phi,0)

    qc.h(1)
    qc.cx(1,2)

    qc.cx(0,1)
    qc.h(0)

    qc.cx(1,2)
    qc.cz(0,2)

    return qc

def create_noise(p):

    noise_model = NoiseModel()

    error1 = depolarizing_error(p,1)
    error2 = depolarizing_error(p,2)

    noise_model.add_all_qubit_quantum_error(error1, ['h','x','z','ry','rz'])
    noise_model.add_all_qubit_quantum_error(error2, ['cx'])

    return noise_model

noise_levels = np.linspace(0,0.2,10)
avg_fidelity = []


for p in noise_levels:

    noise_model = create_noise(p)

    fidelities = []

    for i in range(100):

        theta = np.random.uniform(0,np.pi)
        phi = np.random.uniform(0,2*np.pi)
        
        alice_qc = QuantumCircuit(1)
        alice_qc.ry(theta,0)
        alice_qc.rz(phi,0)

        alice_state = Statevector.from_instruction(alice_qc)

        qc = teleportation_circuit(theta,phi)

        sim = AerSimulator(method="density_matrix", noise_model=noise_model)
        
        qc.save_density_matrix()

        result = sim.run(qc).result()

        state = result.data(0)["density_matrix"]

        bob_state = partial_trace(state, [0,1])

        F = state_fidelity(alice_state,bob_state)

        fidelities.append(F)

    avg_fidelity.append(np.mean(fidelities))

plt.figure(figsize=(8,5))

plt.plot(noise_levels, avg_fidelity, marker='o')

plt.xlabel("Noise Probability")
plt.ylabel("Average Teleportation Fidelity")

plt.title("Teleportation Fidelity vs Noise")

plt.grid(True)

plt.show()
