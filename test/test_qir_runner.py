import unittest
from src.module.qir_runner import QIRRunner

class TestQIRRunner(unittest.TestCase):
    def test_run(self):
        qir_compiler = QIRCompiler(QIRSpec('teleport.qir'))
        qir_runner = QIRRunner(qir_compiler)
        output = qir_runner.run()
        self.assertIsNotNone(output)