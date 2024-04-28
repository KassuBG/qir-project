import unittest
from src.module.qir_compiler import QIRCompiler
from src.module.qir_spec import QIRSpec
from qadence import QuantumCircuit

class TestQIRCompiler(unittest.TestCase):
    
    """ This implementation checks that the compile method returns a QuantumCircuit object, 
    and that the number of qubits and classical bits match those specified in the QIRSpec. 
    """
    def test_compile(self):
        qir_spec = QIRSpec('teleport.qir')
        qir_compiler = QIRCompiler(qir_spec)
        compiled_qir = qir_compiler.compile()
        self.assertIsInstance(compiled_qir, QuantumCircuit)
        self.assertEqual(compiled_qir.num_qubits, qir_spec.num_qubits)
        self.assertEqual(compiled_qir.num_cbits, qir_spec.num_cbits)