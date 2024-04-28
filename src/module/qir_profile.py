""" 
This implementation uses the default values for the number of qubits, 
number of classical bits, and gate set.

Also adds a to_dict method that returns a dictionary representation of the profile. 
This can be useful for serializing and deserializing the profile.

"""

class BaseProfile:
    def __init__(self):
        self.num_qubits = 2
        self.num_cbits = 1
        self.gate_set = ['h', 'cx', 'measure']

    def to_dict(self):
        return {
            'num_qubits': self.num_qubits,
            'num_cbits': self.num_cbits,
            'gate_set': self.gate_set
        }