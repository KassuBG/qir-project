class BaseProfile:
    def __init__(self):
        self.num_qubits = 2
        self.num_cbits = 1
        self.gate_set = ['h', 'cx', 'measure']