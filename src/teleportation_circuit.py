#teleportation for 1024 shots
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit_aer import AerSimulator

q = QuantumRegister(3)
c = ClassicalRegister(2)

qc = QuantumCircuit(q, c)

theta = np.random.uniform(0, np.pi)
phi = np.random.uniform(0, 2*np.pi)

qc.ry(theta, q[0])
qc.rz(phi, q[0])

qc.h(q[1])
qc.cx(q[1], q[2])

qc.cx(q[0], q[1])
qc.h(q[0])

qc.measure(q[0], c[0])
qc.measure(q[1], c[1])

with qc.if_test((c, 1)):
    qc.x(q[2])

with qc.if_test((c, 2)):
    qc.z(q[2])

with qc.if_test((c, 3)):
    qc.x(q[2])
    qc.z(q[2])
