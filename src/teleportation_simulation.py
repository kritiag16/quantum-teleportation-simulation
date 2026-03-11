sim = AerSimulator()

result = sim.run(qc, shots=1024).result()
counts = result.get_counts()

print("Measurement Results:")
print(counts)

print("\nCircuit:")
print(qc.draw())
