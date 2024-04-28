import unittest
from src.module.qir_compiler import QIRCompiler

class TestQIRCompiler(unittest.TestCase):
    def test_compile(self):
        qir_spec = QIRSpec('teleport.qir')
        qir_compiler = QIRCompiler(qir_spec)
        compiled_qir = qir_compiler.compile()
        self.assertIsNotNone(compiled_qir)