from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import RGQFTMultiplier
from qiskit.tools.monitor import job_monitor


q = QuantumRegister(12, 'q') # create a quantum register with 12 qubits q[0:3] for the first number, q[3:6] for the second number, and q[6:12] for the result
c = ClassicalRegister(6, 'c') # create a classical register to store the measurement results

circuit = QuantumCircuit(q, c) # create a quantum circuit

circuit.h(q[0:3]) # apply hadamard gates to the first 3 qubits
circuit.h(q[3:6]) # apply hadamard gates to the next 3 qubits

circuit1 = RGQFTMultiplier(num_state_qubits=3, num_result_qubits=6)
circuit = circuit.compose(circuit1)

circuit.measure(q[7],c[0])
circuit.measure(q[8],c[1])
circuit.measure(q[9],c[2])
circuit.measure(q[10],c[3])
circuit.measure(q[11],c[4])
circuit.measure(q[12],c[5])

print(circuit)

job = execute(circuit, backend, shots=1024)
result = job.result()
counts = result.get_counts()

print(counts)
