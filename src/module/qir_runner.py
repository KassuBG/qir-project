from .qir_compiler import QIRCompiler
from qadence import Simulator

class QIRRunner:
    def __init__(self, qir_compiler: QIRCompiler):
        self.qir_compiler = qir_compiler
        self.results = []

    def run(self):
        # Compile the QIR code
        circuit = self.qir_compiler.compile()

        # Execute the Qadence circuit
        simulator = Simulator()
        simulator.run(circuit)

        # Return the measurement results
        return self.results