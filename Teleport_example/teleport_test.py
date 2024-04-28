import unittest
from src.module.qir_runner import QIRRunner
from src.module.qir_compiler import QIRCompiler
from src.module.qir_spec import QIRSpec
from qadence import QuantumCircuit

class TestTeleport(unittest.TestCase):
    def test_teleport(self):
        
        """ The implementation checks that the run method returns a QuantumCircuit object, 
        and that the number of qubits and classical bits match those of the QuantumCircuit object 
        created by the QIRSpec constructor and the QIRSpec class has a circuit attribute that contains 
        the QuantumCircuit object created by the parse_qir_file method.
        """
        
        qir_spec = QIRSpec('teleport.qir')
        qir_compiler = QIRCompiler(qir_spec)
        qir_runner = QIRRunner(qir_compiler)
        output = qir_runner.run()
        self.assertIsInstance(output, QuantumCircuit)
        self.assertEqual(output.num_qubits, qir_spec.circuit.num_qubits)
        self.assertEqual(output.num_cbits, qir_spec.circuit.num_cbits)        