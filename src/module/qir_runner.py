from .qir_compiler import QIRCompiler
from .qir_profile import BaseProfile
from qadence import Simulator, QuantumCircuit

class QIRRunner:
    def __init__(self, qir_compiler: QIRCompiler, profile: BaseProfile):
        self.qir_compiler = qir_compiler
        self.profile = profile
        self.results = []

    def run(self):
        # Compile the QIR code
        circuit = self.qir_compiler.compile()

        # Set up the simulator
        simulator = Simulator()
        simulator.set_profile(self.profile.to_dict())

        # Execute the Qadence circuit
        simulator.run(QuantumCircuit)

        # Get the measurement results
        for i in range(self.profile.num_qubits):
            result = simulator.get_measurement(i)
            self.results.append(result)

        # Return the measurement results
        return self.results