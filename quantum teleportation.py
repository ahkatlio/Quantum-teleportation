from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

#register with 3 qubits
qr = QuantumRegister(3)

# classical register with 3 bits
cr = ClassicalRegister(3)
qc = QuantumCircuit(qr, cr)
qc.x(qr[0])
qc.h(qr[0])

#Bell state preparation
qc.h(qr[1])
qc.cx(qr[1], qr[2])

# the teleportation
qc.cx(qr[0], qr[1])
qc.h(qr[0])
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])
qc.cx(qr[1], qr[2])
qc.cz(qr[0], qr[2])

#Measure 
qc.measure(qr[2], cr[2])

backend = Aer.get_backend('qasm_simulator')
result = execute(qc, backend).result()
print(result.get_counts())
