from .qir_compiler import QIRCompiler
from qadence import Simulator

class QIRRunner:
    def __init__(self, qir_compiler: QIRCompiler):
        self.qir_compiler = qir_compiler

    def run(self) -> str:
        # Run the compiled QIR intermediate representation
        simulator = Simulator()
        simulator.run(self.qir_compiler.compile())
        return simulator.output