from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import RGQFTMultiplier

q = QuantumRegister(12, 'q') # create a quantum register with 12 qubits q[0:3] for the first number, q[3:6] for the second number, and q[6:12] for the result
c = ClassicalRegister(6, 'c') # create a classical register to store the measurement results

circuit = QuantumCircuit(q, c) # create a quantum circuit

circuit.h(q[0:3]) # apply hadamard gates to the first 3 qubits
circuit.h(q[3:6]) # apply hadamard gates to the next 3 qubits