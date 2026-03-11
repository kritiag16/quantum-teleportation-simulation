## Theory of Quantum Teleportation

Quantum teleportation is a protocol that allows the transfer of an unknown quantum state from one location to another without physically sending the particle itself. The protocol relies on **entanglement and classical communication**.

The idea was first proposed in 1993 by Bennett et al. and is a key primitive in quantum communication and distributed quantum computing.

---

### Qubit Representation

A general single-qubit quantum state can be written as

```
|ψ⟩ = α|0⟩ + β|1⟩
```

where:

* **α and β** are complex probability amplitudes
* **|α|² + |β|² = 1**

This state represents the quantum information that Alice wants to transmit to Bob.

---

### Entanglement

Teleportation uses a pair of entangled qubits shared between Alice and Bob. These qubits are prepared in a Bell state:

```
|Φ⁺⟩ = (|00⟩ + |11⟩) / √2
```

This state exhibits **Quantum Entanglement**, meaning that the two qubits cannot be described independently of each other.

Entanglement serves as the quantum resource that enables teleportation.

---

### Teleportation Protocol

The teleportation circuit uses three qubits.

| Qubit | Role                          |
| ----- | ----------------------------- |
| q0    | Alice's unknown quantum state |
| q1    | Alice's entangled qubit       |
| q2    | Bob's qubit                   |

The protocol proceeds as follows.

---

#### 1. State Preparation

Alice prepares the unknown quantum state

```
|ψ⟩
```

that she wishes to teleport.

---

#### 2. Entangled Pair Creation

Alice and Bob share an entangled Bell pair. This is created using:

* Hadamard gate
* Controlled-NOT (CNOT) gate

This produces the Bell state

```
|Φ⁺⟩
```

between qubits q1 and q2.

---

#### 3. Bell Measurement

Alice performs a joint measurement on her two qubits. This is done using:

* CNOT gate
* Hadamard gate

followed by measurement.

This step collapses the system into one of four possible measurement outcomes.

---

#### 4. Classical Communication

Alice sends the two classical bits obtained from her measurement to Bob through a classical channel.

---

#### 5. Conditional Correction

Depending on Alice's measurement result, Bob applies a corrective unitary operation.

| Alice Measurement | Bob Operation |
| ----------------- | ------------- |
| 00                | Identity      |
| 01                | X gate        |
| 10                | Z gate        |
| 11                | ZX gate       |

After this correction, Bob's qubit becomes identical to Alice's original quantum state.

---

### Teleportation Fidelity

To verify that teleportation was successful, we compute the **fidelity** between the original and recovered quantum states.

```
F = |⟨ψ|φ⟩|²
```

where:

* **|ψ⟩** is Alice's original state
* **|φ⟩** is Bob's recovered state

If

```
F = 1
```

the teleportation is perfect.

---

### Teleportation in Noisy Systems

In real quantum hardware, gate imperfections and decoherence introduce noise. These effects reduce teleportation fidelity.

To study this behavior, noise models such as depolarizing noise can be introduced into the simulation. By analyzing teleportation fidelity under different noise levels, we can evaluate the robustness of the teleportation protocol.

---

### Importance of Quantum Teleportation

Quantum teleportation is a foundational concept in quantum information science and is important for:

* quantum communication
* quantum repeaters
* distributed quantum computing
* quantum networks

It demonstrates how quantum information can be transferred using entanglement and classical communication without violating the no-cloning theorem.
