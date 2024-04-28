import unittest
from src.qir_compiler.qir_runner import QIRRunner

class TestTeleport(unittest.TestCase):
    def test_teleport(self):
        qir_compiler = QIRCompiler(QIRSpec('teleport.qir'))
        qir_runner = QIRRunner(qir_compiler)
        output = qir_runner.run()
        self.assertIsNotNone(output)