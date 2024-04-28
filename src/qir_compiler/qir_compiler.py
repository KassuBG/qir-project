from .qir_spec import QIRSpec
from qadence import Compiler

class QIRCompiler:
    def __init__(self, qir_spec: QIRSpec):
        self.qir_spec = qir_spec

    def compile(self) -> str:
        # Compile the QIR specification into an intermediate representation
        compiler = Compiler()
        compiler.compile(self.qir_spec.circuit)
        return compiler.output