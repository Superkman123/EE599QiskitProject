from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

q = QuantumRegister(12, 'q') # create a quantum register with 12 qubits q[0:3] for the first number, q[3:6] for the second number, and q[6:12] for the result
c = ClassicalRegister(6, 'c') # create a classical register to store the measurement results

circuit = QuantumCircuit(q, c) # create a quantum circuit

circuit.h(q[0:3]) # apply hadamard gates to the first 3 qubits
circuit.h(q[3:6]) # apply hadamard gates to the next 3 qubits

# use Toffoli gates to compute the products of the bits and store them in the result qubits similar to our first project
circuit.ccx(q[0], q[3], q[6]) # q[6] = a[0] AND b[0]
circuit.ccx(q[0], q[4], q[7]) # q[7] = a[0] AND b[1]
circuit.ccx(q[0], q[5], q[8]) # q[8] = a[0] AND b[2]

circuit.ccx(q[1], q[3], q[7]) # q[7] = q[7] XOR (a[1] AND b[0])
circuit.ccx(q[1], q[4], q[8]) # q[8] = q[8] XOR (a[1] AND b[1])
circuit.ccx(q[1], q[5], q[9]) # q[9] = q[9] XOR (a[1] AND b[2])

circuit.ccx(q[2], q[3], q[8]) # q[8] = q[8] XOR (a[2] AND b[0])
circuit.ccx(q[2], q[4], q[9]) # q[9] = q[9] XOR (a[2] AND b[1])
circuit.ccx(q[2], q[5], q[10]) # q[10] = q[10] XOR (a[2] AND b[2])

# measure the result qubits
circuit.measure(q[6],c[0])
circuit.measure(q[7],c[1])
circuit.measure(q[8],c[2])
circuit.measure(q[9],c[3])
circuit.measure(q[10],c[4])
circuit.measure(q[11],c[5])

print(circuit)

# Run AerSimulator
simulator = AerSimulator()
job = simulator.run(circuit, shots=1024)
result = job.result()
counts = result.get_counts()
print(counts)
