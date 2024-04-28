from .qir_spec import QIRSpec
from qadence import QuantumCircuit
import pyqir
import pyqir.patterns as patterns
import pyqir.passes as passes
import pyqir.transforms as transforms


""" This implementation uses 'pyqir' package to parse and manipulate the QIR module. 
    It applies a series of passes to optimize the module, and then creates a QuantumCircuit object 
    from the optimized module.
"""
class QIRCompiler:
    def __init__(self, qir_spec: QIRSpec):
        self.qir_spec = qir_spec

    def compile(self) -> QuantumCircuit:
        # Compile the QIR specification into a QuantumCircuit object

        # Load the QIR module
        module = pyqir.QModule.load(self.qir_spec.qir_file)

        # Apply QIR passes to optimize the module
        passes.apply_passes(module, [
            transforms.ConvertQIRToQASM(),
            transforms.RemoveDeadFunctions(),
            transforms.RemoveDeadVariables(),
            transforms.EliminateCommonSubexpressions(),
            transforms.EliminateEmptyBlocks(),
            transforms.EliminateUnreachableBlocks(),
            transforms.LowerTypeConversions(),
            transforms.LowerToSsa(),
            transforms.PromoteAllocaToRegister(),
            transforms.RemoveRedundantUses(),
            patterns.SimplifyIntrinsics(),
        ])

        # Create a QuantumCircuit object from the QIR module
        circuit = QuantumCircuit(self.qir_spec.num_qubits)
        for func in module.functions:
            if func.name == '__quantum__main__':
                for block in func.blocks:
                    for inst in block.instructions:
                        if inst.opname == 'quantum.exec':
                            for op in inst.operands:
                                if op.opname == 'quantum.measure':
                                    qubit = op.operands[0].value
                                    cbit = op.operands[1].value
                                    circuit.measure(qubit, cbit)
                                elif op.opname == 'quantum.apply':
                                    gate = op.operands[0].value
                                    qubits = [q.value for q in op.operands[1].qubits]
                                    if gate == 'quantum.rz':
                                        circuit.rz(*qubits, op.operands[1].arg)
                                    elif gate == 'quantum.x':
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
                                    elif gate == 'quantum.swap':
                                        circuit.swap(*qubits)
                                    elif gate == 'quantum.cx':
                                        circuit.cx(*qubits)
                                    elif gate == 'quantum.cz':
                                        circuit.cz(*qubits)
                                    elif gate == 'quantum.cp':
                                        circuit.cp(*qubits, op.operands[1].arg)
                                    elif gate == 'quantum.cpH':
                                        circuit.cpH(*qubits, op.operands[1].arg)
                                    elif gate == 'quantum.r':
                                        circuit.r(*qubits, op.operands[1].arg)
                                    elif gate == 'quantum.ry':
                                        circuit.ry(*qubits, op.operands[1].arg)
                                    elif gate == 'quantum.rxx':
                                        circuit.rxx(*qubits, op.operands[1].arg)
                                    elif gate == 'quantum.ryy':
                                        circuit.ryy(*qubits, op.operands[1].arg)
                                    elif gate == 'quantum.rzz':
                                        circuit.rzz(*qubits, op.operands[1].arg)
                                    elif gate == 'quantum.swap':
                                        circuit.swap(*qubits)
                                    elif gate == 'quantum.iswap':
                                        circuit.iswap(*qubits)
                                    elif gate == 'quantum.sx':
                                        circuit.sx(*qubits)
                                    elif gate == 'quantum.sxdg':
                                        circuit.sxdg(*qubits)
                                    elif gate == 'quantum.t':
                                        circuit.t(*qubits)
                                    elif gate == 'quantum.tdg':
                                        circuit.tdg(*qubits)
                                    elif gate == 'quantum.u1':
                                        circuit.u1(*qubits, op.operands[1].arg)
                                    elif gate == 'quantum.u2':
                                        circuit.u2(*qubits, op.operands[1].arg, op.operands[2].arg)
                                    elif gate == 'quantum.u3':
                                        circuit.u3(*qubits, op.operands[1].arg, op.operands[2].arg, op.operands[3].arg)
                                    else:
                                        raise ValueError(f'Unsupported gate: {gate}')

        return circuit
    