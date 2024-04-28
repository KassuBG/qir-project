from qadence import QuantumCircuit
import pyqir

""" file imports the QuantumCircuit class from the qadence library, 
    and uses it to define the parse_qir_file method.
"""    
    
class QIRSpec:
    def __init__(self, qir_file: str):
        self.qir_file = qir_file
        self.circuit = self.parse_qir_file()

    def parse_qir_file(qir_file: str) -> QuantumCircuit:
        # Parse the QIR file and return a QuantumCircuit object
        module = pyqir.QModule.load(qir_file)
        circuit = QuantumCircuit()

        for func in module.functions:
            if func.name == '__quantum__main__':
                for block in func.blocks:
                    for inst in block.instructions:
                        if inst.opname == 'quantum.apply':
                            gate = inst.operands[0].value
                            qubits = [q.value for q in inst.operands[1].qubits]
                            if gate == 'quantum.x':
                                circuit.x(*qubits)
                            elif gate == 'quantum.y':
                                circuit.y(*qubits)
                            elif gate == 'quantum.z':
                                circuit.z(*qubits)
                            elif gate == 'quantum.h':
                                circuit.h(*qubits)
                            elif gate == 'quantum.s':
                                circuit.s(*qubits)
                            elif gate == 'quantum.sdg':
                                circuit.sdg(*qubits)
                            elif gate == 'quantum.t':
                                circuit.t(*qubits)
                            elif gate == 'quantum.tdg':
                                circuit.tdg(*qubits)
                            elif gate == 'quantum.rx':
                                circuit.rx(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.ry':
                                circuit.ry(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.rz':
                                circuit.rz(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.cx':
                                circuit.cx(*qubits)
                            elif gate == 'quantum.cz':
                                circuit.cz(*qubits)
                            elif gate == 'quantum.swap':
                                circuit.swap(*qubits)
                            elif gate == 'quantum.rxx':
                                circuit.rxx(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.ryy':
                                circuit.ryy(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.rzz':
                                circuit.rzz(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.iswap':
                                circuit.iswap(*qubits)
                            elif gate == 'quantum.sx':
                                circuit.sx(*qubits)
                            elif gate == 'quantum.sxdg':
                                circuit.sxdg(*qubits)
                            elif gate == 'quantum.cp':
                                circuit.cp(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.cpH':
                                circuit.cpH(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.cpx':
                                circuit.cpx(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.cpHx':
                                circuit.cpHx(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.cpdg':
                                circuit.cpdg(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.cpdgx':
                                circuit.cpdgx(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.cphase':
                                circuit.cphase(*qubits, inst.operands[1].arg)
                            elif gate == 'quantum.ccx':
                                circuit.ccx(*qubits)
                            elif gate == 'quantum.ccz':
                                circuit.ccz(*qubits)
                            elif gate == 'quantum.toffoli':
                                circuit.toffoli(*qubits)
                            elif gate == 'quantum.reset':
                                circuit.reset(*qubits)
                            elif gate == 'quantum.measure':
                                circuit.measure(*qubits)
                            else:
                                raise ValueError(f'Unsupported gate: {gate}')

        return circuit   
